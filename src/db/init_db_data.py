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
import bcrypt

def main():
    """
    Fills the database with dummy data, and preset accounts.
    """
    con = sqlite3.connect("orange.db")
    cur = con.cursor()

    # Populate accounts
    username = "admin"
    hashed_password = bcrypt.hashpw("admin".encode("utf-8"), bcrypt.gensalt())
    cur.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, hashed_password))

    # Populate articles
    # (id INTEGER PRIMARY KEY, title TEXT, content TEXT, long_content TEXT, date datetime)
    title = "CSUF Avengers Assemble: Earth's Mightiest Titans Unite to Tackle Parking Pandemonium"
    content = "In a heroic endeavor to address the most dire crisis plaguing California State University, Fullerton (CSUF), a group of exceptional students has come together to form the CSUF Avengers.Their mission? To combat the relentless chaos and confusion that is the campus parking situation."
    long_content = """
Leading the charge is Captain Commute, armed with a map of all the elusive parking spots on campus. 
With unparalleled navigation skills and a keen sense of timing, Captain Commute ensures that no student is left wandering the parking structures in search of a coveted space.

Iron MeterMaid, a civil engineering major, dons a suit made of ticket stubs and wields a mighty citation pad. 
Rumor has it that Iron MeterMaid once calmed a parking rebellion with a single, well-placed ticket, restoring order to the asphalt battleground.

The Hulk Valet, a seemingly ordinary business major, transforms into a powerhouse when faced with parallel parking challenges. 
With a roar that echoes through the parking lots, the Hulk Valet clears the clutter and creates spaces where none seemed possible.

Black Ticketmaster, a mysterious and shadowy finance major, possesses the power to manifest parking permits out of thin air. 
Armed with a clipboard and a stack of permits, Black Ticketmaster ensures that every student has the golden ticket to a stress-free parking experience.
"""

    cur.execute("INSERT INTO articles (title, content, long_content, date) VALUES (?, ?, ?, datetime('now'))", (title, content, long_content))

    cur.close
    con.commit()
    con.close()


if __name__ == '__main__':
    main()