'''
Created on Jun 3, 2016

@author: Shrinath
'''
import sys
import json
from pprint import pprint
from collections import OrderedDict # This converts json file into object with order
""" printKeyValue method prints the key value in hierarchical form of any type of JSON file"""

class JsonParser:
    
    def __init__(self,space=0):
        self.space = space # It is used for give spacing before any print
    ''' This is recursive function. It is general so any JSON  file can be parsed'''
        
    def printKeyValue(self,j_obj):
        #Edge case if given json object is not valid then terminate program
        if not isinstance(j_obj, dict):
            return None
        # Iterate over all key value pairs.
        for key, value in j_obj.items():
            if isinstance(value, dict): # if value is again dictionary call this method recursively
                print ''.ljust(self.space),key," =>" #add spaces before string. It is to print hierarchical order.
                self.space +=3 
                self.printKeyValue(value) # recursive call
                self.space -=3
            elif isinstance(value, list):
                for ind,ele in enumerate(value):  # it count the ind form 0 to length of value list
                    if isinstance(ele, dict): # if element is again dictionary call this method recursively
                        print ''.ljust(self.space),key , [ind], " =>"
                        self.space +=3 
                        self.printKeyValue(ele) # recursive call
                        self.space -=3 
                    else:
                        print ''.ljust(self.space),key, [ind], " =>", ele # if value is not dictionary then print it.
            else:
                print ''.ljust(self.space), key, " =>", value #if value is not dictionary then print it.
             
    
    
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
