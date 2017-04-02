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
rpc_connection = AuthServiceProxy("http://%s:%s@192.168.31.158:58345"%(RPC_USER, RPC_PASSWORD))

LENGTH_CHECK = 64

#gcoin-cli listwalletaddress
@route('/listwalletaddress', method='GET')
def listwalletaddress():
        listwalletaddress = rpc_connection.listwalletaddress()
        response.add_header("Access-Control-Allow-Origin", "*")
        return json.dumps(listwalletaddress)

#gcoin-cli getrawtransaction
@route('/tx/<tx_id>', method='GET')
def tx(tx_id=''):
        if len(tx_id) != LENGTH_CHECK:
                return "no tx_id "
        raw_tx = rpc_connection.getrawtransaction(tx_id,1)
        response.add_header("Access-Control-Allow-Origin", "*")
        return raw_tx

#gcoin-cli getblock
@route('/block/<block_hash>', method='GET')
def block(block_hash=''):
        if len(block_hash) != LENGTH_CHECK:
                return "no block_hash "
        block_hash = rpc_connection.getblock(block_hash)
        block_hash = simplejson.dumps(block_hash,cls=DecimalJSONEncoder)
        response.add_header("Access-Control-Allow-Origin", "*")
        return block_hash

#gcoin-cli getblockhash
@route('/blockindex/<block_hash_index>', method='GET')
def blockindex(block_hash_index=''):
        block_hash = rpc_connection.getblockhash(int(block_hash_index))
        block_hash = {'blockhash ' + str(block_hash_index) : block_hash}
        response.add_header("Access-Control-Allow-Origin", "*")
        return json.dumps(block_hash)

#gcoin-cli getfixedaddress
@route('/getfixedaddress', method='GET')
def getfixedaddressr():
        getfixedaddress = rpc_connection.getfixedaddress()
        response.add_header("Access-Control-Allow-Origin", "*")
        return { "gcoin-cli getfixedaddress": getfixedaddress }
#        return json.dumps(getfixedaddress)

#gcoin-cli getmemberlist
@route('/getmemberlist', method='GET')
def getmemberlist():
        getmemberlist = rpc_connection.getmemberlist()
        response.add_header("Access-Control-Allow-Origin", "*")
        return getmemberlist

#gcoin-cli getinfo
@route('/getinfo', method='GET')
def getinfo():
        getinfo = rpc_connection.getinfo()
        response.add_header("Access-Control-Allow-Origin", "*")
        return getinfo

#gcoin-cli getpeerinfo
@route('/getpeerinfo', method='GET')
def getpeerinfo():
        getpeerinfo = rpc_connection.getpeerinfo()
        response.add_header("Access-Control-Allow-Origin", "*")
        return { "gcoin-cli getpeerinfo": getpeerinfo }

#gcoin-cli getnetworkinfo
@route('/getnetworkinfo', method='GET')
def getnetworkinfo():
        getnetworkinfo = rpc_connection.getnetworkinfo()
        response.add_header("Access-Control-Allow-Origin", "*")
        return getnetworkinfo

#gcoin-cli getmininginfo
@route('/getmininginfo', method='GET')
def getmininginfo():
        getmininginfo = rpc_connection.getmininginfo()
        response.add_header("Access-Control-Allow-Origin", "*")
        return getmininginfo

#gcoin-cli getblockcount
@route('/getblockcount', method='GET')
def getblockcount():
        getblockcount = rpc_connection.getblockcount()
        getblockcount = {'blockcount':getblockcount}
        response.add_header("Access-Control-Allow-Origin", "*")
        return json.dumps(getblockcount)

#gcoin-cli mintforminer
@route('/mintforminer', method='GET')
def mintforminer():
        mintforminer = rpc_connection.mintforminer()
        response.add_header("Access-Control-Allow-Origin", "*")
        return { "tx_id": mintforminer }

#gcoin-cli mintforlicense
@route('/mintforlicense', method='GET')
def mintforlicense():
        mintforlicense = rpc_connection.mintforlicense()
        response.add_header("Access-Control-Allow-Origin", "*")
        return { "tx_id": mintforlicense }

#gcoin-cli getbalance
@route('/getbalance', method='GET')
def getbalance():
        getbalance = rpc_connection.getbalance()
        response.add_header("Access-Control-Allow-Origin", "*")
        return getbalance

#gcoin-cli getlicenseinfo
@route('/getlicenseinfo/<getlicenseinfo_index>', method='GET')
def getlicenseinfo(getlicenseinfo_index=''):
        getlicenseinfo = rpc_connection.getlicenseinfo(int(getlicenseinfo_index))
#        getlicenseinfo = {'getlicenseinfo ' + str(getlicenseinfo_index) : getlicenseinfo}
        response.add_header("Access-Control-Allow-Origin", "*")
        return getlicenseinfo
#        return { "gcoin-cli getlicenseinfo": getlicenseinfo }

#gcoin-cli getlicenselist
@route('/getlicenselist', method='GET')
def getlicenselist():
        getlicenselist = rpc_connection.getlicenselist()
        response.add_header("Access-Control-Allow-Origin", "*")
        return getlicenselist

#gcoin-cli sendlicensetoaddress
#license_comment decode tool https://hanky312.github.io/gcoin-encoder/
license_comment = "721101000547636f696e0547636f696e22314e39534650686f6d63794e466352526e5347746335654433354c445741515671560100000000000000000000000022314e39534650686f6d63794e466352526e5347746335654433354c44574151567156000000000000000000000000000a472d636f696e2e6f72670000000000000000000000000000000000000000000000000000000000000000"
@route('/sendlicensetoaddress/<sendlicensetoaddress_addr>/<sendlicensetoaddress_color>', method='GET')
def sendlicensetoaddress(sendlicensetoaddress_addr='',sendlicensetoaddress_color=''):
        sendlicensetoaddress = rpc_connection.sendlicensetoaddress(str(sendlicensetoaddress_addr),int(sendlicensetoaddress_color),license_comment)
        response.add_header("Access-Control-Allow-Origin", "*")
        return { "tx_id": sendlicensetoaddress }

#gcoin-cli gettxoutaddress
@route('/gettxoutaddress/<gettxoutaddress_address>', method='GET')
def gettxoutaddress(gettxoutaddress_address=''):
        gettxoutaddress = rpc_connection.gettxoutaddress(str(gettxoutaddress_address))
        response.add_header("Access-Control-Allow-Origin", "*")
        return { "gettxoutaddress": gettxoutaddress }

#gcoin-cli validateaddress
@route('/validateaddress/<validateaddress_address>', method='GET')
def validateaddress(validateaddress_address=''):
        validateaddress = rpc_connection.validateaddress(str(validateaddress_address))
        response.add_header("Access-Control-Allow-Origin", "*")
        return validateaddress

run(host='0.0.0.0',port=8091,debug='true')
