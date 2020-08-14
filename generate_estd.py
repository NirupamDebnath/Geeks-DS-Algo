import requests
import abc
import sys
from traceback import print_exc
from operator import attrgetter

class AbstractTrain():
    def __init__(self, minutes, platform, destination):
        self.dsestination = destination
        self.minutes = minutes
        self.platform = platform

    @abc.abstractmethod
    def __str__(self):
        pass

class Train(AbstractTrain):

    def __init__(self, minutes, platform, destination):
        super(Train, self).__init__(minutes, platform, destination)

    def __str__(self):
        return f"{self.minutes:>17} min | {self.platform:>10} | {self.dsestination:>20}"


class DepertureTable():

    def __init__(self, station_code="MONT",
                api_key="MW9S-E7SL-26DU-VV8V", 
                url="http://api.bart.gov/api/etd.aspx"):

        self.train_table_list     = []
        self.station_code         = station_code
        self.api_key              = api_key
        self.url                  = url
        self.name                 = None
    
    def get_api_data(self):
        try:
            response = requests.get(self.url, {
                                            'cmd': 'etd',
                                            'orig': self.station_code,
                                            'key': self.api_key,
                                            'json': 'y'
                                        })

            return response.json()
            
        except Exception: 
            print_exc(file=sys.stdout)
            sys.exit(1)

    def populate_table(self,api_data_dict):
        station   = api_data_dict["root"]["station"][0]
        self.name = station["name"]

        for etd in station["etd"]:
            for estimate in etd["estimate"]:
                minutes = estimate["minutes"]
                minutes = 0 if minutes.lower() =="leaving" else int(minutes)
                platform = estimate["platform"]
                destination = etd["destination"]

                train = Train(minutes, platform, destination)

                self.train_table_list.append(train)

    def display(self):
        api_data_dict = self.get_api_data()
        self.populate_table(api_data_dict)
        self.train_table_list = sorted(self.train_table_list, key = attrgetter("minutes"))

        print("="*60)
        print("{:^60}".format("Welcome to the"+self.name))
        print("="*60)
        print("{:>15} (min) | {:>10} | {:>20}".format("Departing In", "Platform", "Destination"))
        print("-"*60)

        for train in self.train_table_list[:10]:
            print(train)

if __name__ == "__main__":
    table_obj = DepertureTable()
    table_obj.display()