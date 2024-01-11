from data_processing import load_dataframes
import threading


def run_load():
    thread = threading.Timer(60.0, run_load)  # 60 seconds = 1 minute
    thread.start()
    vehicles_dataframe, weather_dataframe = load_dataframes()
    vehicles_dataframe.show(100)
    weather_dataframe.show()

run_load()
