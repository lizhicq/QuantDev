#!/usr/bin/python
# -*- coding: utf-8 -*-

# retrieving_data.py
# Test DB Connection
from __future__ import print_function

import pandas as pd
import MySQLdb as mdb


def get_daily_price(ticker):
    # Connect to the MySQL instance
    db_host = 'localhost'
    db_user = 'sec_user'
    db_pass = 'password'
    db_name = 'securities_master'
    con = mdb.connect(db_host, db_user, db_pass, db_name)

    # Select all of the historic Google adjusted close data
    sql = """SELECT dp.price_date, dp.open_price, dp.close_price
             FROM symbol AS sym
             INNER JOIN daily_price AS dp
             ON dp.symbol_id = sym.id
             WHERE sym.ticker = 'GOOG'
             ORDER BY dp.price_date ASC;"""
    sql = sql.replace('GOOG', ticker)
    # Create a pandas dataframe from the SQL query
    df = pd.read_sql_query(sql, con=con, index_col='price_date')

    return df

if __name__ == "__main__":
    print (get_daily_price('TSLA').tail())