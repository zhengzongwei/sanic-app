# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.

import os
import logging

from logging import handlers


def config_log(log_level="INFO"):
    logs_dir = os.path.join(os.path.dirname(__file__), "logs")

    # log_path = os.path.join()
    if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
        pass
    else:
        os.makedirs(logs_dir)

    log_file_name = os.path.join(logs_dir, 'log.log')
    
    # clean old root logger handles
    logging.getLogger("").handlers = []

    file_handler = handlers.RotatingFileHandler(
        filename=log_file_name,
        mode='a',
        maxBytes=1024 * 1024 * 100,
        backupCount=1,
        encoding='utf-8',
    )
    formatter = logging.Formatter("[%(asctime)s %(msecs)03d][%(process)d][tid=%(thread)d][%(name)s][file:%(filename)s func:%(funcName)s line:%(lineno)s][%(levelname)s] %(message)s ", datefmt="%Y-%m-%d %H:%M:%S")
    console_formatter = logging.Formatter("[%(asctime)s %(msecs)03d][file:%(filename)s func:%(funcName)s line:%(lineno)s] [%(levelname)s] %(message)s ", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)

    console_logger = logging.StreamHandler()
    console_logger.setFormatter(console_formatter)
    logging.getLogger(__name__).addHandler(file_handler)
    logging.getLogger(__name__).addHandler(console_logger)

    logger = logging.getLogger(__name__)
    level = log_level.upper()
    logger.setLevel(level)
    return logger
    






