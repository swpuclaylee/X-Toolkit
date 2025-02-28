import click

from x_toolkit.operations.fetch_tweets import fetch_tweets as ft
from x_toolkit.utils.utils import get_user_id


@click.group()
def cli():
    """
    X Toolkit 命令行工具
    :return:
    """
    pass


@click.command()
@click.argument("user_name")
@click.option("--max-results", default=10, help="最大返回的推文数量（默认 10 条）")
@click.option("--pagination-token", help="分页令牌")
@click.option("--exclude-replies", is_flag=True, help="排除回复")
@click.option("--exclude-retweets", is_flag=True, help="排除转发")
@click.option("--output", type=click.Path(), help="输出文件路径")
def fetch_tweets(user_name, max_results, pagination_token, exclude_replies, exclude_retweets, output):
    """
    获取指定用户的推文。

    :param user_name: 用户名称
    :param max_results: 最大返回的推文数量（默认 10 条）
    :param pagination_token: 分页token
    :param exclude_replies: 是否排除回复
    :param exclude_retweets: 是否排除转发
    :param output: 输出文件路径
    :return: 推文列表和分页令牌
    """
    try:
        # user_id = get_user_id(user_name)
        user_id = 1520843497464791040
        click.echo(max_results)
        # 调用 fetch_tweets 功能
        tweets, next_token = ft(
            user_id, max_results, pagination_token=pagination_token, exclude_replies=exclude_replies,
            exclude_retweets=exclude_retweets
        )

        # 打印结果
        result = f"Fetched {len(tweets)} tweets for user {user_id}: \n"
        for tweet in tweets:
            result += f"- {tweet['text']}\n"
        if next_token:
            result += f"Next token: {next_token}\n"

        # 输出到文件或终端
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(result)
            click.echo(f"Results written to {output}")
        else:
            click.echo(result)
    except Exception as e:
        click.echo(f"Error fetching tweets: {e}")


# 注册命令
cli.add_command(fetch_tweets, name="fetch-tweets")  # 使用短横线命名命令

if __name__ == "__main__":
    cli()
