import my_logger
import betman.controller.play_casino


if __name__ == '__main__':
    # root logger作成
    logger = my_logger.root_logger()
    logger.info('Roullet Player is started!!!')
betman.controller.play_casino.play_roullet()
