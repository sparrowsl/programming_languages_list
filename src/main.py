import csv
from typing import Any
import time

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_programming_languages"

html_file = requests.get(URL).text
soup = BeautifulSoup(html_file, "lxml")
parser_output: Any = soup.find("div", class_="mw-parser-output")

with open("./languages.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")

    for language_categories in parser_output.find_all("div", class_="div-col"):
        for category in language_categories.find_all("li"):
            language_link = category.find("a")["href"]
            language_name = category.find("a").text

            language = {
                "name": language_name,
                "link": f"https://en.wikipedia.org{language_link}",
            }

            print(f"Saving {language_name} to csv file")
            time.sleep(0.5)

            csv_writer.writerow([language["name"], language["link"]])
