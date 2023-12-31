# Copyright 2023 Brandon Nguyen, Tung Nguyen, Garret Feng
#
# This file is part of CSUFTheOnion.
# CSUFTheOnion is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CSUFTheOnion is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CSUFTheOnion. If not, see <https://www.gnu.org/licenses/>.
import sqlite3
import bcrypt
from db.article import Article, ARTICLE_CONTENT_WORD_LIMIT

DATABASE_NAME = "orange.db"


class OrangeDB:
    def __init__(self):
        self.articles = []
        self.con = None

    def __enter__(self):
        self.con = sqlite3.connect(DATABASE_NAME)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()

    def get_articles_by_page(self, page_num) -> tuple[list[Article], int]:
        """
        Returns a list of articles on a given page.
        Page 1 is the first 10 entries, page 2 is the next 10, etc.
        """
        cur = self.con.cursor()
        cur.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 10 OFFSET ?;", ((page_num-1) * 10,))
        articles = cur.fetchall()
        cur.execute("SELECT COUNT(title) FROM articles;")
        count = (cur.fetchone()[0] - 1) // 10 + 1
        cur.close()

        article_objects = []

        for article_data in articles:
            article = Article(article_data[1], article_data[2], article_data[3], article_data[4])
            article.uuid = article_data[0]

            article_objects.append(article)

        return article_objects, count
    
    def get_article_by_id(self, article_id) -> Article:
        cur = self.con.cursor()
        cur.execute("SELECT * FROM articles WHERE id=?", (article_id,))
        article_data = cur.fetchone()
        cur.close()
        
        article = Article(article_data[1], article_data[2], article_data[3], article_data[4])
        article.uuid = article_data[0]

        return article

    def save_article(self, article: Article):
        cur = self.con.cursor()

        # Check for article word limit
        if len(article.content.split()) > ARTICLE_CONTENT_WORD_LIMIT:
            raise ValueError(f"Article content exceeds {ARTICLE_CONTENT_WORD_LIMIT} words!")
        
        # Check for duplicate titles
        cur.execute("SELECT * FROM articles WHERE title=?", (article.title,))
        if cur.fetchone():
            raise ValueError(f"Article with title '{article.title}' already exists!")
        
        cur.execute("INSERT INTO articles (title, content, long_content, date) VALUES (?, ?, ?, datetime('now'))", (article.title, article.content, article.long_content))
        self.con.commit()
        cur.close()

    def query_for_article_by_inclusive_title(self, title: str) -> list[Article]:
        cur = self.con.cursor()
        cur.execute("SELECT * FROM articles WHERE title LIKE ?", (f"%{title}%",))
        articles_data = cur.fetchall()
        cur.close()
        
        articles = []

        for article_data in articles_data:
            article = Article(article_data[1], article_data[2], article_data[3], article_data[4])
            article.uuid = article_data[0]
            articles.append(article)

        return articles
    
    def register_user(self, username: str, password: str):
        """
        Registers a user with the given username and password.
        Hashes the password before storing it.
        """
        cur = self.con.cursor()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        cur.execute("SELECT * FROM users WHERE username=?", (username,))

        if cur.fetchone():
            raise ValueError(f"User with username '{username}' already exists!")
        
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        self.con.commit()
        cur.close()

    def get_user(self, username: str) -> tuple[str, str]:
        """
        Returns the username and hashed password of the user with the given username.
        """
        cur = self.con.cursor()
        cur.execute("SELECT * FROM accounts WHERE username=?", (username,))
        user = cur.fetchone()
        cur.close()

        return user