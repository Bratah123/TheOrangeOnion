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

from flask import Flask, render_template
import logger

PORT = 4040

app = Flask(__name__)
log = logger.get_logger(__name__)


@app.route("/")
def landing_page():
    is_logged_in = True
    return render_template("index.html", login_status=is_logged_in)


@app.route("/login")
def login_page():
    return render_template("login.html", login_status=False)


@app.route("/logout")
def perform_logout():
    # Session handling logic here
    # Redirect to landing page
    return render_template("index.html", login_status=False)


@app.route("/new-article")
def new_article():
    is_logged_in = True
    return render_template("new-article.html", login_status=is_logged_in)


@app.route("/read/<article_id>")
def article_page(article_id):
    # Replace with dynamic page generating after fetching from DB
    return "Lorem Ipsum!"


if __name__ == '__main__':
    log.info(f"Starting Flask server on port {PORT}")
    app.run(host="0.0.0.0", port=4040, debug=True)
