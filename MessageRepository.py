from lib.db import * 
from .Message import *

class MessageRepository:
    def __init__(self):
        conn = connect()
        self.conn = conn[0]
        self.curs = conn[1]
    def save(self, message):
        self.curs.execute(f"""
            INSERT INTO messages VALUES(
            {message.id},
            '{message.content}',
            '{message.sender.id}',
            null
                );
            """)
        self.conn.commit()
        
#hm1: delete, update
    def update(self, message):
        self.curs.execute(f"""
            UPDATE messages SET
            content = '{message.content}',
            sender = '{message.sender}',
            receiver = '{message.receiver}'
            WHERE id = {message.id};
            """)
        self.conn.commit()
    def delete(self, message):
        self.curs.execute(f"""
            DELETE FROM messages
            WHERE
            id = {message.id};
            """)
        self.conn.commit()

    def findById(self, id):
        self.curs.execute(f"""
            SELECT * FROM messages
            WHERE
            id = {id};
            """)
        data = self.curs.fetchone()
        return Message(*data)
    def findAllByContent(self, keyword):
        self.curs.execute(f"""
            SELECT * FROM messages
            WHERE content LIKE '%{keyword}%';
            """)
        return list(map(lambda data: Message(*data),self.curs.fetchall()))
