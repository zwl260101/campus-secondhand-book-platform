from db_handler import DBHandler
from models import BookManager


def main():
    db = DBHandler()
    manager = BookManager(db)

    print("=== 欢迎使用校园二手书交易系统 ===")

    while True:
        print("\n1. 发布书籍 | 2. 浏览/搜索书籍 | 3. 下架书籍 | 4. 退出")
        choice = input("请选择操作: ")

        try:
            if choice == '1':
                title = input("书名: ")
                author = input("作者: ")
                price = float(input("价格: "))
                seller = input("您的姓名: ")
                manager.post_book(title, author, price, seller)
                print("发布成功！")

            elif choice == '2':
                kw = input("输入搜索关键词(回车查看全部): ")
                books = manager.search_books(kw)
                if not books:
                    print("未找到相关书籍。")
                for b in books:
                    print(b)

            elif choice == '3':
                bid = int(input("请输入要下架的书籍ID: "))
                db.update_status(bid)
                print(f"书籍ID {bid} 已成功下架。")

            elif choice == '4':
                print("谢谢使用，再见！")
                break
            else:
                print("无效输入，请重试。")

        except ValueError as e:
            print(f"输入错误: {e}")
        except Exception as e:
            print(f"系统运行异常: {e}")


if __name__ == "__main__":
    main()