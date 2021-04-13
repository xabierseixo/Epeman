import sqlite3
import random
import time
import sys

db_conector = sqlite3.connect('epeman.db')
db_cursor = db_conector.cursor()

while True:
    
    grados = (random.randrange(20))
    db_cursor.execute("INSERT INTO temperaturas values(datetime('now'), (?))", (grados,))
    db_conector.commit()    
    print ("sair")
    time.sleep(3)

db_conector.close()

