#!/usr/bin/python3
"""Messaging Class"""

class Message:
    """Message class creation"""
    def __init__(self, user_id, sender_id, receiver_id, message_content, sent_at=None):
        self.user_id = user_id # unique identifier for the message (primary key)
        self.sender_id = sender_id # foreign key linking to the user model
        self.receiver_id = receiver_id # Foreign key linking to the user model
        self.message_content = message_content # Message Content
        self.sent_at = sent_at or datetime.now() # Time stamp of when the message was sent

        def save_to_db(self):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO messages (user_id, sender_id, receiver_id, message_content, sent_at) VALUES (%s, %s, %s, %s, %s)",
                        (self.self_id, self.sender_id, self.receiver_id, self.message_content, self.sent_at))
        mysql.connection.commit()
        cursor.close()