"""
   Description:  This class contains methods for database operations
   Written by:   Arjang Fahim 
   Created:      11/07/2018
   Fixed bugs: 
   Edited by:
   Updates:
"""
import psycopg2
from Database.DBConn import DBConn

class DBHelperFetcher(object):

    
    def __init__(self):
        self._dbconn = DBConn()
        self._dbconnstr = self._dbconn.ConnString()


    def FetchAllURLs(self):

        result = []
        sql = "select * from urllists where is_active = true"
     
        try:
            conn = psycopg2.connect(self._dbconnstr)
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            result = self.CurConvert(cur, rows)
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close() 
        return result

    # converts Postgre Cur to named field dictionary
    # 1- I am not sure if this is the same for MySQL as well
    # 2- Not sure if this is the best way ( the most efficient way) to do this
    def CurConvert(self, cur, rows):

        fields = []
        for row in rows:
            temp = {}
            count = 0
            for col in cur.description:
                temp.update({str(col[0]): row[count]})
                count = count + 1
            fields.append(temp)
        
        return fields   
     
