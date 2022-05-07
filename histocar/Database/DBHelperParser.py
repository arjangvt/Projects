"""
   Description:  This class contains methods for database operations
   Written by:   Arjang Fahim 
   Created:      10/24/2018
   Fixed bugs: 
   Edited by:
   Updates:
"""
import psycopg2
from Database.DBConn import DBConn

class DBHelperParser(object):

    
    def __init__(self):
        self._dbconn = DBConn()
        self._dbconnstr = self._dbconn.ConnString()



    def FindZipcodeByID(self, zipID):

        sql = "select zipcode from zipcodes where id = '" + zipID + "'"

        try:
            conn = psycopg2.connect(self._dbconnstr)
            cur = conn.cursor()
            cur.execute(sql)

            row = cur.fetchone()
            #print (row)
            #while row is not None:
            #    row = cur.fetchone()

            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return row


    def FindCarBodyTypeID(self, bodytype):

        sql = "select id from vehicle_bodystyle where body_style = '" + bodytype + "'"

        try:
            conn = psycopg2.connect(self._dbconnstr)
            cur = conn.cursor()
            cur.execute(sql)

            row = cur.fetchone()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return row
    
    def FindColorID(self, color):

        sql = "select id from colors where color = '" + color + "'"

        try:
            conn = psycopg2.connect(self._dbconnstr)
            cur = conn.cursor()
            cur.execute(sql)

            row = cur.fetchone()
            #print (row)
            #while row is not None:
            #    row = cur.fetchone()

            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
 
        return row


    def FindCurrencyID(self, currency):

        sql = "select id from currencies where currency = '" + currency + "'"

        try:
            conn = psycopg2.connect(self._dbconnstr)
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
 
        return row


    def Insert_HistoCarList(self, data):
        
        try:
            

            sql = ''' INSERT INTO histocar_lists
                      (vehicle_model_id, vehicle_make_id, zipcode_id, onlinecardealer_id, vin_number, 
                       price, mileage, color_id, currency_id, carcondition_id, seller_name, seller_address, seller_telnumber, 
                       seller_address_region, seller_address_locality, image_url, image_local_url, content_url, 
                       content_local_url, vehicle_url, veh_description, production_year, vehicle_trim_id, vehicle_bodystyle_id )
                       VALUES (%(vehicle_modelid)s,%(vehicle_makeid)s,%(zipcodeid)s,%(onlinecardealerid)s,
                       %(vin_number)s,%(price)s,%(mileage)s,%(colorid)s,%(currencyid)s,%(carconditionid)s,
                       %(seller_name)s,%(seller_address)s,%(seller_telnumber)s,%(seller_address_region)s, 
                       %(seller_address_locality)s, %(image_url)s,%(image_local_url)s,%(content_url)s,
                       %(content_local_url)s, %(vehicle_url)s, %(description)s, %(production_year)s, 
                       %(vehicle_trim_id)s, %(bodytypeid)s) '''
         
 
            try:

                conn = psycopg2.connect(self._dbconnstr)
                cur = conn.cursor()
                cur.executemany(sql, data)
            
            #print (cur.lastrowid)
            #print ("---------------------\n") 

            except (psycopg2.Error) as err:
                print ("Error ", err) 
            
            #cur = conn.cursor()
            #cur.execute(sql, (vendor_name,))
            #histocar_listid = cur.fetchone()[0]
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
 
        return ""


#INSERT INTO public.histocar_list
#(histocar_listid, vehicle_modelid, vehicle_makeid, zipcodeid, onlinecardealerid, vin_number, 
#price, mileage, colorid, currencyid, carconditionid, seller_name, seller_address, seller_telnumber, 
#seller_address_region, seller_address_locality, image_url, image_local_url, content_url, content_local_url, 
#create_date, is_active)
#VALUES(0, 0, 0, 0, 0, '', 0, 0, 0, 0, 0, '', '', '', '', '', '', '', '', '', '', false);


#vehicle_modelid
#vehicle_makeid 
#vehicle_makeid
#zipcodeid
#onlinecardealerid
#vin_number
#price
#mileage
#colorid
#currencyid
#carconditionid
#seller_name
#seller_address
#seller_telnumber             
#seller_address_region
#seller_address_locality
#image_url
#image_local_url
#content_url
#content_local_url
