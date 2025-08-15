# Project 10: Ride Booking System
import random

class RideBookingSystem:
    def __init__(self):
        self.drivers = []
        self.rides = []

    def add_driver(self, name, vehicle, plate):
        """Register a new driver"""
        self.drivers.append({
            "name": name,
            "vehicle": vehicle,
            "plate": plate
        })
        print(f"✅ Driver {name} added.")
    
    def calculate_fare(self, distance_km, rate_per_km=2.0):
        """Calculate fare based on distance"""
        return distance_km * rate_per_km
    
    def book_ride(self, passenger, pickup, drop, distance_km):
        """Book a ride for a passenger"""
        if not self.drivers:
            print('❌ No drivers available.')
            return
        # Randomly assign a driver
        driver = random.choice(self.drivers)

        # Calculate fare
        fare = self.calculate_fare(distance_km)

        # Save ride details
        ride_info = {
            "passenger" : passenger,
            "pickup": pickup,
            "drop" : drop,
            "driver":driver["name"],
            "vehicle": driver["vehicle"],
            "plate": driver["plate"],
            "fare": fare
        }
        self.rides.append(ride_info)

        print(f"\n🚗 Ride Confirmed!")
        print(f"Passenger: {passenger}")
        print(f"Pickup: {pickup}")
        print(f"Drop: {drop}")
        print(f"Driver: {driver['name']} ({driver['vehicle']} - {driver['plate']})")
        print(f"Fare: ${fare:.2f}")

    def view_history(self):
        """View all past rides"""
        if not self.rides:
            print("No ride history.")
            
        print("\n Ride History:")
        for idx, ride in enumerate(self.rides, start=1):
            print(f"{idx}. {ride['passenger']} | {ride['pickup']} -> {ride['drop']} | ${ride['fare']:.2f}")
            
#--------- Example usage -------
system = RideBookingSystem()
system.add_driver("John", "Car", "ABC123")
system.add_driver("Emma", "Motorbike", "XYZ789")

system.book_ride("Alex", "Downtown", "Airpot", 15)
system.book_ride("Mia", "Mall", "Home", 8)

system.view_history()
        
        
                
        