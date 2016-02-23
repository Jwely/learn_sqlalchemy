from odo import odo
import os
from sqlalchemy.engine.url import URL


def csv_to_db(csv_path, db_path, table_name=None, **db_kwargs):
    """
    Creates a simple database from a csv file with default sqlite driver.

    :param csv_path:    filepath to csv
    :param db_path:     desired filepath to destination database
    :param table_name:  manual table_name to dump csv into, if None the table will
                        inherit the same name as the csv file without extension
    :param db_kwargs:   kwargs according to db adress as in `sqlalchemy.engine.url.URL`
    :return:            database connection?
    """

    if os.path.exists(csv_path):
        csv_path = os.path.abspath(csv_path)
    else:
        raise IOError("file '{0}' does not exist".format(csv_path))

    # if no table name is supplied, use the basename of the file without extension
    if table_name is None:
        table_name = ".".join(os.path.basename(csv_path).split(".")[0:-1])

    # if no driver was included in kwargs, use sqlite
    if 'drivername' not in db_kwargs:
        db_kwargs['drivername'] = 'sqlite'

    url = URL(database=db_path, **db_kwargs)
    table_url = "{url}::{tbl}".format(url=url, tbl=table_name)
    return odo(csv_path, table_url)



if __name__ == "__main__":

    csv = 'dat/scy_dat.csv'
    db = 'dat/scy_dat.db'
    print csv_to_db(csv, db)
