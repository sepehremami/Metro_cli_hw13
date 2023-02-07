class Trip:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.available = True

    def register_trip(self):
        if self.available:
            self.available = False
            print("Trip registered successfully!")
        else:
            print("This trip is not available for registration.")
    def make_unavailable(self):
        self.available = False

    def is_available(self):
        return self.available
    
class Admin:
    def __init__(self):
        self.trips = []

    def register_trip(self, start_time, end_time):
        trip = Trip(start_time, end_time)
        self.trips.append(trip)

    def arrive_at_destination(self, trip_index):
        trip = self.trips[trip_index]
        trip.make_unavailable()
        
import datetime

class Trip:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.index = None
        self.available = True
    
    def set_index(self, index):
        self.index = index
        
    def mark_unavailable(self):
        self.available = False
        
    def __repr__(self):
        return f'Trip(start_time={self.start_time}, end_time={self.end_time}, index={self.index}, available={self.available})'

class TripManagement:
    def __init__(self):
        self.trips = []
        self.current_index = 0
        
    def add_trip(self, trip):
        self.trips.append(trip)
        trip.set_index(self.current_index)
        self.current_index += 1
        
    def register_trip(self, index):
        trip = self.trips[index]
        if trip.available:
            trip.mark_unavailable()
            print(f'Trip with index {index} has been registered and is no longer available.')
        else:
            print(f'Trip with index {index} is not available.')
            
    def list_trips(self):
        for trip in self.trips:
            print(trip)






