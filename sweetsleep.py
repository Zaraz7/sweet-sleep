# А еще это написано на гребанном, блять, vim #

from os import system, getppid
from os.path import basename, abspath
from time import sleep
import termux, sys

def volis(x):    # volume is
    vol = eval(termux.volume())
    music = vol[3].get(x)
    return music 
wifi = 1
mvol = volis("volume")  # max volume
getper = lambda a: 60 * a / mvol    # get period
def timein():
    while True:
        try:
            m = float(input('Время, завершения работы (мин): '))
            per = getper(m)
            break
        except:
            print('Прости, ты ошибся. П-пожалуйста, напиши число...')
    return per
def cdown(per):
    print('Запускаю обратный отчет.')
    for i in range(mvol, 0, -1):
        sleep(per)
        com = 'termux-volume music ' + str(i) 
        system(com)
        print("Volume: " + str(i))
    # ending
    bye = 'Сладких снов, хозяин.'
    system('termux-wifi-enable false' * wifi)
    print(bye)
    system('termux-toast "{}"'.format(bye))
    system("kill -9 %d"%(getppid()))

argv = sys.argv
if len(argv) >= 2:
    if argv[1] == '-d':
        print('Использую настройки по умолчанию')
        cdown(getper(30))
    elif  argv[1] == '-h':
        print(argv[0] + \
''' [Option]

-h  Выводит это сообщение
-d  Запустить с настройками по умолчанию (30 мин)
''')
    elif argv[1] == '-s':
        script = open('/data/data/com.termux/files/usr/bin/sweetsleep', 'w')
        script.write('#! /bin/bash\npython3 {}'.format(abspath(__file__)))
        script.close()
        system('chmod +x /data/data/com.termux/files/usr/bin/./sweetsleep')
        abspath(__file__)
    else:
        print('Недопустимая опция: попробуй -h, п-пожалуйста.')
else:

    print(\
'''
#--##-##      *
     #x#             _--_
     #     ..       //   \      •
        .   .      [|
      °             \\\___/
     ,     ,     .    ""   .
 .   !\___/!    .         +
     (0 , 0)
     {  ~  }   .    .   + .
     |     |    #   ##
-----\_____/-_#__#%#### ## #x
------"---"------#&###@#@@#x #
    .        \___x ####7#   x  x
        .         \_#####@#####x
.          .       @ #   ###-##x
     :                    @  .
            SW╒╒T    .
            SL└└P
''')
    while True:
        com = input('> ')
        if com == 'exit':
            break
        elif com == 'start':
            cdown(timein())
        else:
            print('Я не знаю такой команды(')
