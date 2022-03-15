# Scrape water levels from DMI's sensor network

## Description

Downloads sea water levels from DMI's sensor network.

### Input

* station:    Station number of the station from which the data is downloaded.
* starttime:  Start date of the requested data in this date format 'dd-mm-yyyy'
* endtime:    Start date of the requested data in this date format 'dd-mm-yyyy'
* sleep_int:  Interval between downloads of records (optional, default 50)
* sleep_time: Pause in seconds between each sleep_int (optional, default 5).

### User guide
Type the following command into the terminal:

python3 water_level.py <station_number> <start_date> <end_date>
Date format: dd-mm-yyyy

Example:        
python3 water_level.py 20253 01-01-2018 01-01-2019
