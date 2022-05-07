'''
   Description:
   Version: 1.0.0
   Written by: Arjang Fahim
   Created:
   Fixed bugs:
   Edited by:
   Updates:
'''
"""
The parser gets the pre-built URLs from 
DB
1- It checks if a URL valid
2- Get the HTML
autotraders.com URL format
example 
https://www.autotrader.com/cars-for-sale/searchresults.xhtml?zip=92603&marketExtension=on&startYear=1981&endYear=2019&makeCodeList=TOYOTA&searchRadius=25&modelCodeList=CAMRY&sortBy=relevance&numRecords=25&firstRecord=0
https://www.autotrader.com/cars-for-sale/searchresults.xhtml?zip=92603&marketExtension=on&startYear=1981&endYear=2019&makeCodeList=AUDI&searchRadius=25&modelCodeList=A4&sortBy=relevance&numRecords=25&firstRecord=0
"""
#https://www.autotrader.com/cars-for-sale/searchresults.xhtml?modelCode1=360&zip=92603&makeCode1=FER
import sys
sys.path.insert(0, '../')

from Parser.HTMLParser import HTMLParser
from URLFetcher.Fetcher import Fetcher

def main():
    print ("Parser --> main(): Initializing Fetcherer object...") 
    _fetcher = Fetcher()
    URLs = _fetcher.LoadURLs()
    print ("Parser --> main(): URLs are ready to be parsed...")
 
    #print (URLs)
    #print(URLs)
    #vendor_id = 1
    #zipcode_id = 92603
    #url = "https://www.americastire.com/fitmentresult/tires/size/205-70-15"
    #html_tire_parser = HTMLTireParser(url, vendor_id, zipcode_id)
    #html_tire_parser.DumpHTML() 
    #html_tire_parser.PasrsingPage()
    #html_parser = HTMLParser(url, vendor_id, historide_vehicle_model_id, historide_vehicle_make_id, zipcode_id)
    #html_parser.DumpHTML()
    #html_parser.PasrsingPage()
    
    for URL in URLs:
        vendor_id = URL["onlinecardealer_id"]
        historide_vehicle_model_id = URL["vehicle_model_id"]
        historide_vehicle_make_id = URL["vehicle_make_id"]
        zipcode  = URL["zipcode"]
        url = URL["url"]
        html_parser = HTMLParser(url, vendor_id, historide_vehicle_make_id, historide_vehicle_model_id, zipcode)
        print ("Dumping... ")
        html_parser.DumpHTML()
        html_parser.PasrsingPage()

if __name__ == "__main__":
    main()