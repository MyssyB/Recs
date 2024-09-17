#!/usr/bin/python3
"""Appointment Class"""


class Appointment:
    """Appointment creation class"""
    def __init__(self, user_id, doctor_id, appointment_date, status="scheduled"):
        self.user_id = user_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status = status
        
    def save_to_db(self):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO appointments (user_id, doctor_id, appointment_date, status) VALUES (%s, %s, %s, %s)",
                        (self.user_id, self.doctor_id, self.appointment_date, self.status))
        mysql.connection.commit()
        cursor.close()