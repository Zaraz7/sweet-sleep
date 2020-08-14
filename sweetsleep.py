# А еще это написано на гребанном, блять, vim #

import sys
from smod import volis, getper, cdown

cv = lambda a: (a-1)**2   # Change Value
wifi = 1
sdown = 1
vol = volis()
def timein():   # time input
    while True:
#        try:
            m = float(input('Время, завершения работы (мин): '))
            per = getper(m, vol)
            break
#        except:
#            print('Прости, ты ошибся. П-пожалуйста, напиши число...')
    return per

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
        quit()
    elif com == 'help':
        print('''\
help     выводит это сообщение
start    запускает таймер сна
wifi     вкл/выкл Wi-Fi после таймера
shutdown выкл/вкл отключение сессии
debug    ???
exit     выход из программы''')
    elif com == 'start':
        break
    elif com == 'wifi':
        wifi = cv(wifi)
        if wifi == 0:
            print('Я не буду отключать Wi-Fi')
        else:
            print('Ладно, я его отключу...')
    elif com == 'shutdown':
        sdown = cv(sdown)
        if sdown == 0:
            print('Сессия продолжит работу')
        else:
            print('Хорошо, я закрою за тебя сессию')
    elif com == 'debug':
        print('music:', volis())
        print('wifi:', wifi)
        print('sdown:', sdown)
    else:
        print('Я не знаю такой команды(\nПопробуй help')
cdown(timein(), wifi, sdown)
