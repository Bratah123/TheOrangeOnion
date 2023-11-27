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
from functools import partial
from typing import Callable, Optional

from flask import redirect, url_for, session
from werkzeug.datastructures.structures import ImmutableMultiDict

from util import logger

log = logger.get_logger(__name__)


def article_creation(form: ImmutableMultiDict) -> Optional[Callable]:
    if form["form_type"] == "new_article":
        user = session['user']
        log.info(f"User {user[0]}, is attempting to create a new article...")

        title = form['title']
        content = form['title']
        long_content = form['title']
        log.info(f"Article title: {title}, content: {content}, long_content: {long_content}")
        return partial(redirect, location=url_for("landing_page", login_status=False))
    return
