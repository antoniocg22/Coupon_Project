def check_groups(s_groups, conn_ec2):
    flg_free_group = False  # Bandera que marca si existe o no un grupo libre
    for group in s_groups:
        for rule in group.rules:
            ip_range = rule.grants
            if str(ip_range) == "[0.0.0.0/0]":
                free_group = group
                flg_free_group = True
            else:
                pass
        if flg_free_group == True:
            print "Grupo con rangos de IP libres encontrado"
            break
            # Si en la cuenta no existe algun "security group" libre, se crea uno con esas caracteristicas
    if flg_free_group == False:
        free_group = conn_ec2.create_security_group("GrupoLibre",
                                                    "Grupo con el cual se puede conectar desde cualquier IP")
        free_group.authorize('tcp', 3306, 3306, '0.0.0.0/0')
        print "Grupo con rangos de IP creados"

    return str(free_group.id)


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


def create_instance_aws(conn_rds, conn_ec2):
    from connect_parameters import define_connect_params

    #Checar si existen "security groups" con rangos de ip libres.
    all_security_groups = conn_ec2.get_all_security_groups()

    free_group = check_groups(all_security_groups, conn_ec2) #Id del grupo para el libre transito

    param_conect = define_connect_params()#Funcion para crear archivo yaml con parametros de conexion

    #Definir parametros para la Instancia
    DB_name = param_conect['DB'] #Nombre que la BD va a tener
    DB_instance_name = param_conect['INSTANCE'] #Nombre de la instancia
    DB_storage_size = 10 #Capacidad de almacenamiento de la instancia en GB
    DB_instance_clase = "db.t2.micro" #Capacidad de la isntancia.
    DB_engine = "MySQL" #Motor de la BD
    DB_master_username = param_conect['USERNAME'] #Nombre del usuario maestro
    DB_master_password = param_conect['PASSWORD'] #Contrasenia del usuario maestro
    DB_secutity_group = [free_group] #Security group libre
    DB_zone = "us-west-2b" #Zona en donde sera creada la isntnacia
    DB_preferred_maintenance_w = "mon:10:48-mon:11:18" #Periodo de mantenimiento
    DB_parameter_group_name = "default.mysql5.6"
    DB_backup_period = 7
    DB_port = param_conect['PORT'] #Puerto
    DB_multi_az = 0 #Si se quiere la instancia en varias zonas
    DB_engine_version = "5.6.27"
    DB_auto_minor_version_upgrade = 1 #Recibir actualizaciones
    DB_license_model = "general-public-license" #Tipo de licencia
    #DB_IOPS = ommit Este parametro lo omitimos
    DB_option_groupname = "default:mysql-5-6" #O
    DB_publicy_access = 1 #Para permitir el trafico
    try:
        conn_rds.create_db_instance(db_instance_identifier= DB_instance_name,
                                    allocated_storage= DB_storage_size,
                                    db_instance_class= DB_instance_clase,
                                    engine= DB_engine,
                                    master_username= DB_master_username,
                                    master_user_password= DB_master_password,
                                    db_name= DB_name,
                                    #db_security_groups= DB_secutity_group,
                                    vpc_security_group_ids=DB_secutity_group,
                                    availability_zone= DB_zone,
                                    #db_subnet_group_name= DB_subnet_groups,
                                    backup_retention_period= DB_backup_period,
                                    port=DB_port,
                                    multi_az= False,
                                    engine_version= DB_engine_version,
                                    auto_minor_version_upgrade= True,
                                    license_model= DB_license_model,
                                    option_group_name= DB_option_groupname,
                                    publicly_accessible=True
                                    )
        print "Instancia Creada"

    finally:
        print "Siguiente paso es obtener el host."

    return param_conect


def main():
    conn_rds, conn_ec2 = multi_conn()
    create_instance_aws(conn_rds, conn_ec2)

if __name__ == "__main__":
    main()

