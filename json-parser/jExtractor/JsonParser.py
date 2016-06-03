'''
Created on Jun 3, 2016

@author: Shrinath
'''
import sys
import json
from pprint import pprint
from collections import OrderedDict # This converts json file into object with order

class JsonParser:
    
    def __init__(self,space=0):
        self.space = space
        
    def printKeyValue(self,j_obj):
        if not isinstance(j_obj, dict):
            return None
        for key, value in j_obj.items():
            if isinstance(value, dict):
                print ''.ljust(self.space),key," =>"
                self.space +=3 
                self.printKeyValue(value)
                self.space -=3
            elif isinstance(value, list):
                for ind,ele in enumerate(value):
                    if isinstance(ele, dict):
                        print ''.ljust(self.space),key , [ind], " =>"
                        self.space +=3 
                        self.printKeyValue(ele)
                        self.space -=3 
                    else:
                        print ''.ljust(self.space),key, [ind], " =>", ele
            else:
                print ''.ljust(self.space), key, " =>", value
             
    
    
def main():
    try:
        fd = open("tests/test3.json",'r')
        json_obj = json.load(fd,object_pairs_hook=OrderedDict)
        fd.close()
    except IOError:
        print "IO error:- file does not found"
        sys.exit()
    obj = JsonParser()
    obj.printKeyValue(json_obj)

if __name__ == '__main__':
    main()
else:
    print "File is imported"
