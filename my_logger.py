# -*- coding:utf-8 -*-
from logging import Formatter, StreamHandler, getLogger, INFO
import logging
import os


def root_logger():
    logging.basicConfig(filename='./resources/roullet.log', level=INFO, format='{asctime} [{levelname:.4}] {name}: {message}', style='{')

    # root loggerを取得
    logger = getLogger()

    # formatterを作成
    formatter = Formatter('%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s')


    # handlerを作成しフォーマッターを設定
    handler = StreamHandler()
    handler.setFormatter(formatter)


    # loggerにhandlerを設定、イベント捕捉のためのレベルを設定
    logger.addHandler(handler)


    return logger