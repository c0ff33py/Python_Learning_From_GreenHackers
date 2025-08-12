from datetime import datetime

class User:
    def __init__(self, name):
        self.name = name 
        self.inbox = [] # store received messages

    def send_message(self, chatroom, message):
        """Send message to the chatroom"""
        chatroom.broadcast_message(self, message)

    def receive_message(self, sender, message):
        """Receive message from other users"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.inbox.append((sender.name, message, timestamp))

    def show_inbox(self):
        """Display all received messages"""
        if not self.inbox:
            print(f"📭 {self.name}'s inbox is empty.")
        else:
            print(f"\n✉️ {self.name}'s Inbox:")
            for sender, message, time in self.inbox:
                print(f"[{time}] {sender}: {message}")

class ChatRoom:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        """Add user to chatroom"""
        self.users.append(user)
    
    def broadcast_message(self, sender, message):
        """Send message to all users except sender"""
        for user in self.users:
            if user != sender:
                user.receive_message(sender,message)

# ============Simulation==========
chatroom = ChatRoom()

# Create Users
alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")

# Add them to chatroom
chatroom.add_user(alice)
chatroom.add_user(bob)
chatroom.add_user(charlie)

# Send some messages
alice.send_message(chatroom, "Hello, everyone! 🙂")
bob.send_message(chatroom, "Hey Alice! How are you?")
charlie.send_message(chatroom, "Hi all! What's up?")

# View inboxes
alice.show_inbox()
bob.show_inbox()
charlie.show_inbox()