import sqlite3
from helper import header2dict
import csv


class ToSqlite3:
    def __init__(self, db_name="sample.sqlite3"):
        self.db_obj = sqlite3.connect(db_name).cursor()
        self.key_dict = {}

    def text2sqlite(self, input_name, table_name="table"):
        with open(input_name) as csvfile:
            reader = csv.DictReader(csvfile)
            

