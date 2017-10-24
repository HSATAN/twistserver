# coding=utf8
from twisted.internet import reactor
from eventlet.twistedutil import block_on
from twisted.enterprise import adbapi
import psycopg2
import psycopg2.extras
SQLDB_DSN_MASTER = {
    'w': 'dbname=renhuai user=huangkaijie password=edison host=47.93.5.189',
    'r': 'dbname=renhuai user=huangkaijie password=edison host=47.93.5.189'
}
dbpool=adbapi.ConnectionPool( 'psycopg2',SQLDB_DSN_MASTER['w'], cursor_factory=psycopg2.extras.RealDictCursor)

def getName(email):
    return ( dbpool.runQuery("SELECT * FROM renhuai_user "))

def printResult(result):
    print result
def finish():
    dbpool.close()
    reactor.stop()
d=getName("huangkaijie@qq.com")
d.addCallback(printResult)
reactor.callLater(1, finish)
reactor.run()
