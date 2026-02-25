import sqlite3

class DBHandler:
    def __init__(self, db_name="campus_books.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """初始化书籍表"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                price REAL,
                seller TEXT,
                status TEXT DEFAULT '在售'
            )
        ''')
        self.conn.commit()

    def add_book(self, title, author, price, seller):
        self.cursor.execute("INSERT INTO books (title, author, price, seller) VALUES (?, ?, ?, ?)",
                            (title, author, price, seller))
        self.conn.commit()

    def query_books(self, keyword=None):
        """实现关键词模糊搜索"""
        if keyword:
            sql = "SELECT * FROM books WHERE (title LIKE ? OR author LIKE ?) AND status='在售'"
            self.cursor.execute(sql, (f'%{keyword}%', f'%{keyword}%'))
        else:
            self.cursor.execute("SELECT * FROM books WHERE status='在售'")
        return self.cursor.fetchall()

    def update_status(self, book_id, status="已下架"):
        self.cursor.execute("UPDATE books SET status = ? WHERE id = ?", (status, book_id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()