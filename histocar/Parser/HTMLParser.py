import sys
sys.path.insert(0, '../')
import httplib2
import json
import urllib.request as ur
import requests
import uuid
import configparser

from Database.DBConn import DBConn
from Database.DBHelperParser import DBHelperParser
from Configuration.Config import Config 
from lxml import html
from datetime import datetime
#from Logging.Logging import Logging


"""
    Check db for available URLs
"""

class HTMLParser(object):

    
    def __init__(self, url, vendor_id, histo_vehicle_make_id, histo_vehicle_model_id, zipcode):
        
        config = Config('config.ini')
        self._html_file_dir = config.getHTMLPath()
        self._image_file_dir = config.getImagesPath()
        self._url = url
        print ("HTMLParser --> __init__: Reading URL:\n")
        print ("Message: url=" + url + "\n")
        self._vendor_id = vendor_id
        print ("HTMLParser --> __init__: vendor_id=" + str(vendor_id) + "\n")
        self._histo_vehicle_make_id = histo_vehicle_make_id
        print ("HTMLParser --> __init__: vehicle_make_id=" + str(histo_vehicle_make_id) + "\n")
        self._histo_vehicle_model_id = histo_vehicle_model_id
        print ("HTMLParser --> __init__: histo_vehicle_model_id=" + str(histo_vehicle_model_id) + "\n")

        self._zipcode = zipcode
        #print ("Message: zipcode=" + str(zipcode) + "\n")
        print ("HTMLParser --> __init__: Finishing HTMLParser initialization." + "\n")
          
        
    def LoadURLs(self, url):
        try:
            self._url = url 
            #print("URL " + self.url + " is loaded.\n")
        except(Exception) as error:
            #2 is for error code
            print (error.args)
            print (error)
            print (type(error))
          
    #TODO: It is not accurate needs to be revised
    def IsURLValid(self):
        print ("method: IsValid\n")
        try:
            h = httplib2.Http()
            resp = h.request(self._url, 'HEAD')            
            return True    
        except(Exception) as error:
            print ("Error: {")
            print (type(error))
            print (error.args)
            print (error)
            print ("}") 
            return False

    def DumpHTML(self):
        """
            This method dumps the html and saves it 
            on the disk!
        """
        print ("method: DumpHTML\n")

        try:
            if (self._url == ""):
                raise Exception ('URL is not provided\n')
                exit()
      
            print ("Messge: Dumping HTML file.\n")
            headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
            resp = requests.get(self._url, headers=headers)
            #resp = requests.get(self._url)
            #response = ur.urlopen(self._url)
            #webcontent = response.read()       

            #TODO: better archiving and nameing file mechanism
            #page = response.url.split("/")[-2]
            page =  str(uuid.uuid1())
            filename = '%s.html' % page

            self._HTMLfilename = self._html_file_dir + "//" + filename
          
            print ("Message: Opening a new file.\n")
            print ("Message: filename=" + self._HTMLfilename)
            f = open(self._HTMLfilename, 'w')
            f.write(resp.text)
            f.close
            print ("HTML file for the URL ' %s  ' is saved sucessfully\n" %self._url)
        except(Exception) as error:
            print ("Error: {")
            print (type(error))
            print (error.args)
            print (error)
            print ("}") 



    #TODO: This method depends on the website, so it is diffrenet for each website
    #TODO: To improve we need regex and AI ....  
    def PasrsingPage(self):
        
        if (self._vendor_id == 1):
            self.CarsDotCom()

        if (self._vendor_id == 2):
            self.AutoTraderDotCom()             
        return

    def AutoTraderDotCom(self):
        
        print ("In the auto trader...")
        colorid = "0"
        mileage = "0"
        bodytypeid = "0"

        #url = "https://www.autotrader.com/cars-for-sale/Toyota/Camry/Irvine+CA-92603?zip=92603&marketExtension=true&startYear=1981&endYear=2019&makeCodeList=TOYOTA&searchRadius=25&modelCodeList=CAMRY&sortBy=relevance&numRecords=25&firstRecord=0"
        #url ="https://www.cars.com/for-sale/searchresults.action/?mdId=20800&mkId=20088&rd=99999&searchSource=QUICK_FORM&stkTypId=28881&zc=92603"
        #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        page = requests.get(self._url, headers=headers)
        print ('page', page)
        
        '''
        f = open("test.txt", 'w')
        f.write(page.text)
        f.close
        '''
        page_tree_struct = html.fromstring(page.content)
        print ('page_tree_struct: ', page_tree_struct)
        #loaded_json = page_tree_struct.xpath('//script[@data-cmp="lstgSchema"]')
        loaded_json = page_tree_struct.xpath('//script[@type="application/ld+json"]/text()')
        #print ('loaded: ', loaded_json)
        _dbhelper = DBHelperParser()
        data = []
 
        for x in loaded_json:
            
            dict = {}

            vehicle_modelid = self._histo_vehicle_model_id
            dict["vehicle_modelid"] = self._histo_vehicle_model_id

            vehicle_makeid = self._histo_vehicle_make_id
            dict["vehicle_makeid"] = self._histo_vehicle_make_id

            #TODO: I get zipid 
            #zipcode = self._zipcode
            dict["zipcodeid"] = self._zipcode

            onlinecardealerid = self._vendor_id 

            dict["onlinecardealerid"] = self._vendor_id

            _json_cars_info = json.loads(x)
            if (_json_cars_info['@type'] != "Car"):
                continue

            if 'vehicleIdentificationNumber' in _json_cars_info.keys():
                vin_number = _json_cars_info['vehicleIdentificationNumber']
                dict["vin_number"] = vin_number
            else:
                dict["vin_number"] = ""

            price = _json_cars_info['offers']['price']
            dict["price"] = _json_cars_info['offers']['price']

            
            mileage = _json_cars_info['mileageFromOdometer']['value']
            if (mileage != ""):
                dict["mileage"] = mileage.replace(",", "")
            else:
                dict["mileage"] = "0"    

            color = _json_cars_info['color']
            color = color.lower()
            
            #print ("Hello") 
            #print(len(color))

            _colorid = _dbhelper.FindColorID(color)
            if (_colorid != None and color != ""):
                colorid = _colorid[0]
                dict["colorid"] = colorid
            else:
                dict["colorid"] = colorid 
             
            if "bodyType" in _json_cars_info:
                #print (_json_cars_info['bodyType']) 
                bodytype = _json_cars_info['bodyType'][0]                
                bodytype = bodytype.lower()
                #print (bodytype) 
            else:
                #print ("Bodytyoe nothinf")
                bodytype = ""

            _bodytypeid = _dbhelper.FindCarBodyTypeID(bodytype)
            if (_bodytypeid != None and bodytype != ""):
                bodytypeid = _bodytypeid[0]
                print (bodytypeid)
                dict["bodytypeid"] = bodytypeid 
            else:
                dict["bodytypeid"] = bodytypeid           
                print ("bti:", bodytypeid)
 
            trim = 0
            if "trim" in  _json_cars_info:
                trim = _json_cars_info['trim']
                if (trim == ""):
                    trim = 0
            else:
                trim = 0
                print ("Keyword 'trim' doesn't exist")

            dict['vehicle_trim_id'] = trim

            
            _year = _json_cars_info['productionDate']

            if (_year != None and _year != ""):
                dict["production_year"] = _json_cars_info['productionDate']
            else:
                dict["production_year"] = 0

            currency = _json_cars_info['offers']['priceCurrency']
            _currencyid = _dbhelper.FindCurrencyID(currency) 
            currencyid = _currencyid[0]
            dict["currencyid"] = currencyid
             
            carconditionid = 0
            dict["carconditionid"] = carconditionid

            dict["description"] =  _json_cars_info['description']
            dict["seller_name"] = ""
            dict["seller_address"] = ""
            dict["seller_telnumber"] = ""
            dict["seller_address_region"] = ""
            dict["seller_address_locality"] = ""
                      
            image_url = _json_cars_info['image']
            dict["image_url"] = image_url

            vehicle_url = _json_cars_info['url']
            dict["vehicle_url"] = vehicle_url

         
            #first download the image then save and rename it.
            dest_image_file = self._image_file_dir + "//" + str(uuid.uuid1()) + ".jpg"

            image_local_url = dest_image_file   # needs to be taken care of
            dict["image_local_url"] = image_local_url

            
            content_url = self._url        # needs to be taken care of
            dict["content_url"] = content_url   
            
            content_local_url = self._HTMLfilename  # needs to be taken care of
            dict["content_local_url"] = content_local_url

            create_date = datetime.now()
            dict["create_date"] = str(create_date)

            is_active = True
            dict["is_active"] = str(is_active)
            data.append(dict)           
            
        print ("Ready to save...")    
        list_id = _dbhelper.Insert_HistoCarList(data)


    def CarsDotCom(self):
        page = requests.get(self._url)
        page_tree_struct = html.fromstring(page.content)
        loaded_json = page_tree_struct.xpath('//script[@type="application/ld+json"]/text()')
        # Converting string jason format to a json object
        _json = json.loads(loaded_json[4])       
        _dbhelper = DBHelperParser()
        data = []
        
        colorid = ""
        vin_number = ""
        currency = ""
        seller_name = ""
        seller_telnumber = ""
        seller_address = ""        
        seller_address_region = ""
        seller_address = ""
        seller_telnumber = ""
        mileage = 0
        carconditionid = 0

        for x in _json:
            
            dict = {}

            vehicle_modelid = self._histo_vehicle_model_id
            dict["vehicle_modelid"] = self._histo_vehicle_model_id

            vehicle_makeid = self._histo_vehicle_make_id
            dict["vehicle_makeid"] = self._histo_vehicle_make_id

            #TODO: I get zipid 
            #zipcode = self._zipcodeid
            dict["zipcode"] = self._zipcode

            onlinecardealerid = self._vendor_id 
            dict["onlinecardealerid"] = self._vendor_id

            vin_number = x['vehicleIdentificationNumber']
            #print("vin", vin_number, "\n")
            dict["vin_number"] = x['vehicleIdentificationNumber']

            price = x['offers']['price']
            dict["price"] = x['offers']['price']

            dict["mileage"] = 0

            if (x['color'] != None or x['color'] != ""):   
                    color = x['color']
            #dict["color"] = x['color']
                    color = color.lower()
                    _colorid = _dbhelper.FindColorID(color)

            if _colorid != None:
                colorid = _colorid[0]
                dict["colorid"] = colorid
            else:
                dict["colorid"] = colorid 

            currency = x['offers']['priceCurrency']
            _currencyid = _dbhelper.FindCurrencyID(currency) 
            currencyid = _currencyid[0]
            dict["currencyid"] = currencyid

            dict["carconditionid"] = carconditionid

            seller_name = x['offers']['seller']['name']
            dict["seller_name"] = seller_name 

            if 'streetAddress' in  x['offers']['seller']['address'].keys():
                seller_address = seller_address + x['offers']['seller']['address']['streetAddress']
            if 'addressRegion' in x['offers']['seller']['address'].keys():
                seller_address = seller_address + " " + x['offers']['seller']['address']['addressRegion']
            if 'addressLocality' in x['offers']['seller']['address'].keys(): 
                seller_address = seller_address + " " + x['offers']['seller']['address']['addressLocality']        
            dict["seller_address"] = seller_address             

            if 'telephone' in x['offers']['seller'].keys():
                seller_telnumber = x['offers']['seller']['telephone']
            dict["seller_telnumber"] = seller_telnumber             
            
            if 'addressRegion' in x['offers']['seller']['address'].keys():
                 seller_address_region = x['offers']['seller']['address']['addressRegion']
            dict["seller_address_region"] = seller_address_region

            seller_address_locality = ""
            if 'addressLocality' in x['offers']['seller']['address'].keys():
                 seller_address_locality = x['offers']['seller']['address']['addressLocality']
            dict["seller_address_locality"] = seller_address_locality
                      
            image_url = x['image']
            dict["image_url"] = image_url

            #first download the image then save and rename it.
            dest_image_file = self._image_file_dir + "//" + str(uuid.uuid1()) + ".jpg"

            ur.urlretrieve(image_url, dest_image_file)

            image_local_url = dest_image_file   # needs to be taken care of
            dict["image_local_url"] = image_local_url

            content_url = self._url        # needs to be taken care of
            dict["content_url"] = content_url   

            content_local_url = self._HTMLfilename  # needs to be taken care of
            dict["content_local_url"] = content_local_url

            create_date = datetime.now()
            dict["create_date"] = str(create_date)

            is_active = True
            dict["is_active"] = str(is_active)           

            data.append(dict)

        #print (data)    
        list_id = _dbhelper.Insert_HistoCarList(data)
        print("New record id " + list_id)

#for testing purpose
#print("hi")
#h = HTMLParser("www.historide.com","test","test","test","test")
#h.LoadURLs("www.historide.com")