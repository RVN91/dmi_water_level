# encoding: utf8   
## Description
# Name: water_level.py
# Function: Scrape water levels from DMI's database 
# Terminal call: water_level.py station starttime endtime sleep_int sleep_time
# Author: Rasmus Nielsen, 2013
#
# Input:
# station:    Station number of the station from which the data is downloaded 
#             See list of station numbers below.
# starttime:  Start date of the requested data in this date format 'dd-mm-yyyy'
# endtime:    Start date of the requested data in this date format 'dd-mm-yyyy'
# sleep_int:  Interval between downloads of records (optional, default 50)
# sleep_time: Pause in seconds between each sleep_int (optional, default 5).
#
# Use guide
# Type the following command into the terminal:
#
# python3 water_level.py <station_number> <start_date> <end_date>
# Date format: dd-mm-yyyy
#
# Example:	
# python3 water_level.py 20253 01-01-2018 01-01-2019

## Updates:
# * (21-01-2019) Added support for specifying the station number as input.
# * (15-03-2022) Fixed extra newline when saving file. Perhaps due to new
#                Python updates???

## Functionality
# Stealing water level measurements from DMI (2013): https://www.dmi.dk/hav/
# maalinger/vandstand/ 
#
# Water level is measured in reference to the danish vertical reference 1990 
# (DVR90) as the zero measurement in centimeters. Be aware that DMI forecast is 
# not included in this script!

# Data is scraped from DMI's servers by changing the date fraction of the
# URL: "http://servlet.dmi.dk/vandstand/servlet/ImageServlet?type=Vandstand&
# pres=csv&stat=20303&date=-"
#
# Date format is guessed from looking at the server response using different 
# date formats by trial and error. The server accepts dates in the format 
# "yyyymmdd". 
#
# To avoid flooding DMI's server with requests (if the server is flooded, the 
# response time increases significantly), this script sleeps for 'sleep_time' 
# sec. every 'sleep_int' days of data downloaded.

## List of stations
# Stationsnr.	Stationsnavn	Ansvarlig
# 20002	Skagen Havn	DMI
# 20003	Skagen Havn	Skagen Havn
# 20043/20047      	Hirtshals Havn	DMI
# 20049	Hirtshals Havn	Hirtshals Havn
# 20101/20102   	Frederikshavn Havn	DMI
# 20252/20253	Hals Barre Fyr	Ålborg Havn
# 20262	Hals Havn	Ålborg Havn
# 20299/20301	Grønlandshavnen	Ålborg Havn
# 20302/20303	Ålborg Øst	Ålborg Havn
# 20333	Haverslev Havn	Skive Kommune
# 20412	Rønbjerg Huse Havn	Vesthimmerland Kommune
# 20423	Løgstør Havn	Løgstør Havn
# 20566/20567	Hobro Havn	DMI
# 20676	Als Odde	Mariagerfjord Kommune
# 21009/21011	Hanstholm Havn	DMI
# 21058	Thisted Havn	Thisted Havn
# 21138	Nykøbing Mors Havn	Nykøbing Mors Havn
# 21191	Skive Havn	Skive Havn
# 22009	Udbyhøj Havn	DMI
# 22058/22059	Randers Havn	DMI
# 22121/22122	Grenå Havn	DMI
# 22331/22333	Århus Havn	DMI
# 22598/22599	Hov Havn	DMI
# 23126	Horsens Havn S	Horsens Vand
# 23128	Horsens Havn N	Horsens Havn
# 23132	Juelsminde Havn	DMI
# 23259	Vejle Havn	Vejle Havn
# 23289/23293	Fredericia Havn	DMI
# 23322	Kolding Havn	Kolding Havn
# 24006	Thyborøn Kyst	Kystdirektoratet
# 24007	Thyborøn Havn	Kystdirektoratet
# 24018	Ferring	Kystdirektoratet
# 24032	Lemvig Havn	Lemvig Havn
# 24053	Struer	Struer Kommune
# 24122/24125	Thorsminde Kyst	Kystdirektoratet
# 24123	Thorsminde Havn	Kystdirektoratet
# 24124	Thorsminde Fjord	Kystdirektoratet
# 24132	Felsted Kog/Klosterhul	Kystdirektoratet
# 24328	Ringkøbing Havn	Kystdirektoratet
# 24342	Hvide Sande Kyst	Kystdirektoratet
# 24343	Hvide Sande Havn	Kystdirektoratet
# 24344	Hvide Sande Fjord	Kystdirektoratet
# 24353	Bork Havn	Kystdirektoratet
# 25137	Grådyb Barre	Esbjerg Havn
# 25147	Esbjerg Havn	Kystdirektoratet
# 25149	Esbjerg Havn	DMI
# 25343/25344	Ribe Kammersluse	Kystdirektoratet
# 25346/25347	Mandø	Kystdirektoratet
# 26088/26089	Haderslev Havn	Kystdirektoratet
# 26136/26137	Havneby Havn	Kystdirektoratet
# 26143/26144	Brøns Sluse	Kystdirektoratet
# 26239	Åbenrå Havn	Åbenrå Havn
# 26346	Ballum Sluse	Kystdirektoratet
# 26359	Vidåslusen/Højer	DMI
# 26361	Vidåslusen/Højer	Kystdirektoratet
# 26457/26459	Fynshav Havn	DMI
# 26473/26474	Sønderborg Havn	Kystdirektoratet
# 27000	Svendborg	Svendborg Havn
# 27014	Vesterø Havn	Vesterø Havn
# 27084	Ballen Havn	DMI
# 28003/28004	Bogense Havn	Kystdirektoratet
# 28068	Odense Fjord	Odense Havn
# 28086	Odense Kanal Stige Ø	Beredskab Fyn
# 28087	Odense Fjord Stige Ø	Beredskab Fyn
# 28198/28199	Kerteminde Havn	Kystdirektoratet
# 28234	Slipshavn	DMI
# 28366/28367	Assens Havn	Kystdirektoratet
# 28397/28398	Fåborg Havn	Kystdirektoratet
# 28548	Bagenkop Havn	DMI
# 29002	Havnebyen/Sjællands Odde	DMI
# 29006	Rørvig Havn	Odsherred Havne
# 29014	Nykøbing Sjælland Havn	Odsherred Havne
# 29038/29039	Holbæk Havn	DMI
# 29141	Kalundborg Havn	Kalundborg Havn
# 29393/29394	Korsør Havn	DMI
# 30017	Hornbæk Havn	DMI
# 30042	Sletten Havn	Fredensborg Forsyning
# 30106	Frederiksværk Havn	Frederiksværk Kommune
# 30112	Hundested Havn	Halsnæs Forsyning
# 30119	Jægerspris Kignæs Havn	Frederikssund Kommune
# 30121	Kyndbyværket	Halsnæs Forsyning
# 30129	Frederikssund S	Frederikssund Forsyning
# 30202/30203	Vedbæk Havn	DMI
# 30336	Københavns Havn	DMI
# 30357	Drogden Fyr	DMI
# 30361/30363	Dragør Havn	DMI
# 30396	Hundige Havn	Klar Forsyning
# 30407/30409	Roskilde Havn	DMI
# 30478/30479	Køge Havn	DMI
# 31063	Rødvig Havn	DMI
# 31171/31172	Karrebæksminde	Kystdirektoratet
# 31243/31244	Kalvehave	Kystdirektoratet
# 31342/31343	Bandholm Havn	Kystdirektoratet
# 31417/31418	Nakskov	Lolland Kommune
# 31463	Sakskøbing Havn	Guldborgsund Kommune
# 31473	Guldborgsundtunnel Falster	Guldborgsund Kommune
# 31478	Guldborgsundtunnel Lolland    	Guldborgsund Kommune
# 31493/31494	Hesnæs Havn	Kystdirektoratet
# 31573	Rødbyhavns Havn	DMI
# 31616	Gedser Havn	DMI
# 32048	Tejn Havn	DMI
# 32096/32098	Rønne Havn	Kystdirektoratet

## HTML response
# The server responds with header and the water level measurements in this 
# form:
#
# dd. month year, station number and location
# hh:mm, water level
# hh:mm, water level
# ...
#
# Example
# 5. januar 2017,20303 Aalborg Øst II
# 00:00,60
# 00:20,61
# ...

from urllib.request import urlopen
import datetime
from datetime import date, timedelta
import re
import sys
import time

## Define start and end times.
# sys.argv = ["", "20002", "01-01-2018", "01-02-2018"] # For testing
station = sys.argv[1]
t1 = sys.argv[2]
t2 = sys.argv[3]

# Check if any extra arguments are specified.
if len(sys.argv) > 4:
    sleep_int  = sys.argv[4]
    sleep_time = sys.argv[5] # Time in seconds.
else:
    sleep_int  = 1000 
    sleep_time = 1 # Time in seconds.

# Split input strings into date vector readable for 'date'.
t1 = t1.split('-', 2)
t2 = t2.split('-', 2)

# Convert strings to 'date' format.
t1 = date(int(t1[2]), int(t1[1]), int(t1[0]))
t2 = date(int(t2[2]), int(t2[1]), int(t2[0]))

print(t1)
print(t2)

delta = t2 - t1 # Amount of days between t1 and t2.

## List with every day from t1 to t2 and append the html response.
t     = [] # yyyymmdd
t_str = [] # yyyy-mm-dd
html  = []

for i in range(delta.days + 1):
	# Define each day to 't' and remove anything other than digits.
	t = re.sub(r'\D', "", str(t1 + timedelta(days=i)))
	
	# Get the date strings for the 
	t_str.append(t1 + timedelta(days=i)) 
	
	url = ("http://servlet.dmi.dk/vandstand/servlet/ImageServlet?"
	       "type=Vandstand&pres=csv&stat={0}&date={1}".format(station, t))
	response = urlopen(url)
	html.append(response.read())

	# Print progress on the same line.
	print(("{0} downloaded out of {1} " 
	       "days of data for station: {2}. " 
		   "Sleep for {3} sec every {4} days.\r".format(str(i + 1), 
		   str((delta.days + 1)), str(station), str(sleep_time), 
		   str(sleep_int))))
    
	# If 'sleep_int' days of records have been downloaded, sleep for 
    # 'sleep_time' sec (trying to prevent DMI's server to block us when 
    # sending too many requests too fast).
	if (i + 1) % int(sleep_int) == 0:
		time.sleep(float(sleep_time)) # Time in seconds.
        
# Terminate with an empty line.
print("")

## Remove header line.
html_i_tmp = []
for i in range(len(html)):
	html[i] = re.sub('.*\r\n', '', html[i].decode('ISO-8859-1'), count=1) # Remove header line
	html[i] = re.sub('.*(?=\d{2}:)', str(t_str[i]) + " ", html[i])        # Insert date
	html_i_tmp.append(html[i].split("\r\n")[:-1])                         # Split by linebreak and remove last "empty" line

# "Flatten" entries for easier access when writing to disk
flat_list = [item for sublist in html_i_tmp for item in sublist]

## Write data to text file.
with open('water_level_{0}.txt'.format(station), 'w') as outfile:
	for i in flat_list:
		outfile.write(i + "\n")

# DEBUG
"""
import matplotlib.pyplot as plt
import numpy as np

## Read the new data
# Load water levels
data        = np.genfromtxt('water_level_{0}.txt'.format(station), 
              delimiter=',')
water_level = data[:,][:, 1]

# Load the date strings
date = np.loadtxt("water_level.txt", delimiter=",", usecols=(0,0), 
       dtype=object, converters={0: lambda x: datetime.strptime(
       x.decode('ISO-8859-1'), "%Y-%m-%d %H:%M")})

time = date[:,][:, 0]

# Plot the time series
plt.plot(time, water_level, color='r', label='the data')
plt.gcf().autofmt_xdate()
plt.show()
"""
