from pyinrail import pyinrail
import pytesseract

import pandas as pd
from datetime import datetime, timedelta

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

current_time = datetime.now().strftime("%H:%M")


# print(current_time)


def get_three_with_time_station_trains(from_station, middle_station, to_station, departure_date, additional_time,
                                       buffer):
    # print(from_station, middle_station, to_station, departure_date, '0000000000000000000')
    result = []
    from_station, middle_station, to_station = from_station.upper(), middle_station.upper(), to_station.upper()
    modified_from_station = from_station.split(' - ')[0]
    modified_middle_station = middle_station.split(' - ')[0]
    modified_to_station = to_station.split(' - ')[0]

    user_input = [modified_from_station, modified_middle_station, modified_to_station]
    # print(user_input)
    enq = pyinrail.RailwayEnquiry(src=modified_from_station, dest=modified_to_station, date=departure_date)
    trains_between_stations = enq.get_trains_between_stations(as_df=True)
    if type(trains_between_stations) is str:
        return trains_between_stations
    # print(trains_between_stations)
    # selected_row = trains_between_stations.loc[trains_between_stations['departureTime'] > current_time]
    train_numbers_between_stations = trains_between_stations['trainNumber']

    for train in train_numbers_between_stations:
        df = enq.get_train_schedule(train, as_df=True)

        stations_name_of_a_name = df['stationName']
        # print(df)
        for station_name in stations_name_of_a_name:
            if station_name == modified_middle_station:
                # test = trains_between_stations.loc[trains_between_stations['stationName'] == modified_middle_station]

                target_train_data = trains_between_stations.loc[trains_between_stations['trainNumber'] == train]
                # print(target_train_data)
                # print(df)
                time_obj = datetime.strptime(additional_time, "%H:%M")
                new_time_obj = time_obj + timedelta(hours=buffer)
                new_time_str = new_time_obj.strftime("%H:%M")
                print(new_time_str)
                selected_row = target_train_data.loc[target_train_data['departureTime'] > new_time_str]
                if selected_row.empty:
                    print('selected_row')
                else:
                    print(selected_row)
                    result.append(selected_row)

    return result
