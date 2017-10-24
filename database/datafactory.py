# coding=utf8
from __future__ import print_function
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


def _run_query(transaction, operation, *args, **kwargs):
    transaction.execute(operation, *args, **kwargs)
    return transaction.fetchall()

def getName():
    return ( block_on(dbpool.runInteraction(_run_query, "SELECT * FROM renhuai_user ")))

def finish():
    dbpool.close()
    reactor.stop()

print(getName())
reactor.callLater(1, finish)
reactor.run()