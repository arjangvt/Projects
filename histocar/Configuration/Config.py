import os
import sys
sys.path.insert(0, '../')

from configparser import SafeConfigParser

class Config(object):

    def __init__(self, configfile):

        if os.path.isfile(configfile):
            self._config = SafeConfigParser()
            self._config.read(configfile)
            #print (self._configfile)

    # This section is setting for Parser
    def getHTMLPath(self):
        return self._config.get('PATHS','htmls')
        #print (self._config.get('PATHS','htmls'))

     
        
    def getImagesPath(self):
        return self._config.get('PATHS','images')

    def getLogsPath(self):
        return self._config.get('PATHS','logs')

    