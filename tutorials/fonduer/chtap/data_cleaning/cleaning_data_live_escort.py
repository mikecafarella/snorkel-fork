##10/10/2017
## SAEIDEH
### data cleaning for getting female scort profiles out of the data


import os 
import re
import shutil
#data ="<!-- http://adultsearch.com/new-york/long-island/female-escorts/1096814 -->"

#datapath="/Users/saeideh.shahrokh/Desktop/data-memex/snorkel/tutorials/fonduer/memex/data/myplugin_test_copy3/"
datapath="/home/jdunnmon/research/re/projects/memex/data/s3/data_live_escort_20171206/"
print(datapath)
files = os.listdir(datapath)
files = [f for f in files if f[-3:]!='crc']
doc_name = []
for fn in files:
	fname = fn[:-5]
	with open(datapath+fn, mode ='r') as f:
		for line in f.readlines():
			if re.search(r'terReport',line):
				    doc_name.append(fn)
								

print len(doc_name)
profile_folder = datapath + '../live_escort_profiles/'
if not os.path.exists(profile_folder): 
	os.makedirs(profile_folder)
for file in doc_name:
	file_basename=os.path.basename(file)
  	shutil.copy(datapath+'/'+file, profile_folder)
