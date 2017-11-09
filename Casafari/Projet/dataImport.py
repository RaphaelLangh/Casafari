'''
Created on 4 nov. 2017

@author: rlang
'''
import csv
  
def import_built_used_area(conn):
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS BuiltUsedArea""")
    cursor.execute("""
    CREATE TABLE BuiltUsedArea(
     id INT ,
     built_area INT,
     used_area INT)
     """)
     
    file = open("C:/Users/rlang/workspace_nouveau/Casafari/Data/Built_used_area.csv","rt")
    reader = csv.DictReader(file,fieldnames=None, restkey=None, restval=None, delimiter=';')
    
    for row in reader :
        cursor.execute("INSERT INTO BuiltUsedArea VALUES (?,?,?)",[row["listing_id"],row["built_area"],row["used_area"]])
    
    return 

def import_details(conn):
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Details""")
    cursor.execute("""
    CREATE TABLE Details(
    id INT ,
    details TEXT
    )
    """)
     
    file = open("C:/Users/rlang/workspace_nouveau/Casafari/Data/Details.csv","rt")
    reader = csv.DictReader(file,fieldnames=None, restkey=None, restval=None, delimiter=';')
    
    for row in reader :
        cursor.execute("INSERT INTO Details VALUES (?,?)",[row["listing_id"],row["Details"]])
    return 
    
def import_price_changes(conn):
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS PriceChanges""")
    cursor.execute("""
       CREATE TABLE PriceChanges(
       id INT ,
       old_price INT , 
       new_price INT ,
       change_date DATE 
       )
       """)
    
    file = open("C:/Users/rlang/workspace_nouveau/Casafari/Data/Price_changes.csv","rt")
    reader = csv.DictReader(file,fieldnames=None, restkey=None, restval=None, delimiter=';')
    for row in reader :
        cursor.execute("INSERT INTO PriceChanges VALUES (?,?,?,?)",[row["listing_id"],row["old_price"],row["new_price"],row["change_date"]])
    return 