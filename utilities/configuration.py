import configparser
import os
from pathlib import Path
import mysql.connector
from mysql.connector import Error


def getConfig():
    # path = Path(__file__)
    # print(path)
    # ROOT_DIR = path.parent.absolute()
    config = configparser.ConfigParser()
    config.read('C:/Users/Umesh_Kumar/PycharmProjects/pythonProject/BakEndAutomation/utilities/properties.ini')
    return config


connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database']
}


def get_connection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successfully")
            return conn
    except Error as e:
        print(e)
    # giving 2 stars to tell whaterver argument we have that is dictionary


def get_query(query):
    con = get_connection()
    cur = con.cursor(buffered=True)
    cur.execute(query)
    row = cur.fetchone()
    cur.close()
    print(row)
    return row


get_query('select * from Books')

