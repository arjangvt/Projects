import sys
import logging
import os

from Configuration.Config import Config 

# TODO: I changed it to save log into a separate files
#       If the file name is the same then content should
#

class Logging:
	def __init__(self, filename):
		logging.basicConfig(level=logging.INFO,format='%(asctime)-15s %(levelname)s %(message)s')
		self.logger = logging.getLogger(__name__)
		self.type_dict = {1: "Log", 2: "Error"}
	
	def log(self,className,message,sysinfo,type):
		if self.type_dict[type] == "Error":
			exc_type, exc_obj, exc_tb = sysinfo
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			#self.logger.error("ClassName: %s Line: %s Message: %s",className,exc_tb.tb_lineno,message)
			print(os.getcwd())
			os.chdir("..")
			os.chdir("LocalStorage/logs")
			hdlr = logging.FileHandler('log.txt')
			formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
			hdlr.setFormatter(formatter)
			self.logger.addHandler(hdlr)
			#config = Config('config.ini')
			#self._log_file_dir = config.getLogsPath()
			#self._LOGfilename = self._log_file_dir + "//" + filename
			self.logger.error("ClassName: %s Line: %s Message: %s",className,exc_tb.tb_lineno,message)
			#print("ankit here")
		else:
			self.logger.info("Debug mode")