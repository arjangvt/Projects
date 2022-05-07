"""
   Description:  This class contains methods for inserting 
                 sample data into the database 
   Written by:   Arjang Fahim 
   Created:      7/18/2019
   Fixed bugs: 
   Edited by:
   Updates:
"""
# Log will be change to the Logging object
import sys
sys.path.insert(0, '../')


import psycopg2
from Database.DBConn import DBConn

class DBSampleData(object):

    def __init__(self):
        self._dbconn = DBConn()
        self._dbconnstr = self._dbconn.ConnString()

    
    # data has the data dictionary format
    # e.g data["makeid": 1, "modelid":1, "name": "Ferarri" ... ]
    def InsertMake(self, data):
        conn = None

        conn = psycopg2.connect(self._dbconnstr)
        cur = conn.cursor()

        for item in data:
            sql = "INSERT INTO vehicle_makes (id, vehicle_make) VALUES (" 
            sql = sql + "'" + str(item["id"]) + "','" +  str(item["vehicle_makes"])  +"')"

            cur.execute(sql)
            conn.commit()

        cur.close()
        conn.close()

        return ""

    def InsertModel(self, data):
        conn = None

        conn = psycopg2.connect(self._dbconnstr)
        cur = conn.cursor()

        for item in data:

            sql = "INSERT INTO vehicle_models (id, vehicle_make_id, model) VALUES ('" 
            sql = sql + str(item["id"]) + "','" +  str(item["vehicle_make_id"]) + "','"  
            sql = sql + str(item["model"]) + "')"
            #print(sql)
            cur.execute(sql)
            conn.commit()

        cur.close()
        conn.close()

        return ""

    def InsertTrim(self, data):
        conn = None

        conn = psycopg2.connect(self._dbconnstr)
        cur = conn.cursor()

        for item in data:

            sql = "INSERT INTO vehicle_trims (id, vehicle_model_id, trim) VALUES ('" 
            sql = sql + str(item["id"]) + "','" +  str(item["vehicle_model_id"]) + "','"  
            sql = sql + str(item["trim"]) + "')"
            #print(sql)
            cur.execute(sql)
            conn.commit()

        cur.close()
        conn.close()

        return ""