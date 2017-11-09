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
    
    # Database connexion and data importation
     
    conn = sqlite3.connect('task2.db')
    
    #the database is already created and include in the project, so you don't need to uncomment this 3 lines 
    
        
    #dataImport.import_built_used_area(conn)
    #dataImport.import_details(conn)
    #dataImport.import_price_changes(conn)
    
    cursor=conn.cursor()
    
    # Question 1 
    
    #averagequestion1 = question1.resol(conn)
    #print(averagequestion1) #uncomment to see the result 
    
    # question 2 
    
    #pred = question2.predict_average(conn, "2018-04") # replace "2018-04" with the "YYYY-MM">="2018-04" you want  
    #print(pred)
    
    # question 3
        
    #datascatter = question3.data_extraction(conn) # uncomment to see the graph 
    #question3.scatter_graph(datascatter) 
    
    
    pass

