#! /usr/bin/env python
#
# privKeyTester.py
#

#WIP: adapting sentinelle.js (by @ericdesa) to my purpose

import argparse
import sys
import bitcoin

def getAddressFromPrivKey(privKey):
	pubKey = bitcoin.fast_multiply(bitcoin.G, privKey)
	address = bitcoin.pubkey_to_address(pubKey)
	return address

def getWalletInfosFromAddress(address):
	pass

def printWalletInfos(walletInfos, printOnlyWhenPositiveBalance, privKey):
    print("balance: %s\n btc. %d\n btc in %i total transactions"
    	%(btcRemaining,btcReceived,nbTransactions))

def testPrivKey(privKey):
	address = getAddressFromPrivKey(privKey)
	walletInfos = getWalletInfosFromAddress(address)
	printWalletInfos(walletInfos, False, privKey)

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description=
		"given a private key, look for its BTC transactions")
	parser.add_argument('privKey',help="private key (32-bytes number in hex)")

	args = parser.parse_args()

	if True: #TODO: if args.privKey is valid
		str_privKey = args.privKey
		privKey = int(str_privKey,16)
	else:
		print("invalid privKey")
		sys.exit(0)

	testPrivKey(privKey)
