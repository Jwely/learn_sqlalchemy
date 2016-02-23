from odo import odo
import os
from sqlalchemy.engine.url import URL


def csv_to_db(csv_path, db_path, table_name=None, **db_kwargs):
    """

    :param csv_path:
    :param db_path:
    :param table_name:
    :param db_kwargs:
    :return:
    """

    if os.path.exists(csv_path):
        csv_path = os.path.abspath(csv_path)
    else:
        raise IOError("file '{0}' does not exist".format(csv_path))

    # if no table name is supplied, use the basename of the file without extension
    if table_name is None:
        table_name = ".".join(os.path.basename(csv_path).split(".")[0:-1])

    url = URL(database=db_path, **db_kwargs)
    table_url = "{url}::{tbl}".format(url=url, tbl=table_name)
    odo(csv_path, table_url)



if __name__ == "__main__":

    csv = '../dat/scy_dat.csv'
    db = '../dat/scy_dat.db'
    csv_to_db(csv, db, drivername='sqlite')
