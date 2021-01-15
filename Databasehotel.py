#Backend

import sqlite3

def HotelDate():
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS booking (id INTEGER PRIMARY KEY, CusID text, Firstname text, Lastname text,\
                  Address text, Mobile text, Nationality text, DoB text, ProveofID text, DateIn text, DateOut text, Email text)")
    con.commit()
    con.close()

def addHotelRec(CusID,Firstname,Lastname,Address,Mobile,Nationality,ProveofID,DateIn,DateOut,Email):
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute("INSERT INTO VALUES (NULL, ?,?, ?,?, ?,?, ?,?, ?,?, ?)", \
               (CusID,Firstname,Lastname,Address,Mobile,Nationality,ProveofID,DoB,DateIn,DateOut,Email))
    con.commit()
    con.close()

def viewDate():
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM hotel")
    rows = cur.fetchall()
    con.close
    return rows
    
    
def deleteRec(id):
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute("DELETE  FROM WHERE id=?",(id,))
    con.commit()
    con.close

def searchDate(CusID="",Firstname="",Lastname="",Address="",Mobile="",Nationality="",ProveofID="",DateIn="",DateOut="",Email=""):
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM hotel WHERE CusID=? OR Firstname=? OR Lastname=? OR Address=? OR Mobile=?\
                 OR Nationality=? OR ProveofID=? OR DoB=? OR DateIn=? OR DateOut=? Email=?",\
                CusID,Firstname,Lastname,Address,Mobile,Nationality,ProveofID,DateIn,DateOut,Email)
    rows = cur.fetchall()
    con.close
    return rows

def dataUpdate(id,CusID="",Firstname="",Lastname="",DoB="",Address="",Mobile="",Nationality="",ProveofID="",DateIn="",DateOut="",Email=""):
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute("UPDATE hotel SET CusID=? OR Firstname=? OR Lastname=? OR Address=? OR Mobile=?\
                 OR Nationality=? OR DoB=? OR ProveofID=? OR DateIn=? OR DateOut=? Email,WHERE id=?",\
                     CusID,Firstname,DoB,Lastname,Address,Mobile,Nationality,ProveofID,DateIn,DateOut,Email,id)
    con.commit()
    con.close
   


   
