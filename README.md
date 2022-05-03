# Battmeter
Simple Battery-Monitoring-Script in Python for Linux relying on the [Power Supply Class](https://www.kernel.org/doc/Documentation/power/power_supply_class.txt) `/sys/class/power_supply/`

Just run `python battmeter.py`

The output will look like this and will simply update every second:

     Spannung:  11.594V
     Strom:     1.693A
     Verbrauch: 19.629W
     Temperatur:37.2°C
     
If your charge the laptop the power draw actually will be the charging power.
