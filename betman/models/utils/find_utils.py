"""Find a element from application page"""

import random
from decimal import Decimal


def select_chip_path(amount):
    ZERO_ONE = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(1) > div.chip--768ce > svg > g > circle.text-background--9cda6"
    ZERO_TWO = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(2) > div.chip--768ce > svg > g > circle.text-background--9cda6"
    ZERO_FIVE = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(3) > div.chip--768ce > svg > g > circle.text-background--9cda6"
    ONE = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(4) > div.chip--768ce > svg > g > circle.text-background--9cda6"
    TWO = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(5) > div.chip--768ce > svg > g > circle.text-background--9cda6"
    FIVE = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(6) > div.chip--768ce > svg > g > circle.text-background--9cda6"
    TWENTY_FIVE = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(7) > div.chip--768ce > svg > g > circle.text-background--9cda6"
    ONE_HUNDRED = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(8) > div.chip--768ce > svg > g > circle.text-background--9cda6"
    FIVE_HUNDRED = "#root > div > div > div > div.footerWrapper--3a742 > div > div.chipStack--ca889 > div > div.expandedWrapper--8f09c > div > div:nth-child(9) > div.chip--768ce > svg > g > circle.text-background--9cda6"

    chips = {Decimal("0.1"): ZERO_ONE, Decimal("0.2"): ZERO_TWO, Decimal("0.5"): ZERO_FIVE, Decimal("1"): ONE, Decimal(
        "2"): TWO, Decimal("5"): FIVE, Decimal("25"): TWENTY_FIVE, Decimal("100"): ONE_HUNDRED, Decimal("500"): FIVE_HUNDRED}

    return chips[amount]


def select_betting_grid_path():
    FIRST_TWELVE = ("#root > div > div > div > div.footerWrapper--3a742 > div > div.perspectiveContainer--b459a > div.bettingGrid--217c5 > div > div.perspectiveContainer--87027 > div > div > div.svg-wrapper--86340 > div > svg > g > rect:nth-child(44)",
                    "#bet_1st12 > div > svg > g > circle.text-background--9cda6")
    SECOND_TWELVE = ("#root > div > div > div > div.footerWrapper--3a742 > div > div.perspectiveContainer--b459a > div.bettingGrid--217c5 > div > div.perspectiveContainer--87027 > div > div > div.svg-wrapper--86340 > div > svg > g > rect:nth-child(45)",
                     "#bet_2nd12 > div > svg > g > circle.text-background--9cda6")
    THIRD_TWELVE = ("#root > div > div > div > div.footerWrapper--3a742 > div > div.perspectiveContainer--b459a > div.bettingGrid--217c5 > div > div.perspectiveContainer--87027 > div > div > div.svg-wrapper--86340 > div > svg > g > rect:nth-child(46)",
                    "#bet_3rd12 > div > svg > g > circle.text-background--9cda6")

    TOP = ("#root > div > div > div > div.footerWrapper--3a742 > div > div.perspectiveContainer--b459a > div.bettingGrid--217c5 > div > div.perspectiveContainer--87027 > div > div > div.svg-wrapper--86340 > div > svg > g > rect:nth-child(47)",
           "#bet_top2to1 > div > svg > g > circle.text-background--9cda6")
    MIDDLE = ("#root > div > div > div > div.footerWrapper--3a742 > div > div.perspectiveContainer--b459a > div.bettingGrid--217c5 > div > div.perspectiveContainer--87027 > div > div > div.svg-wrapper--86340 > div > svg > g > rect:nth-child(48)",
              "#bet_middle2to1 > div > svg > g > circle.text-background--9cda6")
    BOTTOM = ("#root > div > div > div > div.footerWrapper--3a742 > div > div.perspectiveContainer--b459a > div.bettingGrid--217c5 > div > div.perspectiveContainer--87027 > div > div > div.svg-wrapper--86340 > div > svg > g > rect:nth-child(49)",
              "#bet_bottom2to1 > div > svg > g > circle.text-background--9cda6")

    generated_num = random.randint(1, 6)

    betting_grids = {1: FIRST_TWELVE, 2: SECOND_TWELVE,
                     3: THIRD_TWELVE, 4: TOP, 5: MIDDLE, 6: BOTTOM}

    return betting_grids[generated_num]


def get_current_amount_path():
    return "//*[@id=\"root\"]/div/div/div/div[9]/div[3]/div/div/div[1]/div/span[2]/span[2]"
