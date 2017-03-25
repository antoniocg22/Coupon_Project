def con_rds():
    import boto.rds2
    ACCESS_KEY_ID = raw_input("Ingrese la ACCESS KEY ID de la cuenta de AWS ")
    SECRECT_ACCESS_KEY = raw_input("Ingres a SECRET ACCESS KEY de la cuenta de AWS ")

    conn_rds = boto.rds2.connect_to_region(
        "us-west-2",  # Esta region es la de Oregon(Gratuita)
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRECT_ACCESS_KEY
    )
    return conn_rds


def con_ec2():
    import boto.ec2
    ACCESS_KEY_ID = raw_input("Ingrese la ACCESS KEY ID de la cuenta de AWS ")
    SECRECT_ACCESS_KEY = raw_input("Ingres a SECRET ACCESS KEY de la cuenta de AWS ")

    conn_ec2 = boto.ec2.connect_to_region(
        "us-west-2",  # Esta region es la de Oregon(Gratuita)
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRECT_ACCESS_KEY
    )
    return conn_ec2


def con_db(params):
    import pymysql
    connection = pymysql.connect(host=params['HOST'],
                                 port=params['PORT'],
                                 user=params['USERNAME'],
                                 password=params['PASSWORD'],
                                 database=params['DB'],
                                 local_infile=True)
    return connection


def write_yaml(document):
    import yaml
    name_file = raw_input("Ingrese el nombre del archivo yaml deseado a crear ")
    name_file = name_file + str(".yaml")
    with open(name_file, 'w') as yaml_file:
        yaml.dump(document, yaml_file, default_flow_style=False)
    message = str("Archivo ") + name_file + str(" creado con los parametros de conexion")
    print message


def read_yaml() :
    import yaml
    name_file = raw_input("Ingrese el nombre del archivo yaml deseado a leer ")
    name_file = name_file + str(".yaml")
    with open(name_file, 'r') as yaml_file:
       my_parameters = yaml.load(yaml_file)
    return my_parameters


def define_connect_params():
    instance_name = raw_input('Ingrese nombre de la instancia a crear ')
    database_name = raw_input('Ingrese el nombre de la base de datos a crear ')
    username = raw_input('Ingrese el nombre del usuario ')
    password = raw_input('Ingrese el nombre de la contrasenia ')
    port = int(raw_input('Ingrese el numero de puerto '))

    document = dict(INSTANCE=instance_name, DB=database_name, USERNAME=username, PASSWORD=password, PORT=port)
    write_yaml(document)
    return document


def main():
    instance_name = raw_input('Ingrese nombre de la instancia a crear ')
    database_name = raw_input('Ingrese el nombre de la base de datos a crear ')
    username = raw_input('Ingrese el nombre del usuario ')
    password = raw_input('Ingrese el nombre de la contrasenia ')

    document = dict(INSTANCE=instance_name, DB=database_name, USERNAME=username, PASSWORD=password)

    write_yaml(document)

if __name__ == "__main__":
    main()
