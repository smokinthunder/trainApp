# from pyinrail import pyinrail
# import pytesseract
# import datetime
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# # Get the current date
# current_date = datetime.date.today()
#
# # Calculate the ARP date by adding a certain number of days to the current date
# arp_date = current_date + datetime.timedelta(days=0)  # Adjust the number of days as needed
# print(arp_date)
# # Convert the ARP date to the required format
# arp_date_str = arp_date.strftime("%d-%m-%Y")
#
# enq = pyinrail.RailwayEnquiry(src='Trivandrum', dest='ahmedabad', date=arp_date_str)
#
# df = enq.get_trains_between_stations(as_df=True)
# print(df)


# //---------------------------------------------------------/

from pyinrail import pyinrail
import pytesseract
import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get the current date
current_date = datetime.date.today()

# Calculate the ARP date by adding a certain number of days to the current date
arp_date = current_date + datetime.timedelta(days=0)  # Adjust the number of days as needed
print(arp_date)

# Convert the ARP date to the required format
arp_date_str = arp_date.strftime("%d-%m-%Y")

# Create a list of stations
stations = ['Kannur', 'Alappuzha', 'Trivandrum']  # Add the additional station here

enq = pyinrail.RailwayEnquiry(src=stations[0], dest=stations[-1], date=arp_date_str)

df = enq.get_trains_between_stations(as_df=True)
# print(df['departureTime'])

current_time = datetime.datetime.now().strftime("%H:%M")
# greater_times = [time for time in df['departureTime'] if time > current_time]
# print(greater_times)
selected_row = df.loc[df['departureTime'] > current_time]

print(selected_row)

