from latch import *
lt = Latch('TwvjPutSWHZEVeNftnbI','LEKFRA6KXO2OFR4FPLo3ywlAMzmF94ufAwKHgTOt')
v = input("Enter your pair key: ")
p = lt.pair(str(v))
d = open('latch.account', 'a')
# write to it (or read from it)
d.write(p.data['accountId'])
d.close()
