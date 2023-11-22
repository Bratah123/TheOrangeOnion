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

