from .db import *

def registerClient(client_id, client_name, client_phone, client_email,  client_password):
 conn, curs = connect()
# check for client existence
 curs.execute(f"""
  SELECT COUNT(*) FROM clients
  WHERE
   phone = '{client_phone}'
  OR
   'email = '{client_email}';
 """)
 if curs.fetchone()[0] == 0:
  curs.execute(f"""
   INSERT INTO clients VALUES(
    {client_id},
    '{client_name}',
    '{client_phone}',
    '{client_email}',
    '{client_password}'
     );
 """)
  conn.commit()
 else:
  print("This email or phone is used, is this your account ? ")

def loginClient(client_email, client_password):
 conn, curs = connect()
 curs.execute(f"""
  SELECT * FROM clients
  WHERE
   email = '{client_email}'
  AND
   password = '{client_password}'
  AND
   active = true;
 """)
 client = curs.fetchone()
 if client != None:
  id = client[0]
  curs.execute(f"""
   INSERT INTO sessions (client_id, data, authenticated) VALUES (
   {id},
    '',
   NOW()
     );
  """)
  conn.commit()
 else:
  print("Wrong credentials!")
  
def logoutClient(client_id):
 conn, curs = connect()
 curs.execute(f"""
  DELETE FROM sessions
  WHERE client_id = '{client_id}'
  """)
 conn.commit()
 
def removeClient(client_id):
 conn, curs = connect()
  curs.execute(f"""
   DELETE FROM clients
   WHERE id = '{client_id}'
 """)
  conn.commit()
 
def addLocation(id, client_id, city_id, city_name, street_id, street_name, number):
 conn, curs = connect()
 curs.execute(f"""
  BEGIN;
  INSERT INTO locations (id, client_id, city_id, street_id, number) VALUES (
   {id}, {client_id}, {city_id}, {street_id}, '{number}');
  INSERT INTO cities (id, name) VALUES ( {city_id}, '{city_name}');
  INSERT INTO streets (id, name) VALUES ( {street_id}, '{street_name}');
   COMMIT;
 """)
 #conn.commit()
 
def updateClientPhone(client_id, new_phone):
 conn, curs = connect()
 curs.execute(f"""
  UPDATE "clients" SET phone = '{new_phone}' WHERE id = {client_id};
 """)
  conn.commit()
  
def updateClientEmail(client_id, new_email):
 conn, curs = connect()
 curs.execute(f"""
  UPDATE "clients" SET email = '{new_email}' WHERE id = {client_id};
 """)
  conn.commit()
  
def updateClientPassword(old_password, new_password):
# check for client existence
 conn, curs = connect()
 curs.execute(f"""
  SELECT * FROM clients
  WHERE
   password = '{old_password}'
 """)
 client = curs.fetchone()
 if client != None:
  id = client[0]
  curs.execute(f"""
   UPDATE "clients" SET password = '{new_password}' WHERE id = {id};
 """)
  conn.commit()
 else:
  print("Wrong old_password.")

#HW1: create the next functions:
#- removeClient(client_id)
#- addLocation(city_name, street_name, number, client_id)
#- updateClientPhone(client_id, new_phone)
#- updateClientEmail(client_id, new_email)
#- updateClientPassword(client_id, old_password, new_password)