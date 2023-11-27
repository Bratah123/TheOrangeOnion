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
import datetime
from zoneinfo import ZoneInfo

ARTICLE_CONTENT_WORD_LIMIT = 100

class Article:
    def __init__(self, title: str, content: str, long_content: str, date: str = ""):
        self.uuid = -1
        self.title = title
        self.content = content
        self.long_content = long_content
        self.date = date


    def __repr__(self):
        return f"Article with title: '{self.title}'; submitted on {self.date}"
