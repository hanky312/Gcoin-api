#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import pprint

RPC_USER = 'bitcoinrpc'
RPC_PASSWORD = '6SWniYid45ph9VFhVPepSzin2oJSsyepWiZKnJitZELD'

rpc_connection = AuthServiceProxy("http://%s:%s@192.168.186.128:58345"%(RPC_USER, RPC_PASSWORD))

memberlist = rpc_connection.getmemberlist()
print "memberlist:"
pprint.pprint(memberlist)

walletaddress = rpc_connection.listwalletaddress()
print "My wallet:"
pprint.pprint(walletaddress)

