# -*- coding: utf-8 -*-
#
#geoip.py 
#日本をカウント 2014/12/05
#python geoip.py /Volumes/ELECOM_USB/morto_csv/srcIP/uniq/result_sensor12_201401010000.csv
#
from __future__ import print_function
import __future__
import GeoIP
import sys,os

f=open(sys.argv[1])



#list=f.readlines()
#for a in range(10):
#    print(list[a].rstrip())

filename = os.path.basename(sys.argv[1])
num = filename[20:22]
gi = GeoIP.open("/Users/koide/geoip/GeoIP_2014"+num+".dat",GeoIP.GEOIP_STANDARD)

count = 0
for row in f:
    if row.rstrip() == 'SrcIP':
        continue
    if gi.country_code_by_addr(row.rstrip()) == 'JP':
        count+=1  
print(count)
