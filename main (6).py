from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
usersurl = "https://api.sheety.co/30c62f467aac2927a0d958d82fdd2214/flightDeals/users"
header = {"Authorization":"Bearer jjdhbSJy8847ssSHajS"}
#for row in sheet_data:
#    city_name = row["city"]
#    codes = flight_search.get_destination_code(city_name)
#    row['iataCode'] = codes
#    print(row)
#    data_manager.update_destination_code(row)

def details():
  global fname,lname,email
  fname = input("Enter First Name : ")
  lname = input("Enter Last Name : ")
  while True:
    email = input("Enter Email : ")
    cemail = input("Confirm Email : ")
    if email == cemail and '@' in email:
      break
    else:
      print('------> Invalid Email Credentials')
  response = requests.get(url=usersurl,headers=header).json()['users']
  
  if any(row['firstName'] == fname and row['lastName'] == lname for row in response):
    print('----> Name already registered')
  elif any(row['email'] == email for row in response):
    print('----> Email already registered')
  else:
    params = {'user':{'firstName':fname,'lastName':lname,'email':email}}
    response = requests.post(url=usersurl,json=params,headers=header)
    print('\nNew account successfully created')
    print("WELCOME TO THE FLIGHT CLUB ! ")
    3
details()

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )
    if flight is None:
      flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today,
        stop_overs=1
      )
      if flight is None:
        continue
      elif flight.price < destination['lowestPrice']:
        print(f'---> LOW PRICE ALERT ! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."')
        print(f'\n1 stopover,via {flight.via_city}')
        '''
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
        '''
      else:
        pass
    elif flight.price < destination["lowestPrice"]:
        print('---> LOW PRICE ALERT !')
        '''
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
        '''
    else:
      pass
