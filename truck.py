# Author:        Bryan Yang
# Student ID:    #001303738
# Major:         B.S. Computer Science. Started 10/1/22
# Email:         byang10@wgu.edu
# Date:          12/3/22

import csv
from hashmap import *
from package import *


# Truck class for delivery class.
class Truck:

    # Initiate Contractor with variables.
    def __init__(self, truckId):
        self.tk_id = truckId
        self.pk_list = HashMap()
        self.tk_departure_time = 0
        self.travel = 0
        self.total_cost = 0

    # Get package for trucks.
    # Set package departure_time per truck tk_departure_time to deliver pacakge.
    # Big-O Notation: O(1) O(n^2)
    def get_package(self, id):
        with open('WGUPS Package File.csv', 'r') as csv_package:
            read_csv = csv.reader(csv_package, delimiter=',')

            for col in read_csv:
                pk = Package(int(col[0]), col[1], col[2], col[3], col[4], col[5], col[6], col[7])
                if id == pk.pk_id:
                    self.pk_list.insert(pk)

            for i in self.pk_list.hashMap:
                for j in i:
                    if self.tk_id == 1:
                        j.departure_time = self.tk_departure_time
                    elif self.tk_id == 2:
                        j.departure_time = self.tk_departure_time
                    elif self.tk_id == 3:
                        j.departure_time = self.tk_departure_time

        return self.pk_list

    # Set truck travel time.
    # Big-O Notation: O(1)
    def set_travel_time(self, distance):
        self.travel = round(3.33 * distance) + self.tk_departure_time
