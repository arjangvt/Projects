import psycopg2

class DBConn(object):

    """
       This variable is exposed to the outside
       Used this way just to have OOP look! 
    """
    #TODO: Later the conn string should be read from 
    #TODO: config file 

    #set conn string here
    

    def __init__(self):

        #self._conn_string = "host=ec2-107-22-238-217.compute-1.amazonaws.com dbname=ddl9h5fc3psggr user=hjbhzdncvsqgzm password=63bf06a6122b2487d14d07f62bf9892fa88bb0e97f2f3c55c9e40eb521424f64"
        self._conn_string = "dbname=historide user=postgres password=postgres"
    
    """
    retruns connection string 
    """
    def ConnString(self):
        return self._conn_string
  	
    def Connect(self):
        try:
        	
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(self._conn_string)
            print('Coonection was established successfully...')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None   	
         
        return conn 
