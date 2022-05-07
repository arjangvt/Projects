import sys
sys.path.insert(0, '../')
from URLFetcher.Fetcher import Fetcher
#from Database.DBConn import DBConn

def main():
    #URL = "https://www.autotrader.com/cars-for-sale/searchresults.xhtml?zip=92603&marketExtension=on&startYear=1981&endYear=2019&makeCodeList=BMW&searchRadius=25&modelCodeList=320I&sortBy=relevance&numRecords=25&firstRecord=0" 
    #URL = "https://www.cars.com/for-sale/searchresults.action/?mdId=58489&mkId=20066&rd=20&searchSource=QUICK_FORM&stkTypId=28881&zc=92612"
    fetcher = Fetcher()
    fetcher.LoadURLs()
 

if __name__ == "__main__":
    main()