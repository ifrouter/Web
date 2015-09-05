import md5
import struct
import binascii
count=8192

itoa64 = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def encode64(input,cnt=16):
	output=''
	i=0
	while (i<cnt):
		value = ord(input[i])
		i = i+1
		output = output + itoa64[value&0x3f]

		if(i<cnt):
			value |= ord(input[i])<<8
		output = output + itoa64[(value>>6)&0x3f]

		if(i >= cnt):break
		i = i+1
		if(i<cnt):
			value |= ord(input[i])<<16
		output = output + itoa64[(value>>12)&0x3f]

		if(i >= cnt):break
		i = i+1
		output = output + itoa64[(value>>18)&0x3f]

	return output
def decode64(input):
	output=''
	i=0
	cnt = len(input)
	value = 0
	while (i<cnt):
		value=itoa64.find(input[i])
		i=i+1
		if(i >= cnt):break
		value |= itoa64.find(input[i])<<6

		i=i+1
		if(i >= cnt):break
		value |= itoa64.find(input[i]) <<12

		i=i+1
		if(i >= cnt):break
		value |= itoa64.find(input[i]) <<18
		output = output + struct.pack('<I',value)[0:3]

		i=i+1
	return output+ struct.pack('<I',value)[0]

def wp_hash(salt,password):
	hash=md5.md5(salt+password)

	for i in range(count):
		hash = md5.md5(hash.digest()+password)

	print hash.hexdigest()
	print encode64(hash.digest())

def bin2hex(input):
	return ''.join('%02x' % ord(c) for c in input)
if __name__ == '__main__':
    #test $P$Bat/4YEzkmzJMTWoFKaJlCOO1DAwUc.
    # $P$    B    at/4YEzk    mzJMTWoFKaJlCOO1DAwUc.
    #sign = '$P$'
    #count = 1<<itoa64.index('B')

 	wp_hash('at/4YEzk','123456')
  	x=decode64('mzJMTWoFKaJlCOO1DAwUc.')
 	print bin2hex(x)

