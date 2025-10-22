#-*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name=None):
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # 이미 설정되어 있으면 중복 설정 방지

    logger.setLevel(logging.INFO)

    # 콘솔 + 파일 핸들러
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )
    console = logging.StreamHandler()
    file = RotatingFileHandler("app.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding='utf-8')

    console.setFormatter(formatter)
    file.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file)
    return logger

# ✅ 전역으로 바로 쓸 기본 로거
logger = setup_logger(__name__)

# def setup_logging():
#     logging_config = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'formatters': {
#             'default': {
#                 'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#             },
#         },
#         'handlers': {
#             'console': {
#                 'class': 'logging.StreamHandler',
#                 'formatter': 'default',
#                 'level': 'INFO',
#             },
#             'file': {
#                 'class': 'logging.FileHandler',
#                 'formatter': 'default',
#                 'filename': 'qe_tools.log',
#                 'level': 'DEBUG',
#             },
#         },
#         'root': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#         },
#     }
    
#     logging.config.dictConfig(logging_config)

