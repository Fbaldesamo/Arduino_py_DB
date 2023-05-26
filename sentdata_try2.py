import mysql.connector
import time
import serial

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="testing_1"
)

ser = serial.Serial('COM5',9600, timeout = 1)
time.sleep(0.5)

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

    







while(True):
    
    
    #dateFormat
    dt_string = now.strftime("%d/%m/%Y %I:%M:%S")
    #arduinoSerial
    data = ser.readline().decode().strip()
    mycursor = mydb.cursor()
    




    if data=='1':
        
        sql = "INSERT INTO button_state (ButtonState, Date) VALUES (%s, %s)"
        val = ("ON", dt_string)
        print("ON")
        mycursor.execute(sql, val)
        mydb.commit()
        
    if data=='0':
        sql = "INSERT INTO button_state (ButtonState, Date) VALUES (%s, %s)"
        val = ("OFF", dt_string)
        print("OFF") 
        mycursor.execute(sql, val)
        mydb.commit()
        
        
    

    ser.flushInput()
    
    
    
    
    
