'''
Created on 7 nov. 2017

@author: rlang
'''
import numpy as np
from sklearn import linear_model
import datetime as dtime

def date_conversion(date): # date like "YYYY-MM-DD"
    year = date[:4]
    month = date[5:-3]
    day = date[8:]
    return dtime.datetime(int(year),int(month),int(day))

def date_number_month(date): # date like "YYYY-MM" after "2018-01" convert in number of month between date and "2018-01"
    year = int(date[:4])
    month = int(date[5:])
    if(year<2018 or month<0):
        raise ValueError("date should be YYYY-MM with YYYY>2018 and MM>01")
    else:
        return [[month + (year-2018)*12]]   

def date_imcremmonth(date):
    month = date.month
    year = date.year 
    if(month<12):
        month = month + 1
    else:
        year = year + 1
        month = 1 
    return dtime.datetime(year,month,date.day)
 
def data_extraction(con):
    
    cursor = con.cursor()
    
    cursor.execute("""
    
    SELECT PriceChanges.id, PriceChanges.old_price, PriceChanges.new_price, PriceChanges.change_date 
     
    FROM
     
    
    ( SELECT BuiltBetween.id   
    
    FROM Details 
    INNER JOIN 
    (SELECT BuiltUsedArea.id  
    FROM BuiltUsedArea 
    WHERE BuiltUsedArea.built_area>200 AND BuiltUsedArea.built_area<300) AS BuiltBetween
    ON Details.id = BuiltBetween.id 
    
    WHERE Details.details LIKE '%sea%' OR Details.details LIKE '%ocean%' OR Details.details LIKE '%bay%' OR Details.details LIKE '%waterfront%'
    
    GROUP BY BuiltBetween.id) AS BuildOk
    
    INNER JOIN PriceChanges ON PriceChanges.id = BuildOk.id
    
    
    ORDER BY PriceChanges.id, PriceChanges.change_date
       
    """)
    
    donnees = {}
    
    for row in cursor.fetchall() :
        identifiant = row[0]
        datechangement = row[3]
        if not(identifiant in donnees):
            donnees[identifiant] = {}
        donnees[identifiant][datechangement]=np.array([row[1],row[2]])
    return donnees


def research_first_date(date_dico):
    firstdate = "2018-01-01"
    for datechange in (date_dico):
            if(date_conversion(datechange)<date_conversion(firstdate)):
                firstdate=datechange
    return firstdate 
     
def regresstot(donnees):
    dico_regression = {}
    for iden in donnees:
        dico_regression[iden]=regress1(donnees[iden])
    return dico_regression 
        
def regress1(dico_data):
    valueY = np.arange(24)
    firstdatechange = research_first_date(dico_data)       
    datecurrent = dtime.datetime(2016,1,1)
    datefin = dtime.datetime(2017,12,1)
    currentprice = dico_data[firstdatechange][0]
    nextprice = dico_data[firstdatechange][1] 
    i=0
    while(datecurrent<datefin):
        while((datecurrent)>(date_conversion(firstdatechange))) and dico_data:
            firstdatechange = research_first_date(dico_data)
            currentprice = dico_data[firstdatechange][0]
            nextprice = dico_data[firstdatechange][1]
            del dico_data[firstdatechange]
        if((datecurrent)>(date_conversion(firstdatechange))) and (not(dico_data)):
            datecurrent=datefin
            currentprice=nextprice
            for k in range(i,24):
                valueY[k] = currentprice
        else:
            valueY[i] = currentprice
            i=i+1
            datecurrent=date_imcremmonth(datecurrent)
    regression = linear_model.LinearRegression()
    regression.fit(np.arange(24).reshape(24,1), valueY.reshape(24,1))
    return regression

def predict_average(conn, date): # date is month+year like "YYYY-MM"
    data = data_extraction(conn)
    date = date_number_month(date)
    regress = regresstot(data)
    predict = {}
    for iden in regress :
        predict[iden]=regress[iden].predict(date)
    predict_av = np.arange(len(predict)*1.0)
    i=0
    for iden in predict:
        predict_av[i]=predict[iden][0][0]
        i=i+1
    return np.mean(predict_av)                    
                
            
      
        
            
        