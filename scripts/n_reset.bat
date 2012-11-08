netsh interface set interface "Wireless Network Connection" disabled
ping 1.1.1.1 -n 1 -w 3000 > nul
netsh interface set interface "Wireless Network Connection" enabled

