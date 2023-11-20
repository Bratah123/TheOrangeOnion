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


class Article:
    def __init__(self, title: str, content: str, date: str = None):
        self.title = title
        self.content = content

        if not date:
            timestamp = datetime.datetime.now(tz=ZoneInfo("US/Pacific"))
            self.date = timestamp.strftime("%d %b %Y, %I:%M%p")  # format: 31 Jan 2022, 11:59PM
        else:
            self.date = date

    def __repr__(self):
        return f"Article with title: '{self.title}'; submitted on {self.date}"


def get_dummy_articles():
    return [
        Article(
            "Invading Oranges Now Primary Threat",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "15 Dec 2021, 12:51PM",
        ),
        Article(
            "Batman Returns! All Hope Not Lost?",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "13 Dec 2021, 12:21PM",
        ),
        Article(
            "Alien Foodstuff Terrorizing Orange County",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "12 Dec 2021, 11:21AM",
        ),
        Article(
            "Has Batman Forsaken Orange County?",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "11 Dec 2021, 11:31AM",
        ),
    ]
