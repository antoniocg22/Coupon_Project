def get_host(conn_rds, params):
    import time
    import connect_parameters as cp

    myinstance = params['INSTANCE']
    print "La base de datos debe de estar creando. Cuando termine de crearse, se obtendra el host. "
    time.sleep(210)
    flag = True

    while flag == True:
        describe = conn_rds.describe_db_instances(db_instance_identifier=myinstance)
        instances = describe["DescribeDBInstancesResponse"]["DescribeDBInstancesResult"]["DBInstances"]
        for instance in instances:
            if instance['DBInstanceStatus'] != 'creating':
                host = instance['Endpoint']['Address']
                print "Host encontrado"
                flag = False
            else:
                print "La instancia se sigue creando"
                time.sleep(100)

    params['HOST'] = str(host)
    cp.write_yaml(params)

    return params


def main():
    import connect_parameters as cp

    conn_rds = cp.con_rds()
    params = cp.read_yaml()

    get_host(conn_rds, params)

if __name__ == "__main__":
    main()
