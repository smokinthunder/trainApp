from pyinrail import pyinrail
import pytesseract
import datetime
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get the current date
current_date = datetime.date.today()

# Calculate the ARP date by adding a certain number of days to the current date
arp_date = current_date + datetime.timedelta(days=0)  # Adjust the number of days as needed
print(arp_date)

# Convert the ARP date to the required format
arp_date_str = arp_date.strftime("%d-%m-%Y")

# Create a list of stations
stations = ['KOLLAM JN', 'TAMBARAM', 'CHENNAI EGMORE']  # Add the additional station here

# Perform a railway enquiry
enq = pyinrail.RailwayEnquiry(src=stations[0], dest=stations[-1], date=arp_date_str)
df = enq.get_trains_between_stations(as_df=True)
station_name = enq.stations
# print(station_name)
print(df)

# # Filter the DataFrame to get trains passing through Alappuzha
# list_trains = df[df['Stations'].str.contains('Alappuzha', case=False)]
#
# # Convert 'Departure_Time' column to datetime.time objects
# list_trains['Departure_Time'] = pd.to_datetime(list_trains['Departure_Time'], format='%H:%M').dt.time
#
# # Find the train with departure time closest to 11 am
# target_time = datetime.time(11, 0)  # Desired time: 11 am
# closest_train = list_trains.iloc[(list_trains['Departure_Time'] - target_time).abs().argsort()[0]]
#
# # Print the details of the train
# print("Train Details:")
# print("Train Number:", closest_train['Train_Number'])
# print("Train Name:", closest_train['Train_Name'])
# print("Departure Time:", closest_train['Departure_Time'])
