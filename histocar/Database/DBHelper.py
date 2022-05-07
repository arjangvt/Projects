"""
   Description:  This class contains methods for database operations
   Written by:   Arjang Fahim 
   Created:      7/14/2019
   Fixed bugs: 
   Edited by:
   Updates:
"""
import psycopg2
from Database.DBConn import DBConn

class DBHelper(object):

    
    def __init__(self):
        self._dbconn = DBConn()
        self._dbconnstr = self._dbconn.ConnString()


    def GetMinMaxProductYear(self, makeid, modelid, zip):
        fields = []

        sql = "select MIN(production_year), MAX(production_year) from histocar_lists "
        sql = sql + "where vehicle_model_id = " + modelid + " and "
        sql = sql + "vehicle_make_id = " + makeid + " and "
        sql = sql + "zipcode_id = " + zip


        conn = psycopg2.connect(self._dbconnstr)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            temp = {}
            count = 0
            for col in cur.description:
                temp.update({str(col[0]): row[count]})
                count = count + 1
            fields.append(temp)
 
        return fields

        conn = psycopg2.connect(self._dbconnstr)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            temp = {}
            count = 0
            for col in cur.description:
                temp.update({str(col[0]): row[count]})
                count = count + 1
            fields.append(temp)
 
        return fields


    """
       This method returns min and max price for a given car model
       make and zip code. 
       It needs to be improved if either of parameter not presented 
    """
    def GetMinMaxCarPrice(self, makeid, modelid, zip):

        fields = []

        sql = "select MIN(price), MAX(price) from histocar_lists "
        sql = sql + "where vehicle_model_id = " + modelid + " and "
        sql = sql + "vehicle_make_id = " + makeid + " and "
        sql = sql + "zipcode_id = " + zip

        conn = psycopg2.connect(self._dbconnstr)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            temp = {}
            count = 0
            for col in cur.description:
                temp.update({str(col[0]): row[count]})
                count = count + 1
            fields.append(temp)
 
        return fields

    def InsertRecentSearches(self, carlist_id):
    
        try:
            sql = "INSERT INTO recent_search (carlist_id) VALUES (" + str(carlist_id) + ")"
            try:
                conn = psycopg2.connect(self._dbconnstr)
                cur = conn.cursor()
                cur.execute(sql)
            except (psycopg2.Error) as err:
                print ("Error ", err)

            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
        	print(error)
        finally:
            if conn is not None:
                conn.close()

        return ""
