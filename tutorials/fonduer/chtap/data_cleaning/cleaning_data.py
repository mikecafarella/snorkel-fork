##10/10/2017
## SAEIDEH
### data cleaning for getting female scort profiles out of the data


import os 
import re
import shutil
#data ="<!-- http://adultsearch.com/new-york/long-island/female-escorts/1096814 -->"

#datapath="/Users/saeideh.shahrokh/Desktop/data-memex/snorkel/tutorials/fonduer/memex/data/myplugin_test_copy3/"
datapath="/Users/saeideh.shahrokh/projects/memex/data-cleaning/texas-tests/texas_t6/"
files = os.listdir(datapath)
doc_name = []
for fn in files:
	fname = fn[:-5]
	with open(datapath+fn, mode ='r') as f:
		for line in f.readlines():
			if line.startswith("<!-- http:") or line.startswith("<!-- https:") :
				#print "hello"
				if re.search(r'/female-escorts',line):
					#print "hi"
					split_line = line.split("/")
					for i in split_line:
						if re.search(r'^\d+\s*(-->)',i): 
								
								doc_name.append(fn)
								

print len(doc_name)
profile_datapath="/Users/saeideh.shahrokh/projects/memex/data-cleaning/texas-tests/"

profile_folder = profile_datapath + '/texas_profiles_6/'
if not os.path.exists(profile_folder): 
	os.makedirs(profile_folder)
for file in doc_name:
	file_basename=os.path.basename(file)
	#print file
	#print profile_folder+file_basename
  	shutil.move(datapath+'/'+file, profile_folder)
