from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#db_path = Path('/path/python-package/employee_events/employee_events.db').resolve()
#db_path = Path(__file__).parent / "employee_events.db"
db_path = Path(__file__).parent.absolute() / "employee_events.db"
#print(db_path)  # This will print the absolute path to the console


# Define a class called `QueryMixin`
class QueryMixin:
    #db_path = Path('/path/python-package/employee_events/employee_events.db').resolve()
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    def pandas_query(self, sql_query: str) -> pd.DataFrame:
        with connect(db_path) as conn:
            return pd.read_sql_query(sql_query, conn)

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    def query(self, sql_query: str) -> list:
        with connect(db_path) as conn:
            cursor = conn.cursor()
            return cursor.execute(sql_query).fetchall()
    

def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query
