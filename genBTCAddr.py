#! /usr/bin/env python
#
# just glueing chunks of code to better understand how bitcoin addresses work
# (https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses)
#

import argparse

# [i] from: https://bitcoin.stackexchange.com/questions/25024/how-do-you-get-a-bitcoin-public-key-from-a-private-key

class Point(object):
	def __init__(self, _x, _y, _order = None): self.x, self.y, self.order = _x, _y, _order

	def calc(self, top, bottom, other_x):
		l = (top * inverse_mod(bottom)) % p
		x3 = (l * l - self.x - other_x) % p
		return Point(x3, (l * (self.x - x3) - self.y) % p)

	def double(self):
		if self == INFINITY: return INFINITY
		return self.calc(3 * self.x * self.x, 2 * self.y, self.x)

	def __add__(self, other):
		if other == INFINITY: return self
		if self == INFINITY: return other
		if self.x == other.x:
			if (self.y + other.y) % p == 0: return INFINITY
			return self.double()
		return self.calc(other.y - self.y, other.x - self.x, other.x)

	def __mul__(self, e):
		if self.order: e %= self.order
		if e == 0 or self == INFINITY: return INFINITY
		result, q = INFINITY, self
		while e:
			if e&1: result += q
			e, q = e >> 1, q.double()
		return result

	def __str__(self):
		if self == INFINITY: return "infinity"
		return "04%x%x" % (self.x, self.y)

def inverse_mod(a):
	if a < 0 or a >= p: a = a % p
	c, d, uc, vc, ud, vd = a, p, 1, 0, 0, 1
	while c:
		q, c, d = divmod(d, c) + (c,)
		uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc
	if ud > 0: return ud
	return ud + p

# [ii] from: https://stackoverflow.com/questions/47319779/generating-bitcoin-key-pair-in-python-3-6-from-public-key-to-public-address

import hashlib
import base58

def hash160(hex_str):
	sha = hashlib.sha256()
	rip = hashlib.new('ripemd160')
	sha.update(hex_str)
	rip.update( sha.digest() )
	#print ( "key_hash = \t" + rip.hexdigest() )
	return rip.hexdigest()  # .hexdigest() is hex ASCII

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description=
		"given a private key, generate its public key and bitcoin address")
	parser.add_argument('privKey',help="private key. 0x prefix needed")
	parser.add_argument('--compressed',action='store_true',help="public key in compressed form")

	args = parser.parse_args()

	# secp256k1
	p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
	INFINITY = Point(None, None)

	### 1. set privKey,g -> pubKey

	#In Bitcoin, a private key is a single unsigned 256 bit integer (32 bytes).
	privKey = int(args.privKey,0)
	g = Point(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
			0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
			0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
	hex_str_pubKey = str(g * privKey)
	pubKey = int(hex_str_pubKey,16)
	# See 'compressed form' at https://en.bitcoin.it/wiki/Protocol_documentation#Signatures
	compress_pubKey = args.compressed

	### 2. print privKey, pubKey

	print('privKey (hex format) = \t' + hex(privKey))
	print('pubKey = \t\t' + hex(pubKey))

	### 3. pubKey -> btc-address

	if (compress_pubKey):
		if (ord(bytearray.fromhex(hex_str_pubKey[-2:])) % 2 == 0):
			pubKey_compressed = '02'
		else:
			pubKey_compressed = '03'
		pubKey_compressed += hex_str_pubKey[2:66]
		hex_str = bytearray.fromhex(pubKey_compressed)
	else:
		hex_str = bytearray.fromhex(hex_str_pubKey)

	# Obtain key:
	key_hash = '00' + hash160(hex_str)

	# Obtain signature:
	sha = hashlib.sha256()
	sha.update( bytearray.fromhex(key_hash) )
	checksum = sha.digest()
	sha = hashlib.sha256()
	sha.update(checksum)
	checksum = sha.hexdigest()[0:8]

	# Obtain btc-address:
	bctAddress = base58.b58encode( bytes(bytearray.fromhex(key_hash + checksum))).decode('utf-8')

	### 4. print bct-address

	#print ( "checksum = \t" + sha.hexdigest() )
	#print ( "key_hash + checksum = \t" + key_hash + ' ' + checksum )
	print ( "BTC-address = \t\t" +  bctAddress)
