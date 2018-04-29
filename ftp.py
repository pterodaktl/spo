import ftplib
import time
from subprocess import call

host = "testuser@example.com"
ftp_user = "testuser"
ftp_password = "password"
filename = "100"




#print(func(r))

print('Начинаем отпрвку первого файла')
time0 = time.time()
con = ftplib.FTP(host, ftp_user, ftp_password)
# Открываем файл для передачи в бинарном режиме
f = open(filename, "rb")
# Передаем файл на сервер
send = con.storbinary("STOR " + filename, f)
# Закрываем FTP соединение
con.close()

time1 = time.time()
deltaftp1 = time1 - time0

print('Начинаем отпрвку 2го файла')
time2 = time.time()
con = ftplib.FTP(host, ftp_user, ftp_password)
# Открываем файл для передачи в бинарном режиме
f = open(filename, "rb")
# Передаем файл на сервер
send = con.storbinary("STOR " + filename, f)
# Закрываем FTP соединение
con.close()

time3 = time.time()
deltaftp2 = time3 - time2

print('Начинаем отпрвку 3о файла')
time4 = time.time()
con = ftplib.FTP(host, ftp_user, ftp_password)
# Открываем файл для передачи в бинарном режиме
f = open(filename, "rb")
# Передаем файл на сервер
send = con.storbinary("STOR " + filename, f)
# Закрываем FTP соединение
con.close()

time5 = time.time()
deltaftp3 = time5 - time4

srtime = (deltaftp1 + deltaftp2 + deltaftp3) / 3
print(round(srtime), "секунд среднее время отправки файла")
