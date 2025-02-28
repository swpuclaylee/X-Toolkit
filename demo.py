import requests
import os

# 设置 API 基本信息
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPJZzgEAAAAA2esf3GwDM%2BdfE%2BdAMMKZ5mdr9wI%3DQthLoWm8DU0xyC5JFjAcodCsSNtbc8nrWMLTSljm9QwEoZ1cgQ"

# 定义API请求头
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}

# 用户名
username = "clay09903793"  # 替换为你想查询的用户名

# API 请求URL
url = f"https://api.twitter.com/2/users/by/username/{username}"

# 发起请求
response = requests.get(url, headers=headers)

# 获取并打印用户的数字 ID
if response.status_code == 200:
    user_data = response.json()
    print(f"User ID of {username}: {user_data['data']['id']}")
else:
    print(f"Failed to fetch user ID: {response.status_code}")
