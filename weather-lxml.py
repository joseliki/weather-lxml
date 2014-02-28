#!/usr/bin/python
# *-* encoding: UTF-8 *-*
import requests
from lxml import etree
from jinja2 import Template
import webbrowser

def orienta_viento(o):
	if o>=337.5 and o<=360.0 or o>=0 and o<22.5:
		return "N"
	if o>=22.5 and o<=67.5:
		return "NE"
	if o>=67.5 and o<112.5:
		return "E"
	if o>=112.5 and o<157.5:
		return "SE"
	if o>=157.5 and o<202.5:
		return "S"
	if o>=202.5 and o<247.5:
		return "SE"
	if o>=247.5 and o<292.5:
		return "O"
	if o>=292.5 and o<337.5:
		return "NO"

provincias = ['Almeria','Cordoba','Cadiz','Jaen','Malaga','Granada','Huelva','Sevilla']
file = open('wheather.html','r')
nuevo = open('weather.html','w')
list_tempmin=[]
list_tempmax=[]
list_wind=[]
for i in range(8):
	url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&mode=xml&units=metric&lang=es' %provincias[i]
	response = etree.parse(url)
	temp_min = response.find('temperature')
	temp_min1 = temp_min.attrib['min']
	list_tempmin.append(temp_min1)
	temp_max = response.find('temperature')
	temp_max1 = temp_max.attrib['max']
	list_tempmax.append(temp_max1)
	wind = response.find('wind/speed')
	wind1 = wind.attrib['value']
	list_wind.append(wind1)
		
			
	
	
	
pagina = ""
for t in file:
 pagina += t
miplantilla = Template(pagina)
salida = miplantilla.render(provincias=provincias, temp_min=list_tempmin, temp_max=list_tempmax, wind=list_wind)
nuevo.write(salida)	
webbrowser.open("weather.html")
	
	

	 
	

	
	

	
			
	
	
	
	
	
	
	
	
		
	
	
		
			
	
	
