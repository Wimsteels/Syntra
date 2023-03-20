import mysql.connector as msql
from mysql.connector import Error
from key import password_sql 
import json 
#https://qiita.com/skokado/items/caa31d3845df23bc0913
try:

    config = {
    'host': 'localhost',
    'user': 'root',
    'password': password_sql,
    'database': 'reciperevolution'
    }
    #https://www.geeksforgeeks.org/args-kwargs-python/
    conn = msql.connect(**config) 
    if conn.is_connected():

        cursor = conn.cursor()
        f = open('../data/recept.json')  
        data = json.load(f)

        for i in data:
            ReceptID = i["ReceptID"]
            Receptnaam = i["Receptnaam"]
            Bereidingswijze = i["Bereidingswijze"]
           

            query = f'''call insert_data_recept(%s,%s,%s)'''
            val = (ReceptID, Receptnaam, Bereidingswijze)
            cursor.execute(query,val)

        conn.commit()
        #The db.commit() in the above code is important. It is used to commit the changes made to the table. Without using commit(), no changes will be made in the table.
        conn.close()

except Error as e:
    print("Error while connecting to MySQL", e)