import connect_parameters as cp
import create_instance as ci
import get_host as gh


def execute_sql_scripts(filename, conn):
    import pymysql
    fd = open(filename, "r")
    sqlFile = fd.read()
    fd.close()

    sqlCommands = sqlFile.split(';')
    sqlCommands = [x for x in sqlCommands if len(x) > 0]
    try:
        for command in sqlCommands:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(command)
                    conn.commit()
                    print "Comando ejecutado exitosamente"
            except pymysql.OperationalError, msg:
                print "Command omitido: ", msg
    finally:
        print "Archivo .sql ejecutado"

def multi_conn():
    import boto.rds2
    import boto.ec2

    ACCESS_KEY_ID = raw_input("Ingrese la ACCESS KEY ID de la cuenta de AWS ")
    SECRECT_ACCESS_KEY = raw_input("Ingres a SECRET ACCESS KEY de la cuenta de AWS ")

    conn_rds = boto.rds2.connect_to_region(
        "us-west-2",  # Esta region es la de Oregon(Gratuita)
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRECT_ACCESS_KEY
    )

    conn_ec2 = boto.ec2.connect_to_region(
        "us-west-2",  # Esta region es la de Oregon(Gratuita)
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRECT_ACCESS_KEY
    )

    return conn_rds, conn_ec2


conn_rds, conn_ec2 = multi_conn()

params = ci.create_instance_aws(conn_rds, conn_ec2)

params = gh.get_host(conn_rds, params)

#Conexion a la BD
my_conn = cp.con_db(params)

#Para crear tablas en la bd
print "Se ejecutara el Query para la creacion de tablas"
execute_sql_scripts("create_tables.sql", my_conn)

#Para poblar las tablas
print "Se ejecutara el Query para poblar las tablas"
execute_sql_scripts("insert_data.sql", my_conn)

my_conn.close()
print "Conexion cerrada"