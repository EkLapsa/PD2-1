# Hostname; IP; Latency(ms); Status
nodes = [
"Srv-Web-01;192.168.1.10;15;UP",
"Srv-DB-01;192.168.1.20;450;UP",
"Srv-Backup;10.0.0.5;0;DOWN",
"Workstation-A;192.168.1.105;5;UP",
"Srv-Proxy-01;172.16.0.1;10;up",
"Srv-Mail;10.0.0.10;120;UP",
"Router-Core;192.168.1.1;2;UP",
"Srv-Dev-01;192.168.2.50;500;UP",
"Printer-Main;192.168.1.200;0;down",
"Srv-Log;10.0.0.15;105;UP"
]
skaits = 0

for name in nodes:
    dalas = name.split()
    name = dalas[0].split(";")[0]
    stavoklis = dalas[0].lower().split(";")[3]
    if stavoklis == "up" or "UP" in nodes:
        skaits += 1
        print(name)
print(f"Atrastie serveri: {skaits}")