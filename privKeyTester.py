#! /usr/bin/env python
#
# privKeyTester.py
#

#WIP: adapting sentinelle.js (by @ericdesa) to my purpose

import argparse
import sys

def getWalletFromPassphrase(passphrase):
	pass

def getWalletInfosFromAddress(address):
	pass

def printWalletInfos(walletInfos, printOnlyWhenPositiveBalance, passphrase):
	pass

def explore(passphraseList, delay):
	pass

def testPrivKey(privKey):
	pass

def addPassphraseToFile(passphrase, filepath):
	pass



if __name__ == "__main__":

	parser = argparse.ArgumentParser(description=
		"given a private key, look for its BTC transactions")
	parser.add_argument('privKey',help="private key ")

	args = parser.parse_args()

	if True: #TODO: if args.privKey is valid
		privKey = args.privKey
	else:
		print("invalid privKey")
		sys.exit(0)

	testPrivKey(privKey)
