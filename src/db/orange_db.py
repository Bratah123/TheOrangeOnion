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
from db.article import Article

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

    def get_articles_by_page(self, page_num) -> list[Article]:
        """
        Returns a list of articles on a given page.
        Page 1 is the first 10 entries, page 2 is the next 10, etc.
        """
        cur = self.con.cursor()
        cur.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 10 OFFSET ?", (page_num * 10,))
        articles = cur.fetchall()
        cur.close()

        article_objects = []

        for article in articles:
            article_objects.append(Article(article[1], article[2], article[3], article[4]))

        return article_objects
    
    def get_article_by_id(self, article_id) -> Article:
        cur = self.con.cursor()
        cur.execute("SELECT * FROM articles WHERE id=?", (article_id,))
        article = cur.fetchone()
        cur.close()

        return Article(article[1], article[2], article[3], article[4])

