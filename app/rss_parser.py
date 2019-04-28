# -*- coding: utf-8 -*-

import feedparser
import csv
import time
import pandas as pd

from typing import Dict, List, Iterable
from .boTool import boTool
from datetime import datetime


class RssParser:
    def __init__(self):
        self.rss_file = "./rss_index.csv"

    def parse(self, keys: str, tag: str = "", date: str = None) -> List[str]:
        cleanTool = boTool()

        if date is not None:
            str_rss = f"https://news.google.com/rss/search?q={keys},{date}&hl=en-US&gl=US&ceid=US:en"
        else:
            str_rss = f"https://news.google.com/rss/search?q={keys}&hl=en-US&gl=US&ceid=US:en"

        print(str_rss)

        RssFeed = feedparser.parse(str_rss)
        rss_df = pd.DataFrame.from_dict(RssFeed.entries)

        try:
            return (
                rss_df.assign(tag=tag)
                .assign(summary=rss_df["summary"].apply(cleanTool.clearTag))
                .filter(["title", "summary", "published", "tag"])
            )
        except Exception as e:
            return None

    def read_csv(self, addr: str = None) -> Iterable[List[str]]:
        if addr is None:
            addr = self.rss_file

        with open(addr, mode="r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="^")
            next(csv_reader, None)

            for row in csv_reader:
                yield row

    def save_as_csv(self, pd_result, tag: str, date: str = None) -> None:
        if date is not None:
            today = date
        else:
            today = datetime.now().strftime("%Y-%m-%d")

        pd_result.to_csv(f"./csv/{tag}/{today}_{tag}.csv", sep="^", index=False)

        return None

    def start_parse(self, date: str = None) -> None:
        for row in self.read_csv():
            parsed_result = self.parse(tag=row[0], keys=row[1], date=date)

            if parsed_result is not None:
                self.save_as_csv(parsed_result, tag=row[0], date=date)

        return None
