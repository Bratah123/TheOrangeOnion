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
from flask import Flask, redirect, render_template, request, url_for, session

from db.orange_db import OrangeDB
from util import logger
from form_management.login import login_form
from form_management.search import search_form

PORT = 4040

app = Flask(__name__)
app.secret_key = "super duper secret key that no one can guess"
log = logger.get_logger(__name__)


@app.route("/", methods=("GET", "POST"))
def landing_page():
    if request.method == "POST":
        action = search_form(request.form)
        if action:
            return action()

    is_logged_in = False
    recent_articles = []

    with OrangeDB() as db:
        recent_articles = db.get_articles_by_page(0)

    # Checking if user is logged in, in our case, only admins can be logged in
    if "user" in session:
        is_logged_in = True

    return render_template("index.html", login_status=is_logged_in, articles=recent_articles)


@app.route("/search/<search_field_input>", methods=("GET", "POST"))
def search_page(search_field_input: str):
    if request.method == "POST":
        action = search_form(request.form)
        if action:
            return action()

    return render_template("search.html", search_field_input=search_field_input)


@app.route("/login", methods=("GET", "POST"))
def login_page():
    if request.method == "POST":
        action = login_form(request.form)
        if action:
            return action()
        action = search_form(request.form)
        if action:
            return action()
        
    is_logged_in = False

    # Checking if user is logged in, in our case, only admins can be logged in
    if "user" in session:
        is_logged_in = True

    return render_template("login.html", login_status=is_logged_in)


@app.route("/logout")
def perform_logout():
    # Session handling logic here
    # Redirect to landing page

    if "user" in session:
        session.pop("user")

    return redirect(url_for("landing_page"))


@app.route("/new_article", methods=("GET", "POST"))
def new_article():
    if request.method == "POST":
        action = search_form(request.form)
        if action:
            return action()

    is_logged_in = False

    if "user" in session:
        is_logged_in = True
        
    return render_template("new_article.html", login_status=is_logged_in)


@app.route("/read/<article_id>", methods=("GET", "POST"))
def article_page(article_id):
    if request.method == "POST":
        action = search_form(request.form)
        if action:
            return action()
    article = None
    # Replace with dynamic page generating after fetching from DB
    with OrangeDB() as db:
        article = db.get_article_by_id(article_id)

    login_status = False

    if "user" in session:
        login_status = True

    return render_template("article.html", article=article, login_status=login_status)


if __name__ == '__main__':
    log.info(f"Starting Flask server on port {PORT}")
    app.run(host="0.0.0.0", port=4040, debug=True)
