#!/usr/bin/env python3

import binascii
import sys

def main():
	if len(sys.argv) != 2:
		print("[*] Usage: %s <path to dumpfile>" % sys.argv[0])
		print("[*] Example: %s /home/malice/file.dmp"  % sys.argv[0])
		sys.exit(-1)

	dmp_file = sys.argv[1]

	with open(dmp_file, 'rb') as f:
		while True:
			i = 1
			data = binascii.hexlify(f.read(1024))
			if not data: break
			print("[*] %s. Chunk: 0x" + data.decode()) % i

			i += 1

if __name__ == '__main__':
	main()
