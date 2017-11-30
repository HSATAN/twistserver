# coding=utf8
from __future__ import print_function
from twisted.internet import reactor
#from eventlet.twistedutil import block_on
from twisted.enterprise import adbapi
import psycopg2
from datetime import datetime
import psycopg2.extras
SQLDB_DSN_MASTER = {
    'w': 'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.133',
    'r': 'dbname=renhuai user=huangkaijie password=edison host=47.93.5.189'
}
dbpool=adbapi.ConnectionPool('psycopg2',SQLDB_DSN_MASTER['w'], cursor_factory=psycopg2.extras.RealDictCursor)


def _run_query(transaction, operation, *args, **kwargs):
    transaction.execute(operation, *args, **kwargs)
    return transaction.fetchall()

def getName():
    return (dbpool.runInteraction(_run_query, "SELECT * FROM pw_user limit 1 "))

def printData(data):
    print(data[0])

    print(data[0]['signup_time'].hour)

d = getName()
d.addCallback(printData)

reactor.run()