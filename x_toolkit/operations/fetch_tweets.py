from x_toolkit.api_client import XApiClient
from x_toolkit.utils.logger import get_logger
from x_toolkit.config import Config

logger = get_logger(Config.LOG_NAME)


def fetch_tweets(user_id, max_results=10, pagination_token=None, exclude_replies=False, exclude_retweets=False):
    """
    获取指定用户的推文。

    :param user_id: 用户 ID
    :param max_results: 最大返回的推文数量（默认 10 条）
    :param pagination_token: 分页令牌
    :param exclude_replies: 是否排除回复
    :param exclude_retweets: 是否排除转发
    :return: 推文列表和分页令牌
    """
    try:
        client = XApiClient()
        params = {"max_results": max_results}

        # 分页
        if pagination_token:
            params["pagination_token"] = pagination_token

        # 过滤推文类型
        exclude = []
        if exclude_replies:
            exclude.append("replies")
        if exclude_retweets:
            exclude.append("retweets")
        if exclude:
            params["exclude"] = ",".join(exclude)

        response = client.fetch_tweets(user_id, **params)
        # 提取推文数据和分页令牌
        tweets = response.get("data", [])
        next_token = response.get("meta", {}).get("next_token")
        logger.info(f"Fetched {len(tweets)} tweets for user {user_id}")
        return tweets, next_token
    except Exception as e:
        logger.error(f"Error fetching tweets for user {user_id}: {e}")
        raise


if __name__ == "__main__":
    # 示例用法
    user_id = 1520843497464791040

    tweets, next_token = fetch_tweets(user_id)
    result = f"Fetched {len(tweets)} tweets for user {user_id}: \n"
    for tweet in tweets:
        result += f"- {tweet['text']}\n"
    print(result)
    print(next_token)
