import requests
from datetime import datetime
from collections import defaultdict
from operator import itemgetter
from math import ceil

def get_stations(source_station):
    """This function fetches all the available stations in the BART API

    Args:
        source_station (string): takes abbriviation of the source station

    Returns:
        [list]: list of all the available [stations abbr, station name] in the BART API
    """
    URL = "http://api.bart.gov/api/stn.aspx"  
    PARAMS = {"cmd":"stns","key":"MW9S-E7SL-26DU-VV8V","json":"y"} 

    res = requests.get(url = URL, params = PARAMS) 
    station_list = []
    for stn in res.json()["root"]["stations"]["station"]:
        station_list.append([stn["abbr"],stn["name"]])
        
    return station_list
        
def get_trains_per_station(source_station):
    """Takes the source station and returns all the next 2 deperture time
     from current station to all the source station

    Args:
        source_station (string): takes abbriviation of the source station

    Returns:
        list of list, current_station_name: [["station name", datetime of deperture]......], and current station name
    """
    schedule_inventory = []

    stations = get_stations(source_station)
    current_station_name = None

    for station in stations:
        if station[0] == source_station:
            current_station_name = station[1]
            continue
        PARAMS = {'cmd':'depart','orig':source_station,'dest':station[0],'date':'now','key':'MW9S-E7SL-26DU-VV8V','b':'0','a':'2','l':'1','json':'y'}
        URL = "http://api.bart.gov/api/sched.aspx"  
        res = requests.get(url = URL, params = PARAMS) 
        try:
            for trip in res.json()['root']['schedule']['request']['trip']:
                deperture_time = trip["@origTimeDate"]+" "+trip["@origTimeMin"]

                schedule_inventory.append([station[1], datetime.strptime(deperture_time, '%d/%m/%Y %H:%M %p')])
        except Exception as e:
            print(e)

    schedule_inventory = sorted(schedule_inventory,key=itemgetter(1))
    return schedule_inventory, current_station_name

def display(schedule_inventory, current_station_name):
    """prints the deperture time and destinion station name

    Args:
        schedule_inventory ([[]]): take lis of list of format [["station name", deperture time]]
        current_station_name (string): current station name
    """
    print("-"*20)
    print(f"Welcome to {current_station_name}")
    print("-"*20)
    table_row_format = "{:15} min       {:20}"
    print(table_row_format.format("Deperting in", "Destination"))
    now = datetime.now()
    for station, dept_time in schedule_inventory[:10]:
        dept_time_left = dept_time - now
        print(table_row_format.format(ceil(dept_time_left.seconds/60), station))

if __name__ == "__main__":
    time_table_inventory, current_station_name = get_trains_per_station("MONT")
    display(time_table_inventory, current_station_name)




