import sys

class TravelBooking:
    # Overall class to manage travel bookings
    def __init__(self):
        self.booking = {}

    def add_booking(self, name, destination):
        self.booking[name] = destination

    def get_booking(self, name):
        return self.booking.get(name)

    def list_bookings(self):
        return self.booking

    def remove_booking(self, name):
        if name in self.booking:
            del self.booking[name]
            return True
        return False
    
if __name__ == '__main__':
    tb = TravelBooking()