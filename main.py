import numpy as np

from data_processing import load_dataframes
import threading
from plotting import plot
from datetime import datetime as dt
import pandas as pd

def run_load():
    thread = threading.Timer(60.0, run_load)  # 60 seconds = 1 minute
    thread.start()
    vehicles_dataframe, weather_dataframe = load_dataframes()

    weather_timestamp_list = weather_dataframe.select("timestamp").collect()
    weather_timestamp_list = [int(dt.timestamp(x.__getitem__("timestamp"))) for x in weather_timestamp_list]
    #plot for temperature
    # plot(weather_timestamp_list, weather_dataframe.select("temperature").collect(), "timestamp", "temperature", "temperature based on timestamps", 1)
    #plot for humidity
    # plot(weather_timestamp_list, weather_dataframe.select("humidity").collect(), "timestamp", "temperature","humidity based on timestamps", 2)

    # vehicles_dataframe.show(10000, truncate= False)
    # print(len(vehicles_dataframe.select("timestamp").collect()))

    vehicles_timestamp_list = vehicles_dataframe.select("timestamp").collect()
    vehicles_timestamp_list = [int(dt.timestamp(x.__getitem__("timestamp"))) for x in vehicles_timestamp_list]

    vehicles_speed_list = vehicles_dataframe.select("speed").collect()
    vehicles_speed_list = [int(x.__getitem__("speed")) for x in vehicles_speed_list]

    print(len(vehicles_timestamp_list))
    print(len(vehicles_speed_list))

    #plot for speed
    plot(vehicles_timestamp_list, vehicles_speed_list, "timestamp", "km/h", "speed based on timestamps", 3)

run_load()
