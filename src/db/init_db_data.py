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
import json

def main():
    """
    Fills the database with dummy data, and preset accounts.
    """
    con = sqlite3.connect("orange.db")
    cur = con.cursor()

    # Populate accounts
    username = "admin"
    hashed_password = bcrypt.hashpw("admin".encode("utf-8"), bcrypt.gensalt())
    cur.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, hashed_password))

    # Populate articles from articles_metadata.json
    # (id INTEGER PRIMARY KEY, title TEXT, content TEXT, long_content TEXT, date datetime)
    file_path = "src/db/articles_metadata.json"
    with open(file_path, "r") as f:
        articles_metadata = json.load(f)
        # Mass Insert all articles
        cur.executemany("INSERT INTO articles (title, content, long_content, date) VALUES (:title, :content, :long_content, datetime('now'))", articles_metadata)

    cur.close
    con.commit()
    con.close()


if __name__ == '__main__':
    main()