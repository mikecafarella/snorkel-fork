''' Saeideh 10/1/2017
create a spreadsheet containing all file names and urls of profiles '''
import os 
import re
import shutil
import pandas as pd
from pandas import DataFrame
#data ="<!-- http://adultsearch.com/new-york/long-island/female-escorts/1096814 -->"
#path = './data/myplugin_test/'
#g_path= "/Users/saeideh.shahrokh/Desktop/data-memex/snorkel/tutorials/fonduer/memex/data/garbage_test1/"
#datapath="/Users/saeideh.shahrokh/Desktop/data-memex/snorkel/tutorials/fonduer/memex/data/myplugin_test_copy3/"
datapath="/Users/saeideh.shahrokh/projects/memex/data-cleaning/texas-tests/texas_profiles_6/"
files = os.listdir(datapath)
doc_name = []
url_list =[]
for fn in files:
	doc_name.append(fn)
	with open(datapath+fn, mode ='r') as f:
		for line in f.readlines():
			if line.startswith("<!-- http:") or line.startswith("<!-- https:") :
				url_list.append(line)
print len(doc_name)
print len(url_list)

df = DataFrame({'file name': doc_name, 'url': url_list})
writer = pd.ExcelWriter('texas_profiles.xlsx')
df.to_excel(writer, sheet_name='sheet1', index=False)
writer.save()
