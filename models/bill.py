class Bill:
    def __init__(self, user_id, amount_due, due_date, status):
        self.user_id = user_id
        self.amount_due = amount_due
        self.due_date = due_data
        self.status = status

    def save_to_db(self):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO appointments (user_id, amount_due, due_date, status) VALUES (%s, %s, %s, %s)",
                        (self.user_id, self.amount_due, self.due_date, self.status))
        mysql.connection.commit()
        cursor.close()