#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, request, run, response
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

import urllib,json
import pprint
import decimal, simplejson

#fix json type
class DecimalJSONEncoder(simplejson.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)

#./gcoin/gcoin.conf type rpcuser; rpcpassword; rpcport
RPC_USER = 'bitcoinrpc'
RPC_PASSWORD = '6SWniYid45ph9VFhVPepSzin2oJSsyepWiZKnJitZELD'
rpc_connection = AuthServiceProxy("http://%s:%s@192.168.186.128:58345"%(RPC_USER, RPC_PASSWORD))

LENGTH_CHECK = 64

#listwalletaddress
@route('/listwalletaddress', method='GET')
def listwalletaddress():
        listwalletaddress = rpc_connection.listwalletaddress()
        response.add_header("Access-Control-Allow-Origin", "*")
        return json.dumps(listwalletaddress)

#get tx_id
@route('/tx/<tx_id>', method='GET')
def tx(tx_id=''):
        if len(tx_id) != LENGTH_CHECK:
                return "no tx_id "
        raw_tx = rpc_connection.getrawtransaction(tx_id,1)
        response.add_header("Access-Control-Allow-Origin", "*")
        return raw_tx

#get block_hash
@route('/block/<block_hash>', method='GET')
def block(block_hash=''):
        if len(block_hash) != LENGTH_CHECK:
                return "no block_hash "
        block_hash = rpc_connection.getblock(block_hash)
        block_hash = simplejson.dumps(block_hash,cls=DecimalJSONEncoder)
        response.add_header("Access-Control-Allow-Origin", "*")
        return block_hash

#get blockindex
@route('/blockindex/<block_hash_index>', method='GET')
def blockindex(block_hash_index=''):
        block_hash_index = rpc_connection.getblockhash(int(block_hash_index))
        response.add_header("Access-Control-Allow-Origin", "*")
        return json.dumps({'blockhash': block_hash_index})

#get fixedaddress
@route('/getfixedaddress', method='GET')
def getfixedaddressr():
        getfixedaddress = rpc_connection.getfixedaddress()
        response.add_header("Access-Control-Allow-Origin", "*")
        return json.dumps(getfixedaddress)

#get memberlist
@route('/getmemberlist', method='GET')
def getmemberlist():
        getmemberlist = rpc_connection.getmemberlist()
        response.add_header("Access-Control-Allow-Origin", "*")
        return getmemberlist

#get info
@route('/getinfo', method='GET')
def getinfo():
        getinfo = rpc_connection.getinfo()
        response.add_header("Access-Control-Allow-Origin", "*")
        return getinfo

run(host='0.0.0.0',port=8091,debug='true')
