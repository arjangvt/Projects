"""
   Description:  This class contains database operations methods
                 for restful APIs
   Written by:   Arjang Fahim 
   Created:      04/09/2019
   Fixed bugs: 
   Edited by:
   Updates:
"""

import psycopg2
from Database.DBConn import DBConn
from Database.DBHelper import DBHelper
from flask import jsonify

class DBHelperRestAPI(object):
    def __init__(self):
        self._dbconn = DBConn()
        self._dbconnstr = self._dbconn.ConnString()
        self._dbhelper = DBHelper()

    def FetchCarBodyType(self):
        fields = []

        sql = "select * from vehicle_bodystyle"
        
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


    def FetchCarDetail(self, carid):
        fields = []

        sql = "select * from histocar_lists where id = '" + carid + "'"
        
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


    def FetchCarTrim(self, modelid):
        fields = []

        sql = "select id, trim from vehicle_trims where vehicle_model_id =" + modelid
                
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


    def FetchRecentSearches(self):
        fields = []

        sql = "select A.veh_description, B.vehicle_make, A.price, C.color, "
        sql = sql + "A.mileage, D.model, A.vin_number, A.image_url, A.vehicle_url,A.id from " 
        sql = sql + "histocar_lists as A, vehicle_makes as B, colors as C, "
        sql = sql + "vehicle_models as D where "
        sql = sql + "A.vehicle_model_id = D.id and "
        sql = sql + "A.vehicle_make_id = B.id  and "
        sql = sql + "A.color_id = C.id and A.id in "
        sql = sql + "(select carlist_id from recent_search order by created_at desc limit 6)"
        
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

    def FetchMinMaxProductYear(self, makeid, modelid, zipcode):
        fields = []
        fields = self._dbhelper.GetMinMaxProductYear(makeid, modelid, zipcode)
        return fields
    
    def FetchMinMaxPrice(self, makeid, modelid, zipcode):
        fields = []
        fields = self._dbhelper.GetMinMaxCarPrice(makeid, modelid, zipcode)
        return fields     

    def FetchModelsMake(self, makeid):
        fields = []
        sql = "select model, id, vehicle_make_id from vehicle_models where is_active = true "
        sql = sql +  "and vehicle_make_id = '" + makeid + "' order by model"
     
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


    def FetchAllCarMakes(self):

        fields = []
        sql = "select vehicle_make, id from vehicle_makes where is_active = true order by vehicle_make"
     
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
    

    def FetchAllCarLists(self):

        fields = []
        sql = "select * from histocar_lists where is_active = true"
     
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


    def FetchCarsMakeModelZip(self, makeid, modelid, zipcode):

        #makeid = 0
        #modelid = 0
        zipid = 0
        fields = []
        conn = psycopg2.connect(self._dbconnstr)

        #print(makeid)
        sql_zip =  "select * from zipcodes where zipcode = '" + zipcode + "' and is_active = true"
        cur = conn.cursor()
        cur.execute(sql_zip)
        if (cur.rowcount != 0 ):
            rows = cur.fetchall()
            zipid = rows[0][0]
 
        sql_car = "select  B.vehicle_make, A.price, C.color, "
        sql_car = sql_car + "A.mileage, D.model, A.vin_number, A.image_url, A.vehicle_url,A.id, A.veh_description, A.created_at from " 
        sql_car = sql_car + "histocar_lists as A, vehicle_makes as B, colors as C, "
        sql_car = sql_car + "vehicle_models as D where "
        sql_car = sql_car + "A.vehicle_model_id = '" + str(modelid) + "' and "
        sql_car = sql_car + "A.vehicle_make_id = '" + str(makeid) + "' and "
        sql_car = sql_car + "A.zipcode_id = '" + str(zipid) + "' "
        sql_car = sql_car + "and  A.vehicle_make_id = B.id "
        sql_car = sql_car + "and  A.color_id = C.id "
        sql_car = sql_car + "and  A.vehicle_model_id = D.id "
        sql_car = sql_car + "limit 40"

        #print(sql_car)
        cur = conn.cursor()
        cur.execute(sql_car)
        rows = cur.fetchall()
        recent_search_id = 0
        count = 0
        for row in rows:
            temp = {}
            if (count == 0):
                recent_search_id = row[8]
            count = 0
             
            for col in cur.description:
                temp.update({str(col[0]): row[count]})
                count = count + 1
            fields.append(temp)

        
        #print ("My Recent")
        #print (recent_search_id)

        self._dbhelper.InsertRecentSearches(recent_search_id)
        return fields