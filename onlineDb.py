import MySQLdb
import helper 

config = helper.read_config()

try:
    bantudb = MySQLdb.connect(user= config['db_credentials']['user'],
                              password= config['db_credentials']['Password'],
                              host=config['db_credentials']['host'],
                              port = 3306,
                              database = config['db_credentials']['database'], 
                              auth_plugin= config['db_credentials']['auth_plugin']
                            
       )
    print("Connection Opened Successfully!")
except (MySQLdb.Error, MySQLdb.Warning) as e:
    print (e)
    print ("nope")



