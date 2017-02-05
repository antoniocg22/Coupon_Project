import pymysql

# Para conectar a la base de datos
HOST = 'couponplus.c58qgcdaakud.us-west-2.rds.amazonaws.com'
USER = 'alumno'
PASSWORD = 'proyecto2017'
DB = 'Coupon'

CSV_FILE = "en_coupon_list_train.csv"

connection = pymysql.connect(host=HOST,
                             port=3306,
                             user=USER,
                             password=PASSWORD,
                             database=DB,
                             local_infile=True)
print "Conectado a la base de datos"
try:
    with connection.cursor() as cursor:
        sql = """LOAD DATA LOCAL INFILE 'en_coupon_list_train.csv'
                 INTO TABLE list
                 FIELDS TERMINATED BY ","
                 OPTIONALLY ENCLOSED BY '"'
                 LINES TERMINATED BY '\r\n'
                 IGNORE 1 ROWS"""
        print "Subiendo datos"
        cursor.execute(sql)
        print "Datos subidos a tabla de list"
    with connection.cursor() as cursor:
        sql2 = """LOAD DATA LOCAL INFILE 'en_coupon_area_train.csv'
                 INTO TABLE area
                 FIELDS TERMINATED BY ","
                 OPTIONALLY ENCLOSED BY '"'
                 LINES TERMINATED BY '\r\n'
                 IGNORE 1 ROWS"""
        print "Subiendo datos"
        cursor.execute(sql2)
        print "Datos subidos a tabla de area"
    with connection.cursor() as cursor:
        sql3 = """LOAD DATA LOCAL INFILE 'en_coupon_detail_train.csv'
                 INTO TABLE detail
                 FIELDS TERMINATED BY ","
                 OPTIONALLY ENCLOSED BY '"'
                 LINES TERMINATED BY '\r\n'
                 IGNORE 1 ROWS"""
        print "Subiendo datos"
        cursor.execute(sql3)
        print "Datos subidos a tabla de detail"
    with connection.cursor() as cursor:
        sql4 = """LOAD DATA LOCAL INFILE 'en_user_list.csv'
                 INTO TABLE user
                 FIELDS TERMINATED BY ","
                 OPTIONALLY ENCLOSED BY '"'
                 LINES TERMINATED BY '\r\n'
                 IGNORE 1 ROWS"""
        print "Subiendo datos"
        cursor.execute(sql4)
        print "Datos subidos a tabla user"
    with connection.cursor() as cursor:
        sql5 = """LOAD DATA LOCAL INFILE 'coupon_visit_train.csv'
                 INTO TABLE area
                 FIELDS TERMINATED BY ","
                 OPTIONALLY ENCLOSED BY '"'
                 LINES TERMINATED BY '\r\n'
                 IGNORE 1 ROWS"""
        print "Subiendo datos"
        cursor.execute(sql5)
        print "Datos subidos a tabla de visit"
finally:
    connection.close()
    print "Conexcion cerrada"