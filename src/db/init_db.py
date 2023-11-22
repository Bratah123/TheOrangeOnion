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

def main():
    con = sqlite3.connect("orange.db")
    cur = con.cursor()

    # content is the short description of the article you see in the main page
    # long_content is the full article when you click on an article
    cur.execute("CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, title TEXT, content TEXT, long_content TEXT, date TEXT)")
    # All accounts in the account section are considered admins
    cur.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

    # Clean up
    con.commit()
    cur.close()
    con.close()

if __name__ == "__main__":
    main()