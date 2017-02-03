import csv
import pymysql

HOST = 'couponplus.c58qgcdaakud.us-west-2.rds.amazonaws.com'
USER = 'alumno'
PASSWORD = 'proyecto2017'
DB = 'Coupon'
ENGINE = 'MyISAM'
TABLE_DEFINITION_area = (
    'CREATE TABLE `area` ('
    '   `small_area_name` varchar(50),'
    '   `pref_name` varchar(25),'
    '   `coupon_id_hash` varchar(32)'
    ') ENGINE=MyISAM'
)

TABLE_DEFINITION_detail = (
    'CREATE TABLE `detail` ('
    '   `item_count` tinyint unsigned,'
    '   `i_date` datetime,'
    '   `small_area_name` varchar(50),'
    '   `purchaseid_hash` varchar(32),'
    '   `user_id_hash` varchar(32),'
    '   `coupon_id_hash` varchar(32)'
    ') ENGINE=MyISAM'
)

TABLE_DEFINITION_list = (
    'CREATE TABLE `list` ('
    '`capsule_text` varchar(21),'
    '`genre_name` varchar(24),'
    '`price_rate` tinyint unsigned,'
    '`catalog_price` mediumint unsigned,'
    '`discount_price` mediumint unsigned,'
    '`dispfrom` datetime,'
    '`dispend` datetime,'
    '`dispperiod` tinyint unsigned,'
    '`validfrom` date,'
    '`validend` date,'
    '`validperiod` tinyint unsigned,'
    '`usable_date_mon` tinyint unsigned,'
    '`usable_date_tue` tinyint unsigned,'
    '`usable_date_wed` tinyint unsigned,'
    '`usable_date_thu` tinyint unsigned,'
    '`usable_date_fri` tinyint unsigned,'
    '`usable_date_sat` tinyint unsigned,'
    '`usable_date_sun` tinyint unsigned,'
    '`usable_date_holiday` tinyint unsigned,'
    '`usable_date_before_holiday` tinyint unsigned,'
    '`large_area_name` varchar(14),'
    '`ken_name` varchar(20),'
    '`small_area_name` varchar(41),'
    '`coupon_id_hash` varchar(32)'
    ') ENGINE=MyISAM'
)

TABLE_DEFINITION_visit = (
    'CREATE TABLE `visit` ('
    '`PURCHASE_FLG` tinyint(1),'
    '`I_DATE` datetime,'
    '`PAGE_SERIAL` smallint unsigned,'
    '`REFERRER_hash` varchar(32),'
    '`VIEW_COUPON_ID_hash` varchar(32),'
    '`USER_ID_hash` varchar(32),'
    '`SESSION_ID_hash` varchar(32),'
    '`PURCHASEID_hash` varchar(32)'
    ') ENGINE=MyISAM'
)

TABLE_DEFINITION_user = (
    'CREATE TABLE `user` ('
    '`reg_date` datetime,'
    '`sex_id` varchar(1),'
    '`age` tinyint unsigned,'
    '`withdraw_date` datetime,'
    '`pref_name` varchar(20),'
    '`user_id_hash` varchar(32)'
    ') ENGINE=MyISAM'
)
connection = pymysql.connect(host=HOST,
                             port=3306,
                             user=USER,
                             password=PASSWORD,
                             database=DB)
print 'Conectado a la base de datos'

try:
    with connection.cursor() as cursor:
        cursor.execute(TABLE_DEFINITION_area)
    connection.commit()
    print "Tabla area creada"

    with connection.cursor() as cursor:
        cursor.execute(TABLE_DEFINITION_detail)
        connection.commit()
        print "Tabla detail creada"

    with connection.cursor() as cursor:
        cursor.execute(TABLE_DEFINITION_list)
        connection.commit()
        print "Tabla list creada"

    with connection.cursor() as cursor:
        cursor.execute(TABLE_DEFINITION_user)
        connection.commit()
        print "Tabla user creada"

    with connection.cursor() as cursor:
        cursor.execute(TABLE_DEFINITION_visit)
        connection.commit()
        print "Tabla visit creada"

finally:
    connection.close()
    print 'Conexcion cerrada'
