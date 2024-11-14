
from ipaddress import ip_network # Стандартная библиотека

net = ip_network("192.168.32.160/255.255.255.240", strict=False) # Создаем объект сети "ip/маска"

bin_addresses = [f"{address:b}" for address in net] # Все адреса сети переводим в двоичный вид

counter = 0
for address in bin_addresses:
    if address.count("1") % 2 == 0: # Считаем сколько адресов подходят под условие
        counter += 1

print(counter)