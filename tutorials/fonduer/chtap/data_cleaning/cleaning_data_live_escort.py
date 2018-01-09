##01/09/2017
## Jared Dunnmon
### data cleaning for getting profiles out of live escort data


import os 
import re
import shutil

datapath="/home/jdunnmon/research/re/projects/memex/data/s3/data_live_escort_20171206/"
files = os.listdir(datapath)
files = [f for f in files if f[-3:]!='crc']
doc_name = []
#using single rule based on existence of 'terReport' class
for fn in files:
	fname = fn[:-5]
	with open(datapath+fn, mode ='r') as f:
		for line in f.readlines():
			#if re.search(r'terReport',line):
                        if re.search(r'^read reviews$|^write a review$|^no ter review found$|^ter id$',line.lower()):
				    doc_name.append(fn)
								

print len(doc_name)
profile_folder = datapath + '../live_escort_profiles/'
if not os.path.exists(profile_folder): 
	os.makedirs(profile_folder)
for file in doc_name:
	file_basename=os.path.basename(file)
  	shutil.copy(datapath+'/'+file, profile_folder)
