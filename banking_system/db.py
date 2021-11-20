"""Manage DB for BankingSystem class"""
import sqlite3
import os
from card_number import generate_card, generate_password


class BankingDB:
    """Creates db, creates table, inserts/updates/deletes data"""
    db_name = 'card.s3db'

    def __init__(self):
        self.db_create_cards_table()

    def db_create_cards_table(self):
        """Creates db if not exists"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS cards(
        id INTEGER PRIMARY KEY NOT NULL,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0 )''')
        dbase.commit()
        dbase.close()

    def db_create_account(self, number, pin):
        """Inserts new account row in 'cards' table"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(f''' INSERT INTO cards (number, pin) VALUES ({number}, {pin})''')
        dbase.commit()
        dbase.close()

    def db_select_all(self):
        """Selects and prints all from 'cards' table"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(''' SELECT * FROM cards''')
        result = cursor.fetchall()
        print(result)
        dbase.commit()
        dbase.close()

    def db_select_userid(self, number, pin):
        """Selects and returns user id by card number and pin"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(f''' SELECT id FROM cards WHERE number={number} AND pin={pin}''')
        result = cursor.fetchone()
        dbase.commit()
        dbase.close()
        return result

    def db_select_user_balance(self, user_id):
        """Selects and returns user balance by user id"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(f''' SELECT balance FROM cards WHERE id={user_id}''')
        result = cursor.fetchone()
        dbase.commit()
        dbase.close()
        return result

    def db_update_user_balance(self, user_id, income):
        """Increases balance by income value to user id"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(f''' UPDATE cards SET balance = balance + {income} WHERE id = {user_id} ''')
        dbase.commit()
        dbase.close()

    def db_select_transfer_id(self, number):
        """Selects and returns transfer id by card number"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(f''' SELECT id FROM cards WHERE number={number}''')
        result = cursor.fetchone()
        dbase.commit()
        dbase.close()
        return result

    def db_transfer_money(self, user_id, transfer_id, transfer):
        """Transfers money from one user to another"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(f'''UPDATE cards SET balance = balance + {transfer} WHERE id = {transfer_id}''')
        cursor.execute(f'''UPDATE cards SET balance = balance - {transfer} WHERE id = {user_id}''')
        dbase.commit()
        dbase.close()

    def db_delete_account(self, user_id):
        """Delete account by user id"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(f''' DELETE FROM cards WHERE id = {user_id} ''')
        dbase.commit()
        dbase.close()

    def db_drop_table(self):
        """Drops 'cards' table"""
        dbase = sqlite3.connect(self.db_name)
        cursor = dbase.cursor()
        cursor.execute(''' DROP TABLE cards ''')
        print("Table dropped")
        dbase.commit()
        dbase.close()

    @classmethod
    def delete_db(cls):
        """Deletes db"""
        os.remove(cls.db_name)
        print("DB removed")


if __name__ == '__main__':
    # Create table
    db_check = BankingDB()
    db_check.db_select_all()
    # Create account
    card_ = generate_card()
    pin_ = generate_password()
    db_check.db_create_account(card_, pin_)
    db_check.db_select_all()
    # Get id
    user_id_ = db_check.db_select_userid(card_, pin_)[0]
    print(f"id: {user_id_}")
    # Get balance
    print(f"balance: {db_check.db_select_user_balance(user_id_)[0]}")
    # Income balance
    db_check.db_update_user_balance(user_id_, 1000)
    print(f"balance after income: {db_check.db_select_user_balance(user_id_)[0]}")
    # Get transfer id
    card_ = generate_card()
    pin_ = generate_password()
    db_check.db_create_account(card_, pin_)
    db_check.db_select_all()
    transfer_id_ = db_check.db_select_transfer_id(card_)[0]
    print(f"transfer id: {transfer_id_}")
    # Transfer
    db_check.db_transfer_money(user_id_, transfer_id_, 500)
    print(f"balance {user_id_}: {db_check.db_select_user_balance(user_id_)[0]}")
    print(f"balance {transfer_id_}: {db_check.db_select_user_balance(transfer_id_)[0]}")
    # Delete account
    db_check.db_delete_account(user_id_)
    print(f"{user_id_} deleted")
    db_check.db_select_all()
    # Delete table
    db_check.db_drop_table()
    # Delete DB
    db_check.delete_db()
