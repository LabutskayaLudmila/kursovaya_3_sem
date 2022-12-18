from win32process import EnumProcesses
from win32api import OpenProcess

print(EnumProcesses())  # получает id процессов
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000  #просто 16-ная константа, позволяющая просить разные уровни доступа
p = OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, 1976)  # присоединяемся к процессу. (уровень доступа (у нас лайт), ..., pid)
# глубоко в си, какие-то токены, системы отладки.... проблема началась с винды 8
# нам все это нужно для handle, без него мы никто))
# винда не пускает!!!!
