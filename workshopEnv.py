import arcpy
import os
import urllib
import zipfile
from arcpy import env

print 'Downloading class data into home directory'
url = 'https://dl.dropboxusercontent.com/u/17521862/WLIA_2016_classdata.zip'
home = os.path.expanduser("~")
print 'home directory: ' + home
wd = home + '\\pythonWorkshopWLIA2016'
print 'working directory: ' + wd
fgdb = wd + '\\WLIA_pythonclass_data.gdb'
print 'class data: ' + fgdb


def refresh_data():
	if not os.path.exists(wd):
		os.makedirs(wd)
	urllib.urlretrieve(url, wd + '\\data.zip')
	f = open(wd + '\\data.zip', 'rb')
	print wd + '\\data.zip'
	z = zipfile.ZipFile(f)
	for name in z.namelist():
		z.extract(name, wd)
	f.close()
	os.remove(wd + '\\data.zip')
	env.workspace = fgdb
	feature_classes = arcpy.ListFeatureClasses()
	rasters = arcpy.ListRasters()
	datasets = feature_classes + rasters
	roads = feature_classes[0]

refresh_data()


