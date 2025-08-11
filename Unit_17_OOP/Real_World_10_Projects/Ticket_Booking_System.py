# Ticket Booking System
# Author: c0ff33py
# Description: Simple console_based ticket booking system using OOP.

# Event class - Represents an event that has tickets to sell

class Event:
    def __init__(self, name, total_seats, price):
        self.name = name # Event name(string)
        self.total_seats = total_seats # Total seats available(integer)
        self.price = price # Price per ticket(float)
        self.booked_seats = 0 # Number of seats already booked

    # Method to check available seats
    def avaliable_seats(self):
        return self.total_seats - self.booked_seats
    
    # Method to book tickets
    def book_ticket(self, quantity):
        if quantity <= 0:
            return "❌ Invalid quantity."
        if quantity > self.avaliable_seats():
            return f"❌ Only {self.available_seats()} seats left."
        
        self.booked_seats += quantity
        total_cost = quantity * self.price
        return f"✅ {quantity} ticket(s) canceled for {self.name}."
    
    # Method to cancel tickets
    def cancel_ticket(self, quantity):
        if quantity <= 0:
            return "❌ Invalid quantity."
        if quantity > self.booked_seats:
            return f"❌ You only have {self.booked_seats} booked tickets to cancel."
        
        self.booked_seats -= quantity
        return f"✅ {quantity} ticket(s) canceled for {self.name}."
# TicketBookingSystem class - Manages multiple events
class TicketBookingSystem:
    def __init__(self):
        self.events = [] # Stores all events

    # Add a new event
    def add_event(self, event):
        self.events.append(event)
        print(f"Event '{event.name}' added with {event.total_seats} seats at ${event.price} each.")

    # Show all events
    def show_events(self):
        if not self.events:
            print("❌ No events available.") 
        else:
            print("\n Available Events: ")
            for idx, event in enumerate(self.events, start=1):
                print(f"{idx}. {event.name} - ${event.price} | Seats left: {event.avaliable_seats()}")



# --------------------------Main Program------------------
if __name__ == "__main__":
    system = TicketBookingSystem()

    # Create and add events 
    concert = Event("AC/DC Rock Concert",50 , 20)
    movie = Event("Avengers: Endgame", 100, 30)

    system.add_event(concert)
    system.add_event(movie)

    # Display Events
    system.show_events()

    # Booking tickets
    print(concert.book_ticket(3))
    print(movie.book_ticket(5))

    # Cancel tickets
    print(movie.cancel_ticket(2))

    # Show updated events
    system.show_events()
    
    
    