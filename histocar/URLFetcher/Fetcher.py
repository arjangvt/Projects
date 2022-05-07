import sys
sys.path.insert(0, '../')

from Database.DBConn import DBConn
from Database.DBHelperFetcher import DBHelperFetcher


"""
    Check db for available URLs
"""

class Fetcher(object):

   
    def __init__(self):
        pass
    
    """
        This methods loads all URLs  URLS from database for parsing and processing
    """    
    def LoadURLs(self):
 
        try: 
            _dbhelper = DBHelperFetcher()
            records = _dbhelper.FetchAllURLs()  
        except(Exception):
            print("Exception: " + error)
        
        return records
