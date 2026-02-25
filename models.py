class Book:
    def __init__(self, book_id, title, author, price, seller, status="在售"):
        self.id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.seller = seller
        self.status = status

    def __str__(self):
        return f"ID:{self.id} | 《{self.title}》 | 作者:{self.author} | 价格:{self.price}元 | 卖家:{self.seller}"

class BookManager:
    def __init__(self, db):
        self.db = db

    def post_book(self, title, author, price, seller):
        """发布书籍，包含基础校验"""
        if not title or price <= 0:
            raise ValueError("书名不能为空且价格必须大于0")
        self.db.add_book(title, author, price, seller)

    def search_books(self, keyword=None):
        data = self.db.query_books(keyword)
        return [Book(*item) for item in data]