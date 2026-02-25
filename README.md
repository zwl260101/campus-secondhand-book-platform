# campus-secondhand-book-platform
基于Python+SQLite开发的轻量级校园二手书交易命令行管理系统，支持书籍发布、关键词检索、书籍下架等核心功能。

## 核心功能
- 书籍发布：校验书名非空、价格大于0，将书籍信息存入SQLite数据库
- 模糊搜索：支持按书名/作者关键词检索在售书籍
- 书籍下架：根据书籍ID修改书籍状态，实现下架功能
- 异常处理：对输入格式、业务规则做基础校验，捕获运行异常

## 运行环境
- Python 3.8+
- SQLite 3（Python内置，无需额外安装）

## 快速运行
1. 克隆仓库到本地
```bash
git clone https://github.com/zwl260101/campus-secondhand-book-platform.git