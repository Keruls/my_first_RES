import logging
import logging.handlers
import os
import traceback


def fun01():
    # logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # handler
    if os.path.exists('./log'):
        pass
    else:
        os.mkdir('./log')
    handler = logging.handlers.TimedRotatingFileHandler('./log/log.log')
    handler.setLevel(logging.DEBUG )
    # formatter
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    # set formatter for handler
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


def fun02(a,b):
    try:
        c = a+ b
        print(c)
    except Exception as e:
        log = fun01()
        log.error(e)
        log.error(traceback.format_exc())

fun02(1, '1')


