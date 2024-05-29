from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/30c62f467aac2927a0d958d82fdd2214/flightDeals/prices"
header = {"Authorization":"Bearer jjdhbSJy8847ssSHajS"}
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,headers=header).json()
        print(response)
        data = response.json()['price']
        self.destination_data = data
        return self.destination_data

    def update_destination_code(self,city):
        self.new_data = {
            "price": {
                "iataCode": city["iataCode"]
            }
        }
        response = requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
            json=self.new_data,headers=header
        )
        response.raise_for_status()
        print(response.text)
