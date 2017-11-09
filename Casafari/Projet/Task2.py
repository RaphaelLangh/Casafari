'''
Created on 2 nov. 2017

@author: rlang
'''
import sqlite3
from Projet import dataImport
from Projet import question1
from Projet import question2
from Projet import question3
  

if __name__ == '__main__':
    
    # Database creation and data importation
     
    conn = sqlite3.connect('task2.db')
    dataImport.import_built_used_area(conn)
    dataImport.import_details(conn)
    dataImport.import_price_changes(conn)
    
    cursor=conn.cursor()
    
    # Question 1 
    
    averagequestion1 = question1.resol(conn)
    print(averagequestion1)
    
    # question 2 
    
    #pred = question2.predict_average(conn, "2018-04")
    #print(pred)
    
    # question 3
        
    datascatter = question3.data_extraction(conn)
    question3.scatter_graph(datascatter)
    
    
    
    pass

