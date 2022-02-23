"""Controller for playing casino!!"""
from logging import getLogger, INFO
from selenium.common import exceptions


from betman.models.entity import player
from betman.views import input
import time

def play_roullet():
    """Function to play roullet"""
    menu = input.Menu()
    user_info = menu.get_user_info()
    play(user_info, menu)

def play(user_info, menu):
        """player1 = player.RoulletPlayer(mailaddress=user_info["mail"],password=user_info["password"], base_amount=user_info["base_amount"], roop_num=user_info["roop_num"])"""
        player1 = player.RoulletPlayer(mailaddress=user_info["mail"],password=user_info["password"])
        player1.access_to_casino()
        if not player1.login():
            menu.show_error_message_cannot_login()
        else:
            time.sleep(3)
            player1.transfer_to_roullet()
            time.sleep(15)
            player1.play_roullet()
            player1.logout()
            player1.quit()
    




