'''
Created on 8 nov. 2017

@author: rlang
'''

import numpy as np 
from matplotlib import pyplot as plt

def data_extraction(con):
    
    cursor = con.cursor()
    
    cursor.execute("""
    
    SELECT SeaviewPrice.id, (1.0*SeaviewPrice.new_price)/BuiltUsedArea.built_area 
    
    FROM 
    
    (SELECT SeaviewId.id, PriceChanges.new_price
    
    FROM
    
    (SELECT Details.id
    FROM Details
    WHERE Details.details LIKE '%sea%' OR Details.details LIKE '%ocean%' OR Details.details LIKE '%bay%' OR Details.details LIKE '%waterfront%')
    AS SeaviewId
    INNER JOIN PriceChanges ON SeaviewId.id = PriceChanges.id
    
    GROUP BY PriceChanges.id
    
    HAVING strftime('%s',PriceChanges.change_date) = MAX(strftime('%s',PriceChanges.change_date))
    
    )
    
    AS SeaviewPrice
    
    INNER JOIN BuiltUsedArea ON SeaviewPrice.id = BuiltUsedArea.id
    
    WHERE BuiltUsedArea.built_area>0
    
    GROUP BY BuiltUsedArea.id   
    
    """)
    
    valueid = []
    valueprice = []
    
    for row in cursor.fetchall():
        valueid.append(row[0])
        valueprice.append(row[1])
    
    return np.array([valueid,valueprice])

def scatter_graph(data):
    valueX = np.arange(len(data[1]))
    valueY = np.array(data[1])
    print(valueY)
    plt.scatter(valueX,valueY)
    plt.show()
    return 
