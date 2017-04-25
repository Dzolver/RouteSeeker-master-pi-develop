import pymssql
import time
import subprocess

'''create connection to azure sql db'''
conn = pymssql.connect(server='sdgpsqldb.database.windows.net',
                       user='dbadmin@sdgpsqldb',
                       password='Smarthelmetv1',
                       database='sdgplocationdb')

cursor = conn.cursor()

refresh = True
while refresh:
    print("Searching for location data.........")
    cursor.execute('SELECT loc FROM locations;')
    row = cursor.fetchone()
    while row:
        if (str(row[0])!= ""):
            with open("loc.txt", "w") as text_file:
                text_file.write(str(row[0]))
                print("Success!\n")
                refresh = False
        else:
            print("No value detected.\n")
            refresh = True
        row = cursor.fetchone()
    print("Searching for destination data........")
    cursor.execute('SELECT dest FROM locations;')
    row = cursor.fetchone()
    while row:
        if (str(row[0])!= ""):
            with open("dest.txt", "w") as text_file:
                 text_file.write(str(row[0]))
                 print("Success!\n")
                 refresh = False
        else:
            print("No value detected.\n")
            refresh = True
        row = cursor.fetchone()
    if refresh:
        time.sleep(5)

print("Route confirmed.")

subprocess.call(["python", "mapgen.py"])