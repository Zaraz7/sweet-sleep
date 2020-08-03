# !Код требует доработки! #
# А еще это написано на гребанном, блять, vim

from os import system, getppid
import termux
from time import sleep

def volis(x):    # volume is
    vol = eval(termux.volume())
    music = vol[3].get(x)
    return music 

mvol = volis("volume")
# max volume

while True:
    try:
        sec = 60 * int(input('Время, через которое система прекратит работу (мин): ')) / mvol
        break
    except:
        print('Прости, ты ошибся. П-пожалуйста, напиши число...')

for i in range(mvol, 0, -1):
    sleep(sec)
    com = "termux-volume music " + str(i) 
    system(com)
    print("Volume: " + str(i))

system("termux-wifi-enable false")
system('termux-toast "Сладких снов, хозяин."')
system("kill -9 %d"%(getppid()))
