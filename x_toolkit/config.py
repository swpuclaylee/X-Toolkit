import os
from dotenv import load_dotenv

# 加载 .env文件中的环境变量
load_dotenv()


class Config:
    """
    配置管理类
    """
    # TOKEN AND SECRET KEY
    API_KEY = os.getenv("TWITTER_API_KEY")
    API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
    ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

    # 日志配置
    LOG_FOLDER = os.getenv("LOG_FOLDER", "logs")
    LOG_NAME = os.getenv("LOG_NAME", "x_toolkit")

    @classmethod
    def validate(cls):
        if not all([
            cls.API_KEY,
            cls.API_SECRET_KEY,
            cls.ACCESS_TOKEN,
            cls.ACCESS_TOKEN_SECRET,
            cls.BEARER_TOKEN
        ]):
            raise ValueError("缺少必要的配置项，请检查 .env 文件或环境变量。")

# # 初始化时候进行配置验证
# Config.validate()
