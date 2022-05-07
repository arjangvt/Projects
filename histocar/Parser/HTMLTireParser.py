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
from Logging.Logging import Logging



"""
    Check db for available URLs
"""

class HTMLTireParser(object):

       
    def __init__(self, url, tire_vendor_id, zipcode_id):
        self.l = Logging()
        print ("initializing HTMLParser object\n")
        print ("Message: reading config file.\n")
        config = Config('config.ini')
        self._html_file_dir = config.getHTMLPath()
        self._image_file_dir = config.getImagesPath()

        self._url = url
        print ("Message: reading URL:\n")
        print ("Message: url=" + url + "\n")
        self._tire_vendor_id = tire_vendor_id
        print ("Message: vendor_id=" + str(tire_vendor_id) + "\n")
        self._zipcodeid = zipcode_id
        print ("Message: zipcode_id=" + str(zipcode_id) + "\n")
        print ("Finished HTMLParser initialization." + "\n")
           
        
    def LoadURLs(self, url):

        try:
            self._url = url 
            print("URL " + self.url + " is loaded.\n")
        except(Exception) as error: 
            print ("Error: {")
            print (type(error))
            print (error.args)
            print (error)
            print ("}") 
    
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
            headers ={'User-Agent': 'Mozilla/5.0 (Machintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}
            resp = requests.get(self._url, headers=headers)

            #TODO: better archiving and nameing file mechanism
            #page = response.url.split("/")[-2]
            page =  str(uuid.uuid1())
            filename = '%s.html' % page
            filename = "tire-" + filename

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
        
        if (self._tire_vendor_id == 1):
            self.AmericanTire()

        return

 

    def AmericanTire(self):

        headers ={'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','accept-encoding' : 'gzip, deflate, br','accept-language' : 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7','cookie' :'TS01c4ee78=019de3c5d945d607aace681959d07e3b3177624bd45a6fc5bb934dfc874c52e7e7d0941a063e668d2d2e653fe6a19b0cc655b97fa4; rxVisitor=1544323123566ANKDTET43M9OLJMUPI0L0US6QI48VFM3; searchArea=92612; myStoreCookie=1458; D_SID=68.231.213.59:iu9GpxteNjqq/QDDTcWhIutXodFvtlwx2Nnzj+yPFTo; TLTSID=H9TZ9RPB16602VEUGE6AFML27085J4X5; _ga=GA1.2.1989247356.1544323128; _gcl_au=1.1.2057093884.1544323129; __qca=P0-207733436-1544323129547; americastire-cart=a41b8487-61c4-412a-b1bd-f1aa57b9367f; D_IID=0FD99C00-C0DC-36DD-99C1-0428E2F6C389; D_UID=81812D70-2B06-3EFF-BC11-91F5E8E75DC3; D_ZID=5E39C417-AD0A-30C1-8391-5631E28163B7; D_ZUID=88610665-499B-3D90-89AB-51C7EC2EAC6B; D_HID=DAA01774-FB16-3EE5-BFCD-70A2132D97CF; americastire-recentlyViewed-anonymous=28450__32518__; _gid=GA1.2.1212383515.1544596489; JSESSIONID=817E3DA0DD040F5384F2985E813C683A; dtSa=-; mmcore.tst=0.385; last_interacted_list=Entry_, Sort_price (low to high); mmapi.store.p.0=%7B%22mmparams.d%22%3A%7B%7D%2C%22mmparams.p%22%3A%7B%22pd%22%3A%221576223763090%7C%5C%22-218541982%7CHAAAAApVAwCeUOFPCBHgWQABEQABQkuHVpAGADlBEG3QYNZIp901cn9d1kgAAAAA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8ABkRpcmVjdAEIEQYAAAAAAAAAAAA8BgIA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8CAN7gAAA6vEi9DAgRAP%2F%2F%2F%2F8BCBELEf%2F%2FAgAAAQAAAAABKwECAJALAwABPAYCAAEAAAAp4QAAqtYzFPQIEQD%2F%2F%2F%2F%2FAQgRDBH%2F%2FwwAAAEAAAAAAc8BAgCQDAMAAAAAAAAAAUU%3D%5C%22%22%2C%22srv%22%3A%221576223763100%7C%5C%22lvsvwcgus05%5C%22%22%7D%2C%22mmengine%22%3A%7B%7D%7D; mmapi.store.s.0=%7B%22mmparams.d%22%3A%7B%7D%2C%22mmparams.p%22%3A%7B%7D%2C%22mmengine%22%3A%7B%22mm1%22%3A%220%7C%5C%22yes%5C%22%22%2C%22mm2%22%3A%220%7C%5C%22yes%5C%22%22%7D%7D; AWSELB=57C379DB040AACF4D1FB5A46E779A6624ACD2543A7FCE5E546C7206ACC3A23C01777AA4DDCD0ACFBA58F05A7F895369A10F267DFFF2735A98D5AB4936FA20B821974C6CD26A4DEB43131A541E00819D260EE2DD36E; TS01cd60d2=019de3c5d961d2aade53a9c4f3e32c4e4718251421a2eb19844c48f276f0028383bcd9aca8a755ebd82e87c589a6d2bc62ddd4db9b31fc1ca39c937d8547e6c209b7f0016e5e4224c37a55c624571b3d1184314a914a6efbf1f035555cd03b87202fa6083c45be8eadda12ed6ff88d20af567ec3ee3f643943fa06d6731a963189b852a96e07ea7c8f18fd139fce2e40a19a74ff12bbac39eaf50e5cdbade81a31a9109dc9; utag_main=v_id:016790d4db35007cad253f331e1803073001d06b0086e$_sn:7$_ss:1$_st:1544689564181$_pn:1%3Bexp-session$ses_id:1544687762829%3Bexp-session; _tq_id.TV-72459018-1.a045=501a153982e9c4f3.1544323130.0.1544687765..; dtLatC=1; dtCookie=2$7D6C58BEBE1645802C2D4DE4FF2BB237|Prod+-+America%27s+Tire|1; dtPC=2$283855010_1h-vGJCPCLIKNPBPAENEGMBODLPEXKDPOGEE; rxvt=1544734572097|1544732772097','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        page = requests.get(self._url, headers=headers)
        page_tree_struct = html.fromstring(page.content)
        loaded_json = page_tree_struct.xpath('//script[@type="application/ld+json"]/text()')


        print (loaded_json)

        exit() 
        # Converting string jason format to a json object
        _json = json.loads(loaded_json[3])       
        _dbhelper = DBHelperParser()
        data = []
        
        exit()
        for x in _json:

            dict = {}

            vehicle_modelid = self._histo_vehicle_model_id
            dict["vehicle_modelid"] = self._histo_vehicle_model_id

            vehicle_makeid = self._histo_vehicle_make_id
            dict["vehicle_makeid"] = self._histo_vehicle_make_id

            #TODO: I get zipid 
            zipcodeid = self._zipcodeid
            dict["zipcodeid"] = self._zipcodeid

            onlinecardealerid = self._vendor_id 
            dict["onlinecardealerid"] = self._vendor_id

            vin_number = x['vehicleIdentificationNumber']
            dict["vin_number"] = x['vehicleIdentificationNumber']


            data.append(dict)

           
        #list_id = _dbhelper.Insert_HistoCarList(data)
        #print("New record id " + list_id)
