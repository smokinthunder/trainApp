from pyinrail import pyinrail
import pytesseract
import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
current_time = datetime.datetime.now().strftime("%H:%M")


def get_two_station_trains(from_station, to_station, departure_date):
    print(departure_date, 'from')
    modified_from_station = from_station.split(' - ')[0]
    modified_to_station = to_station.split(' - ')[0]
    user_input = [modified_to_station, to_station]

    enq = pyinrail.RailwayEnquiry(src=from_station, dest=to_station, date=departure_date)
    trains_between_stations = enq.get_trains_between_stations(as_df=True)

    if type(trains_between_stations) is str:
        return trains_between_stations
    # print(trains_between_stations)
    else:
        selected_row = trains_between_stations.loc[trains_between_stations['departureTime'] > current_time]
        train_numbers_between_stations = trains_between_stations['trainNumber']

        for train in train_numbers_between_stations:
            df = enq.get_train_schedule(train, as_df=True)

            stations_name_of_a_name = df['stationName']
            for station_name in stations_name_of_a_name:
                # print(station_name)

                if station_name == user_input[0]:
                    # print(train)
                    target_train_data = trains_between_stations.loc[trains_between_stations['trainNumber'] == train]
                    # print(target_train_data)

                    return target_train_data


# print(get_trains())


def get_three_station_trains(from_station, middle_station, to_station, departure_date):
    print(from_station, middle_station, to_station, departure_date, '0000000000000000000')
    result = []
    from_station, middle_station, to_station = from_station.upper(), middle_station.upper(), to_station.upper()
    modified_from_station = from_station.split(' - ')[0]
    modified_middle_station = middle_station.split(' - ')[0]
    modified_to_station = to_station.split(' - ')[0]

    user_input = [modified_from_station, modified_middle_station, modified_to_station]
    print(user_input)
    enq = pyinrail.RailwayEnquiry(src=modified_from_station, dest=modified_to_station, date=departure_date)
    trains_between_stations = enq.get_trains_between_stations(as_df=True)
    if type(trains_between_stations) is str:
        return trains_between_stations
    # print(trains_between_stations)
    selected_row = trains_between_stations.loc[trains_between_stations['departureTime'] > current_time]
    train_numbers_between_stations = trains_between_stations['trainNumber']

    # for train in train_numbers_between_stations:
    #     df = enq.get_train_schedule(train, as_df=True)
    #     print(df)
    #     stations_name_of_a_name = df['stationName']
    #     for station_name in stations_name_of_a_name:
    #         # print(station_name)
    #         if station_name == modified_middle_station:
    #             # print(train)
    #             target_train_data = trains_between_stations.loc[trains_between_stations['trainNumber'] == train]
    #             # print(target_train_data)
    #             return target_train_data

    for train in train_numbers_between_stations:
        df = enq.get_train_schedule(train, as_df=True)
        stations_name_of_a_name = df['stationName']
        for station_name in stations_name_of_a_name:
            # print(station_name)
            if station_name == modified_middle_station:
                target_train_data = trains_between_stations.loc[trains_between_stations['trainNumber'] == train]
                print(target_train_data)
                result.append(target_train_data)
    return result[0:]
