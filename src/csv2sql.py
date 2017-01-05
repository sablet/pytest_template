import sqlite3
import csv
from src.helper import csv_header2dict


class ToSqlite3:
    def __init__(self, db_name="tests/data/sample.sqlite3", table_name="my_table"):
        self.connect = sqlite3.connect(db_name)
        self.db_obj = self.connect.cursor()
        self.table_name = table_name

    def text2sqlite(self, csv_obj):
        """
        :param csv_obj: obj
        :rtype: None
        """
        header, *values = csv.reader(csv_obj)
        create_s = "CREATE TABLE " + self.table_name + "(" + ', '.join(header) + ")"
        self.db_obj.execute(create_s)
        for value_arr in values:
            self.db_obj.execute(
                "INSERT INTO " +
                self.table_name +
                " values (" +
                ", ".join('?'*len(header)) +
                ")",
                tuple(value_arr)
            )
        self.connect.commit()

    def select_all(self):
        """
        :return: all SQL elemnet
        :rtype str
        """
        select_s = "SELECT * FROM " + self.table_name
        self.db_obj.execute(select_s)
        return self.db_obj.fetchall()