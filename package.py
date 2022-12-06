# Author:        Bryan Yang
# Student ID:    #001303738
# Major:         B.S. Computer Science. Started 10/1/22
# Email:         byang10@wgu.edu
# Date:          12/3/22

# Package Class for truck class.
class Package:

    # Initiate Contractor with variables.
    def __init__(self, pk_id, address, city, state, zip, deadline, weight, notes):
        self.pk_id = pk_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.delivery_status = 'Hub'
        self.departure_time = 0
        self.delivery_time = 0
        self.time = 0
        self.update_status = None

    # Print packages' status that are 'not_loaded' on a truck at hub.
    # Big-O Notation: O(1)
    def not_loaded(self):
        return print('Package:', self.pk_id, '|', self.address, '|', self.deadline, '|', self.city, '|', self.state, '|', self.zip, '|', self.weight, '|', self.delivery_status)

    # Print packages' status that are 'loaded' on a truck at hub.
    # Big-O Notation: O(1)
    def loaded(self):
        return print('Package:', self.pk_id, '|', self.address, '|', self.deadline, '|', self.city, '|', self.state, '|', self.zip, '|', self.weight, '|', 'Loaded')

    # Print packages' status that are 'out_for_delivery.'
    # Big-O Notation: O(1)
    def out_for_delivery(self):
        return print('Package:', self.pk_id, '|', self.address, '|', self.deadline, '|', self.city, '|', self.state, '|', self.zip, '|', self.weight, '|', 'Out For Delivery')

    # Time Conversion: Hour(s) to Minute(s).
    # Big-O Notation: O(1)
    def hr_to_mn(self, time):
        t = time.split(':')
        mn = (int(t[0]) * 60) + int(t[1])
        return mn

    # Time Conversion: Minute(s) to Hour(s).
    # Usage: Delivery status update with timestamp.
    # Big-O Notation: O(1)
    def set_delivered(self):
        hr = int(self.delivery_time / 60)
        mn = int(self.delivery_time % 60)
        self.time = str(hr) + ":" + str(mn).zfill(2)
        self.update_status = 'Delivered Time: ' + self.time

    # Update package delivery time in Minutes using miles traveled.
    # Big-O Notation: O(1)
    def set_timestamp(self, distance):
        self.delivery_time = round(3.33 * distance) + self.departure_time
        # Multiply Traveling Speed(3.33) with Minute Rate(Distance), then Add Departure_Time.

    # Package Status by Time in Minutes.
    # Big-O Notation: O(1)
    def lookup(self, mn):
        mn = self.hr_to_mn(mn)

        if mn < 480:
            self.not_loaded()

        elif 480 <= mn and mn < self.departure_time:
            self.loaded()

        elif self.departure_time <= mn and mn < self.delivery_time:
            self.out_for_delivery()

        elif mn >= self.delivery_time:
            print('Package:', self.pk_id, '|', self.address, '|', self.deadline, '|', self.city, '|', self.state, '|', self.zip, '|', self.weight, '|', self.update_status)

