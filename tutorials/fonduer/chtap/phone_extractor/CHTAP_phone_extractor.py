from bs4 import BeautifulSoup
import os
from phonenumbers.python import phonenumbers
#-*- coding: utf-8 -*- 
import sys
import io
import codecs
import json
reload(sys)
sys.setdefaultencoding("utf-8")

def finde_phone_number(text):

	
	for match in phonenumbers.PhoneNumberMatcher(text, "US"):
		num = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL)
 		yield num.encode('utf-8')
 		

def phone_ext(text):
	
	lst =[]
	for i in finde_phone_number(text):
		lst.append(i)
	return lst

##################################
path = '../data/profiles_chtap/'

files = os.listdir(path)
#define a list of document name
phone_dict = {}
doc_name = []
for fn in files:
    #print (fn)
    #print fn
    fname= fn[:-5]
    #print fn[:-5]
    doc_name.append(fname)
    #print doc_name
    with codecs.open(path + fn, mode="r", encoding="utf-8") as f:#open(path + fn, 'r') as f:

        ftext = f.read()
        #print type(ftext)
     
	phones = phone_ext(ftext)
	phone_dict[fn[:-5]] = phones


print "number of doc:\n" , len(phone_dict.keys())

path2= '../data/analysis/'

json.dump(phone_dict, open( path2+ "out_put_phone_1.text",'w'))

   
