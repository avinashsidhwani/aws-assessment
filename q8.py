import logging
import pymysql

# logging config
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

# db config
host1 = "av-q8-db.csaruqlxxway.us-east-1.rds.amazonaws.com"
port1 = 3306
db_name = "av_q8_db"
user1 = "av_q8_user"
pwd = "av_q8_password"

# queries
qry_create = "CREATE TABLE Emp(eid int, ename varchar(30))"
qry_insert = "INSERT INTO Emp(eid, ename) VALUES (1, 'user1'),(2, 'user2'),(3, 'user3'),(4, 'user4')"
qry_read = "SELECT * FROM Emp"
qry_update = "UPDATE Emp SET eid = 10, ename = 'user10' WHERE eid = 1"
qry_delete = "DELETE FROM Emp WHERE eid = 2"

# connection object
connectn = pymysql.connect(host=host1, user=user1, password=pwd, db=db_name, port=port1)

try:
    # CREATE operation
    cursr = connectn.cursor()
    cursr.execute(qry_create)
    qry_show = "show tables"
    cursr.execute(qry_show)
    rows = cursr.fetchall()
    for row in rows:
        logger.info(row)
    
    # READ operation
    cursr.execute(qry_insert)
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        logger.info(row)
    
    # UPDATE operation
    cursr.execute(qry_update)
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        logger.info(row)
    
    # DELETE operation
    cursr.execute(qry_delete)
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        logger.info(row)
    
    connectn.commit()
except Exception as e:
    logger.info(e)
finally:
    connectn.close()
