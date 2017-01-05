import pytest
from src.csv2sql import ToSqlite3
import os
sample_in = "tests/data/sample.csv"
# sample_in = "tests/data/KEN_ALL_ROME_utf8.CSV"
sample_out = "tests/data/sample.sqlite3"


@pytest.fixture(autouse=True)
def db_initialize():
    print("\n\ninitialize table\n")
    if os.path.exists(sample_out):
        os.remove(sample_out)


def test_text2sqlite():
    db_obj = ToSqlite3(sample_out)
    with open(sample_in) as csv_f:
        db_obj.text2sqlite(csv_f)
    ret = db_obj.select_all()
    if sample_in == "tests/data/sample.csv":
        assert ret == [('2', '3', '5'), ('1', '3', '5')]