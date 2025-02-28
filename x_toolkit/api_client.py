import requests
import datetime
from requests_oauthlib import OAuth1
from x_toolkit.config import Config
from x_toolkit.utils.logger import get_logger


class XApiClient:
    """
    X API 客户端，封装 X API的调用。
    """

    def __init__(self):
        self.logger = get_logger(Config.LOG_NAME)
        self.auth = OAuth1(
            Config.API_KEY,
            Config.API_SECRET_KEY,
            Config.ACCESS_TOKEN,
            Config.ACCESS_TOKEN_SECRET,
        )

    def _make_request(self, method, url, **kwargs):
        """
        发送HTTP请求
        :param method:
        :param url:
        :param kwargs:
        :return:
        """
        try:
            response = requests.request(method, url, auth=self.auth, **kwargs)
            response.raise_for_status()
            self.logger.info(f"API 请求成功：{url}")
            return response
        except requests.exceptions.RequestException as e:
            if response.status_code == 429:
                self.logger.warning(
                    f"API 请求失败: {url}, 错误: {e}。{datetime.datetime.utcfromtimestamp(int(response.headers.get('X-Rate-Limit-Reset')))}后可以继续发送API请求")
            else:
                self.logger.error(f"API 请求失败: {url}, 错误: {e}。")
            raise

    def fetch_tweets(self, user_id, **kwargs):
        """
        获取指定用户的推文
        :param user_id:
        :param max_results:
        :return:
        """
        url = f"https://api.twitter.com/2/users/{user_id}/tweets"
        response = self._make_request("GET", url, params=kwargs)
        return response.json()
