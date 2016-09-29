#https://straymarcs.net/2014/12/how-to-create-your-own-weather-forecast-program-using-python/

import urllib
import json
import os

os.system('clear')
key="6a59f2e657d0997a"

#city=raw_input("Enter Zip Code: ")
print '=================================='
print '|'+'         Weather App     '+'       |'
print '=================================='
print '|'+'Welcome to the Weather App     '+' |'
print '|'+'Please enter country and city  '+' |'
print '=================================='
country=raw_input("Country Code: ")
city=raw_input("City Name: ")


url='http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/' + country + '/' + city + '.json'
url2='http://api.wunderground.com/api/' + key + '/geolookup/astronomy/q/' + country + '/' + city + '.json'

conditions=urllib.urlopen(url)
json_string=conditions.read()
parsed_json=json.loads(json_string)
location=parsed_json['current_observation']['display_location']['full']
weather=parsed_json['current_observation']['weather']
temperature_string=parsed_json['current_observation']['temperature_string']
feelslike_string=parsed_json['current_observation']['feelslike_string']
observation_time=parsed_json['current_observation']['observation_time']
observation_location=parsed_json['current_observation']['observation_location']['city']
wind_string=parsed_json['current_observation']['wind_string']
relative_humidity=parsed_json['current_observation']['relative_humidity']
dewpoint_string=parsed_json['current_observation']['dewpoint_string']
visibility=parsed_json['current_observation']['visibility_km']
UV=parsed_json['current_observation']['UV']
conditions.close()

astronomy=urllib.urlopen(url2)
json_string=astronomy.read()
parsed_json=json.loads(json_string)
sunrise_hour=parsed_json['moon_phase']['sunrise']['hour']
sunrise_minute=parsed_json['moon_phase']['sunrise']['minute']
sunset_hour=parsed_json['moon_phase']['sunset']['hour']
sunset_minute=parsed_json['moon_phase']['sunset']['minute']

moonrise_hour=parsed_json['moon_phase']['moonrise']['hour']
moonrise_minute=parsed_json['moon_phase']['moonrise']['minute']
moonset_hour=parsed_json['moon_phase']['moonset']['hour']
moonset_minute=parsed_json['moon_phase']['moonset']['minute']
moon_phase=parsed_json['moon_phase']['phaseofMoon']
percentIlluminated=parsed_json['moon_phase']['percentIlluminated']
moon_hemisphere=parsed_json['moon_phase']['hemisphere']
astronomy.close()

os.system('clear')    

def UV_Index(UV):
	UV=float(UV)
	if UV<0:
		UV_risk="Low Risk"
	elif UV>=0 and UV<=2:
		UV_risk="Low Risk"
	elif UV>=3 and UV<=5:	
		UV_risk="Moderate Risk"
	elif UV>=6 and UV<=7:	
		UV_risk="High Risk"	
	elif UV>=8 and UV<=10:	
		UV_risk="Very High Risk"	
	elif UV>=11:
		UV_risk="Extreme Risk"	
	else:
		print "Error"	
	return UV_risk
print '=================================='
print '|'+'         Weather App     '+'       |'
print '=================================='
print 'Location:', location 
print " "
print "Weather: ", weather
print "Temp: ", temperature_string
print "Feels Like: ", feelslike_string
print " "
print "Wind: ", wind_string
print "Dew Point: ", dewpoint_string
print "Humidity: ", relative_humidity
print "Visibility: ", visibility+'km'
print "UV Index: ", UV+" ("+UV_Index(UV)+")"
print " "
print "Sunrise: ",  " "+sunrise_hour+":"+sunrise_minute+"AM"
print "Sunset: ",   "  "+sunset_hour+":"+sunset_minute+"PM"
print "Moonrise: ", moonrise_hour+":"+moonrise_minute+"AM"
print "Moonset: ",  " "+moonset_hour+":"+moonset_minute+"PM"
print " "
print "Moon Phase: ", moon_phase
print "The moon is " + percentIlluminated +'%'+' illuminated/ '+moon_hemisphere+' hemisphere'
print '=================================='
print observation_time

print observation_location
print " "

