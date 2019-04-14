# -*- coding: utf-8 -*-

import feedparser
import csv
import pandas as pd
from typing import Dict, List

from boTool import boTool
from datetime import datetime


class RssParser:
    def __init__(self, rss_file:str):
        if rss_file is not None:
            self.rss_file = rss_file
        else:
            self.rss_file = "./rss_index.csv"


    def clean_rss(self, desc=True, *args:List[str]) -> List[str]:
        cleanTool = boTool()
        str_search = ",%20".join(*args)
        RssFeed = feedparser.parse(
            f"https://news.google.com/rss/search?q={str_search}&hl=en-US&gl=US&ceid=US:en"
        )

        if desc is True:
            descriptions = [
                cleanTool.clearTag_old(x.description) for x in RssFeed.entries
            ]
            return descriptions

        titles = [x.title for x in RssFeed.entries]
        return titles

    def read_csv(self) -> Dict[str, str]:
        return {"key": "", "value": ""}

    def parse(self) -> pd.DataFrame:
        return

    def save_as_csv(self) -> None:
        return None

