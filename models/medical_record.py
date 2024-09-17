#!usr/bin/python3
"""Medical Record class"""

import datatime


class MedicalRecord:
    """ Medical record creation"""
    def __init__(self, user_id, record_type, record_data, created_at=None):
        self.user_id = user_id
        self.record_type = record_type
        self.record_data = record_data
        self.created_at = created_at or datatime.now()

    def save_to_db(Self):
        """ Saving the record the the database"""
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO medical_records (user_id, record_type, record_data, created_at) VALUES (%s, %s, %s, %s)", 
                        (self.user_id, self.record_type, self.record_data, self.created_at))
        mysql.connection.commit()
        cursor.close()