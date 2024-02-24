from lib.db import * 
from .Client import *

# Repository pattern - storage operations 
class ClientRepository:
#CRUD / BREAD
    def __init__(self):
        #self.conn, self.cur = connect()
        conn = connect()
        self.conn = conn[0]
        self.curs = conn[1]
        # HW1: this function should return a list of all Client objects
    def findAll(self):
        self.curs.execute(f"""
            SELECT * FROM clients
            """)
        clients = []
        #print(self.curs.fetchall())
        data = self.curs.fetchall()
        for client in data:
             #c = Client(*client)
             #clients.append(c)
             clients.append(Client(*client))
        return clients
    def findById(self, id):
        self.curs.execute(f"""
            SELECT * FROM clients
            WHERE
            id = {id};
            """)
        #print(self.curs.fetchone())
        data = self.curs.fetchone()
        return Client(*data)
    def countByEmailOrPhone(self, phone, email):
            self.curs.execute(f"""
            SELECT COUNT(*) FROM clients
            WHERE
            phone = '{phone}'
            OR
            email = '{email}';
            """)
            return self.curs.fetchone()[0]
    def save(self, client):
        self.curs.execute(f"""
            INSERT INTO clients VALUES(
            {client.id},
            '{client.name}',
            '{client.phone}',
            '{client.email}',
            '{client.password}',
            '{client.active}'
                );
            """)
        self.conn.commit()
    def update(self, client):
        pass
    def delete(self, client):
        pass

