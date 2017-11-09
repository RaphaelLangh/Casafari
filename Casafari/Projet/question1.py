'''
Created on 8 nov. 2017

@author: rlang
'''
def resol(conn):
    cursor = conn.cursor()
    
    cursor.execute(""" 
    
    SELECT AVG(PriceRise2016Present.new_price*1.0/BuiltUsedArea.built_area)
    
    FROM 
    
    (
    
    SELECT PriceChanges.id, PriceChanges.new_price
    
    FROM 
        
    ( SELECT PriceChangesFin.id 
    
    FROM
    
    (SELECT PriceChanges2016.id, PriceChanges2016.new_price
    FROM (SELECT * FROM PriceChanges WHERE strftime('%Y',change_date)='2016' ORDER BY id) AS PriceChanges2016 
    GROUP BY id 
    HAVING strftime('%s',PriceChanges2016.change_date)=MAX(strftime('%s',PriceChanges2016.change_date))) AS PriceChangesFin 
    
    INNER JOIN 
    
    (SELECT PriceChanges2016.id, PriceChanges2016.old_price
    FROM (SELECT * FROM PriceChanges WHERE strftime('%Y',change_date)='2016' ORDER BY id) AS PriceChanges2016 
    GROUP BY id
    HAVING strftime('%s',PriceChanges2016.change_date)=MIN(strftime('%s',PriceChanges2016.change_date) )) AS PriceChangesDeb
    
    ON PriceChangesFin.id = PriceChangesDeb.id
    
    WHERE old_price < new_price ) AS PriceRise2016 
    
    INNER JOIN PriceChanges
    
    ON PriceRise2016.id = PriceChanges.id
    
    GROUP BY PriceChanges.id HAVING MAX(strftime('%s',PriceChanges.change_date))=strftime('%s',PriceChanges.change_date)) AS PriceRise2016Present
    
    INNER JOIN BuiltUsedArea
    
    ON PriceRise2016Present.id = BuiltUsedArea.id
    
    WHERE BuiltUsedArea.built_area>200   
    
    """)
    return cursor.fetchall()