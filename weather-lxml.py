#!/usr/bin/python
# *-* encoding: UTF-8 *-*
import requests
from lxml import etree
from jinja2 import Template
import webbrowser

provincias = ['Almeria','Cordoba','Cadiz','Jaen','Malaga','Granada','Huelva','Sevilla']
file = open('wheather.html','r')
nuevo = open('weather.html','w')
list_tempmin=[]
list_tempmax=[]
list_wind=[]
list_viento=[]
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
	viento1 = response.find('wind/direction')
	viento2 = viento1.attrib['code']	
	list_viento.append(viento2)		
	
	
	
pagina = ""
for t in file:
 pagina += t
miplantilla = Template(pagina)
salida = miplantilla.render(provincias=provincias, temp_min=list_tempmin, temp_max=list_tempmax, wind=list_wind, direction=list_viento)
nuevo.write(salida)	
webbrowser.open("weather.html")
	
	

	 
	

	
	

	
			
	
	
	
	
	
	
	
	
		
	
	
		
			
	
	
