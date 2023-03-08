import mysql.connector as msql
from mysql.connector import Error
from key import password_sql #dit is een klasse die ik heb gemaakt en mijn password in zit als een variable

try:
    

    config = {
        'host': 'localhost',
        'user': 'root',
        'password': password_sql,
        'database': 'social_media'
        }

    with msql.connect(**config) as conn:
        print('Creating table....')
        cursor = conn.cursor()
        cursor.execute("call create_table_recept()")
        cursor.execute("call create_table_ingredients()")
        cursor.execute("call create_table_categorys()")
        cursor.execute("call create_table_materialen()")
        cursor.execute("call create_table_recept_materialen()")
        print("Tables are created....")

   
except Error as e:
    print("Error while connecting to MySQL", e)