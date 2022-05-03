import subprocess, time

while True:
    voltage = open("/sys/class/power_supply/BAT0/voltage_now","r").read().splitlines()
    voltage = float(voltage[0])/1000000

    current = open("/sys/class/power_supply/BAT0/current_now","r").read().splitlines()
    current = float(current[0])/1000000

    watt = round(voltage * current, 3)

    temp = open("/sys/class/power_supply/BAT0/temp","r").read().splitlines()
    temp = float(temp[0])/10

    print("Spannung:  "+str(voltage)+"V")
    print("Strom:     "+str(current)+"A")
    print("Verbrauch: "+str(watt)+"W")
    print("Temperatur:"+str(temp)+"°C")
    print()
    time.sleep(1)
