## 目录结构
```angular2html
x-Toolkit/
├── x_toolkit/                  # 主代码目录
│   ├── __init__.py
│   ├── api_client.py              # API 客户端封装
│   ├── config.py                  # 配置管理
│   ├── operations/                # 功能模块
│   │   ├── __init__.py
│   │   ├── delete_tweet.py        # 删除推文功能
│   │   ├── post_tweet.py          # 发布推文功能
│   │   ├── fetch_tweets.py        # 获取推文功能
│   │   └── ...                    # 其他功能
│   ├── utils/                     # 工具模块
│   │   ├── __init__.py
│   │   ├── logger.py              # 日志工具
│   │   ├── error_handler.py       # 错误处理
│   │   ├── utils.py               # 通用函数
│   │   └── ...                    # 其他工具
│   └── cli.py                     # 命令行接口
├── tests/                         # 测试目录
│   ├── __init__.py
│   ├── test_api_client.py         # API 客户端测试
│   ├── test_delete_tweet.py       # 删除推文功能测试
│   └── ...                        # 其他测试
├── .env                           # 环境变量文件
├── .gitignore                     # Git 忽略文件
├── requirements.txt               # 依赖文件
├── README.md                      # 项目说明
└── setup.py                       # 项目安装脚本
```