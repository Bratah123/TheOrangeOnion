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
from form_management.article_creation import article_creation

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

    # Checking if user is logged in, in our case, only admins can be logged in
    login_status = True if "user" in session else False
    recent_articles = []

    with OrangeDB() as db:
        recent_articles = db.get_articles_by_page(0)

    return render_template("index.html", login_status=login_status, articles=recent_articles)


@app.route("/search/<search_field_input>", methods=("GET", "POST"))
def search_page(search_field_input: str):
    if request.method == "POST":
        action = search_form(request.form)
        if action:
            return action()

    login_status = True if "user" in session else False

    return render_template("search.html", login_status=login_status, search_field_input=search_field_input)


@app.route("/login", methods=("GET", "POST"))
def login_page():
    if request.method == "POST":
        action = login_form(request.form)
        if action:
            return action()
        action = search_form(request.form)
        if action:
            return action()

    if "user" in session:
        return redirect(url_for("landing_page"))
    else:
        login_status = False

    return render_template("login.html", login_status=login_status, invalid=request.args.get("invalid", default=False))


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
        action = article_creation(request.form)
        if action:
            return action()

    if "user" in session:
        is_logged_in = True
    else:
        log.info("User is not logged in, redirecting to login page...")
        return redirect(url_for("login_page"))
        
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

    login_status = True if "user" in session else False

    return render_template(
        "article.html",
        article=article,
        formatted_body=article.long_content.split("\r\n"),
        login_status=login_status,
    )


@app.errorhandler(404)
def not_found(error):
    log.debug(f"Invalid page access:\n\t\t%s", error)

    login_status = True if "user" in session else False

    return render_template("404.html", login_status=login_status)


if __name__ == '__main__':
    log.info(f"Starting Flask server on port {PORT}")
    app.run(host="0.0.0.0", port=4040, debug=True)
