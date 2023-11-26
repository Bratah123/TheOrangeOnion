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
import bcrypt

from db.orange_db import OrangeDB
from functools import partial
from typing import Callable, Optional

from flask import redirect, url_for, session
from werkzeug.datastructures.structures import ImmutableMultiDict

from util import logger

log = logger.get_logger(__name__)


def login_form(form: ImmutableMultiDict) -> Optional[Callable]:
    if form["form_type"] == "login":
        username = form["username"]
        password = form["password"]
        log.debug(f"User `{username}` has attempted to logged in.")

        # fetch data from database
        with OrangeDB() as db:
            user = db.get_user(username)

            if not user:
                log.debug(f"User `{username}` does not exist.")
                return partial(redirect, location=url_for("login_page"))
            
            password_from_db = user[2]

            if bcrypt.checkpw(password.encode("utf-8"), password_from_db):
                log.debug(f"User `{username}` has successfully logged in.")
                session['user'] = user
                return partial(redirect, location=url_for("landing_page"))
            else:
                log.debug(f"User `{username}` has failed to logged in.")
                return partial(redirect, location=url_for("login_page"))
    return
