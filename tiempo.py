import datetime
import time

inicio = "Empezo "+datetime.datetime.strftime(datetime.datetime.today() , '%d-%m-%Y %H:%M:%S') + " =>"
while True:
	now = datetime.datetime.strftime(datetime.datetime.today() , '%d-%m-%Y %H:%M:%S')
	print(now)
	f = open("info.txt", "w")
	f.write(inicio + " Ultima ejecucion " + now)
	time.sleep( 30 )
