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
    return render_template("index.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


if __name__ == '__main__':
    log.info(f"Starting Flask server on port {PORT}")
    app.run(host="0.0.0.0", port=4040, debug=True)
