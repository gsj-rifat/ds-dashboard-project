# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies for sql execution
import sqlite3
import pandas as pd


# Create a subclass of QueryBase
# called  `Team`
class Team(QueryBase):
    # Set the class attribute `name`
    # to the string "team"
    name = "team"

    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    def names(self):
        # Query 5: Select team_name and team_id from the team table
        sql_query = """
            SELECT
                team_name,
                team_id
            FROM team
        """
        return self.query(sql_query=sql_query)

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    def username(self, id):
        # Query 6: Select team_name for the team with the specified ID
        sql_query = f"""
        SELECT team_name
            FROM {self.name}
            WHERE team_id = {id}
        """
        return self.query(sql_query=sql_query)

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id):
        query = f"""
                SELECT positive_events, negative_events
                FROM (
                    SELECT
                        employee_id,
                        SUM(positive_events) AS positive_events,
                        SUM(negative_events) AS negative_events
                    FROM {self.name}
                    JOIN employee_events
                    USING ({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                    GROUP BY employee_id
                )
            """
        return self.pandas_query(query)
