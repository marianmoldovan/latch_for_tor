from latch import *
import os

def write(file, value):
	with open(file, "wt") as out_file:
		out_file.write(value)

def read(file):
	with open(file, "rt") as in_file:
		return in_file.read()

old = True
if 'off' in str(read('latch.status')):
	old = False
account = str(read('latch.account'))
print(old)

lt = Latch('appId','SecretKey')
a = lt.status(account)

new = True
if len(str(a.data['operations']['TwvjPutSWHZEVeNftnbI']['status'])) > 2:
	new = False

if new:
	print("status is off, turning on")
	os.putenv("http_proxy","http://127.0.0.1:8118")
	os.putenv("https_proxy","http://127.0.0.1:8118")
	os.putenv("HTTP_PROXY","http://127.0.0.1:8118")
	os.putenv("HTTPS_PROXY","http://127.0.0.1:8118")
	os.system('bash')
	os.system("echo 'on' > latch.status")
	os.system('bash')
elif not new:
	print("status is on, turning off")
	os.unsetenv("http_proxy")
	os.unsetenv("https_proxy")
	os.unsetenv("HTTP_PROXY")
	os.unsetenv("HTTPS_PROXY")
	os.system('bash')
	os.system("echo 'off' > latch.status")
	os.system('bash')
print(new)
