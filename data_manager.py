import requests

SHEETY_API = "https://api.sheety.co/f50e4ea2e3849db065f4e33dca7b951c/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.response = requests.get(url=SHEETY_API)
        self.sheet_data = self.response.json()

    def sheety_data(self):
        return self.sheet_data["prices"]

