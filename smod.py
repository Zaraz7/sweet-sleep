from time import sleep
from os import system, getppid
from os.path import abspath
import sys
import termux

def volis():    # volume is
    vol = eval(termux.volume())
    music = vol[3].get('volume')
    return music

getper = lambda m, v: 60 * m / v

def cdown(per, wifi = 1, sdown = 1):
    print('Запускаю обратный отчет.')
    vol = volis()
    for i in range(vol, 0, -1):
        sleep(per)
        com = 'termux-volume music ' + str(i)
        system(com)
        print("Volume: " + str(i))
    # endin
    system('termux-wifi-enable false' * wifi)
    print('Сладких снов, хозяин.')
    system(("kill -9 %d"%(getppid())) * sdown)

argv = sys.argv
if len(argv) >= 2:
    if argv[1] == '-d':
        print('Использую настройки по умолчанию')
        cdown(getper(30))
    elif  argv[1] == '-h':
        print(argv[0] + ' [Option]\n-h  Выводит это сообщение\n-d  Запустить с настройками по умолчанию (30 мин)')
    elif argv[1] == '-s':
        script = open('/data/data/com.termux/files/usr/bin/sweetsleep', 'w')
        script.write('#! /bin/bash\npython3 {}'.format(abspath(__file__)))
        script.close()
        system('chmod +x /data/data/com.termux/files/usr/bin/./sweetsleep')
    else:
        print('Недопустимая опция: попробуй -h, п-пожалуйста.')
