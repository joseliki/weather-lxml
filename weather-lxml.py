#!/usr/bin/python
import requests
from lxml import etree
dicc = {'1':'Almeria','2':'Cordoba','3':'Cadiz','4':'Jaen','5':'Malaga','6':'Granada','7':'Huelva','8':'Sevilla'}
values = dicc.values()
url = 'http://api.openweathermap.org/data/2.5/weather'
payload = {'q':'%s,Spain','mode':'xml','units':'metrics','lang':'es'}
response = requests.get(url, params=payload)
dato = etree.fromstring(response.content)
for i in dato:
	eti = i.attrib
	print eti
	
	
	
	
	
	
	
		
	
	
		
			
	
	
