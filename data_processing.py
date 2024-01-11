
from vehicles_table import vehicles_dataframe_reader
from trips_table import trips_dataframe_reader
from stops_table import stops_dataframe_reader
from stop_times_table import stop_times_dataframe_reader
from routes_table import routes_dataframe_reader
from weather_table import weather_dataframe_reader

vehicles_dataframe = vehicles_dataframe_reader.load()
trips_dataframe = trips_dataframe_reader.load()
stops_dataframe = stops_dataframe_reader.load()
stop_times_dataframe = stop_times_dataframe_reader.load()
routes_dataframe = routes_dataframe_reader.load()
weather_dataframe = weather_dataframe_reader.load()

def load_dataframes():
    # put your code here
    vehicles_dataframe = vehicles_dataframe_reader.load()
    trips_dataframe = trips_dataframe_reader.load()
    stops_dataframe = stops_dataframe_reader.load()
    stop_times_dataframe = stop_times_dataframe_reader.load()
    stop_times_dataframe.show()
    routes_dataframe = routes_dataframe_reader.load()
    weather_dataframe = weather_dataframe_reader.load()
    weather_dataframe = weather_dataframe.dropDuplicates().select("timestamp", "temperature", "humidity").orderBy("timestamp")
    return weather_dataframe





