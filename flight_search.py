from data_manager import DataManager


class FlightSearch:
    def __init__(self, sheet):
        self.sheet_data = sheet
        # self.city_name = [DataManager().sheet_data()[i]["city"] for i in range(0, len(DataManager().sheet_data()))]

    def iata_respose(self):
        for i in self.sheet_data:
            i['iataCode'] = "testing"
        return self.sheet_data
    #This class is responsible for talking to the Flight Search API.
