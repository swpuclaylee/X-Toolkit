import requests
from x_toolkit.config import Config


def get_user_id(username):
    """
    获取指定用户名的用户 ID。

    :param username: 用户名
    :return: 用户 ID
    """
    # 定义API请求头
    headers = {
        "Authorization": f"Bearer {Config.BEARER_TOKEN}",
    }
    response = requests.get(f"https://api.twitter.com/2/users/by/username/{username}", headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        return user_data["data"]["id"]
    else:
        raise ValueError(f"无法获取用户 {username} 的数字 ID: {response.status_code} {response.text}")

