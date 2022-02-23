"""Difined a player model"""
import os
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from decimal import Decimal
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

from logging import getLogger, INFO

from betman.models.utils import find_utils
from betman.models.utils import sequence_utils
from betman.models.utils import calc_utils

ENTRY_URL = "https://classic.verajohn.com/ja"
EXIT_URL = "https://classic.verajohn.com/ja/logout"


class Player(object):
    """Base model for Player."""

    def __init__(self, mailaddress, password):
        self._logger = getLogger(__name__)
        self.mailaddress = mailaddress
        self.password = password
        service = Service("./resources/chromedriver")
        service.creationflags = CREATE_NO_WINDOW
        self.browser = webdriver.Chrome(service=service)

    def access_to_casino(self):
        self.browser.get(ENTRY_URL)

    def login(self):
        login_text = self.browser.find_element_by_xpath(
            "//*[@id=\"signin-mail\"]") 
        pass_text = self.browser.find_element_by_xpath(
            "//*[@id=\"signin-pass\"]")

        mailaddress = self.mailaddress
        password = self.password

        login_text.send_keys(mailaddress)
        pass_text.send_keys(password)

        login_btn = self.browser.find_element_by_name("op")
        login_btn.click()
        return self.browser.current_url == 'https://classic.verajohn.com/ja/myaccount/overview'

    def logout(self):
        self.browser.get(EXIT_URL)
    
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)



class RoulletPlayer(Player):
    """Handle data model on player."""
    ROULLET_URL = "https://classic.verajohn.com/ja/play/instant-roulette"

    """def __init__(self, mailaddress, password, base_amount, roop_num):"""

    def __init__(self, mailaddress, password):

        super().__init__(mailaddress=mailaddress, password=password)

        self.base_amount = Decimal('0.1')
        """self.roop_num = int(roop_num)"""
        self.sequence = []
    
    def transfer_to_roullet(self):
        self.browser.get(self.ROULLET_URL)
        time.sleep(3)
        self.transfer_frames()

    def transfer_frames(self):
        iframe = self.browser.find_element_by_css_selector(
            "#gameFrame")
        self.browser.switch_to.frame(iframe)
        self.browser.switch_to.frame("EVO_GAME")

    def play_roullet(self):
        self.previous_amount = self.get_amount()
        self.current_amount = self.get_amount()
        roop_count = 0
        while True:
            self._logger.info(f'credit : ${self.current_amount}')
            if len(self.sequence) < 2:
                self.sequence = sequence_utils.generate(self.base_amount)

            self._logger.info(f'sequence : {self.get_sequence_str()}')
            if roop_count > 0:
                self.logout()
                self.access_to_casino()
                self.login()
                self.transfer_to_roullet()
                time.sleep(10)

            while True:
                total_betting_amount = calc_utils.get_betting_amount(
                    self.sequence)
                self._logger.info(f'betting_amount : ${total_betting_amount}')
                self.bet(total_betting_amount)
                self.current_amount = self.get_amount()
                if self.current_amount.compare(self.previous_amount) >= 1:
                    self.sequence = sequence_utils.remove_both_ends(
                        self.sequence)
                    self._logger.info(
                        f'You win!!! Got ${total_betting_amount * 3}')
                else:
                    self.sequence = sequence_utils.add_num(self.sequence)
                    self._logger.info('You lose.')
                self.previous_amount = self.current_amount

                if len(self.sequence) < 2:
                    self._logger.info('A set is over')
                    break

            roop_count += 1

    def bet(self, amount):
        total_betting_amount = amount
        betting_grid_path = find_utils.select_betting_grid_path()
        count = 0
        try:
            while total_betting_amount > 0:
                betting_amount = calc_utils.select_chip(total_betting_amount)
                total_betting_amount = total_betting_amount - betting_amount
                self.click_chip(betting_amount)
                self.click_betting_grid(count, betting_grid_path)
                count = count + 1
            self.click_betting_btn()
        except NoSuchElementException as e:
            self._logger.error(e.msg)
            self.logout()
            self.access_to_casino()
            self.login()
            self.transfer_to_roullet()
            self.play_roullet()

    def quit(self):
        self.browser.quit()

    def get_amount(self):
        self._logger.info("getting current credit...")
        return Decimal(self.browser.find_element_by_xpath(
            find_utils.get_current_amount_path()).get_attribute("textContent").replace(",", ""))

    def click_betting_grid(self, count, betting_grid_path):
        self._logger.info("click a betting grid.")
        if count == 0:
            betting_grid = self.browser.find_element_by_css_selector(
                betting_grid_path[0])
        else:
            betting_grid = self.browser.find_element_by_css_selector(
                betting_grid_path[1])
        betting_grid.click()

    def click_chip(self, betting_amount):
        self._logger.info(f"choosing a chip...${betting_amount}")
        chip = find_utils.select_chip_path(betting_amount)
        chip_path = self.browser.find_element_by_css_selector(chip)
        chip_path.click()

    def click_betting_btn(self):
        self._logger.info("click a betting button.")
        betting_btn = "//*[@id=\"root\"]/div/div/div/div[7]/div/div[3]/div[3]/div/div[1]/div[1]/button"
        self.browser.find_element_by_xpath(betting_btn).click()
        self._logger.info("Now betting... Please wait.")
        time.sleep(40)

    def get_sequence_str(self):
        sequence_str = []
        for decimal_num in self.sequence:
            sequence_str.append(str(decimal_num))
        return sequence_str
