import os
from pathlib import Path
import platform
import subprocess
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import pandas as pd


class scraper():
    """
    A class to create a scraper for html pages and extraction of relevant
    data. Relies on Chrome for webscraping please insure that the chromedriver
     is installed locally.
    """

    def __init__(self, chrome_drive_path):
        self.chrome_drive_path = chrome_drive_path
        self.base_url = None
        self.save_dir = None
        self.scrape_list = []
        self.driver = None

    def create_session(self, base_url, save_dir):
        try:
            self.base_dir = Path(save_dir)
        except OSError as error:
            print(error)
        assert_error = "is not accessable, please check url spelling and \
                        internet connection."
        assert self._ping(base_url) is True, f"{base_url} {assert_error}"
        self.base_url = base_url
        self._initialize_selenium()

    def add_scrape_list(self, json_file, sub_domain_element):
        try:
            with open(json_file) as jf:
                pages_data = json.load(jf)
            self.scrape_list = pages_data[sub_domain_element]
        except IOError as error:
            print(error)

    def _ping(self, url):
        """
        Checks that the provide base url is live.

        Parameters
        ----------
        url : string
            Base url to be scraped.
        """
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', url]
        output = subprocess.call(command, stdout=subprocess.DEVNULL) == 0
        return output

    def _initialize_selenium(self):
        """
        Initializes the selenium driver for scraping through Chrome.
        """
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        self.driver = webdriver.Chrome(options=options, /
                                    executable_path=self.chrome_drive_path)
