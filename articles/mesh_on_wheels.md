# Mesh on Wheels (MoW)
**A Smart Wireless Mesh node with edge compute, data transformation, sensors & IoT.**

[![MoW with solar panel mounted on a vehicle roof](img/mow/roof_25p.jpg)](img/mow/roof.jpg)

Mesh on Wheels (MoW) is a portable vehicle mountable Smart Wireless Mesh 
“node”. The MoW is capable of connecting to a mobile ad-hoc network (MANET) and 
enabling edge-compute, data transformation, sensor/IoT, SDN & SDR. Other 
capabilities include an on-board solar-charge controller and batteries.

Developed by [Greg Albrecht W2GMD](http://ampledata.org) for the Bay Area Mesh 
[www.sfwem.net](http://www.sfwem.net).

AREDN is Copyright © 2015-2021 Amateur Radio Emergency Data Network Inc. 
More information on AREDN can be found at [www.arednmesh.org](http://www.arednmesh.org)

## Bill of Materials
[![Internal contents of the MoW](img/mow/mow_inside_25p.jpg)](img/mow/mow_inside.jpg)

The bill of materials (BoM) is primarily sourced from commercial off-the-shelf 
(COTS) components.
1. [Ubiquiti SunMAX SolarSwitch](https://store.ui.com/collections/solar/products/sunmax-solarswitch) 
   solar charge controller (SCC) ($199)
2. [Ubiquiti airMAX RocketM 5 GHz BaseStation](https://store.ui.com/collections/wireless/products/rocket-m5) 
   ($89), running the [AREDN](https://www.arednmesh.org/) firmware
3. [Raspberry Pi](https://www.adafruit.com/product/3055): [Node-RED](https://nodered.org/) 
   & local compute
4. [HackRF](https://www.adafruit.com/product/3583): Wideband software defined 
   radio (SDR) ($339.95)
5. [uRadMontior model A3](https://www.uradmonitor.com/products/): Environment 
   & air quality monitoring station ($549.00)
6. [12V to 5V DC Converter Buck Module](https://smile.amazon.com/Converter-Module-Output-Adapter-Regulator/dp/B08RBWX2GL) ($9.99)
7. 24 VDC (2x 12 VDC) SLA batteries in series
8. Wideband Receive Antenna
9. Omnidirectional MIMO 5.8 GHz Antenna
10. Solar Panel(s)

A follow-up design included a Ubiquiti NanoBeam to offload establishing an 
IP-tunnel connection to a larger mesh network.

## Sub-systems & Descriptions
[![MoW systems diagram](img/mow/systems_diagram_25p.jpg)](img/mow/systems_diagram.jpg)

Mobile node is a self-contained AREDN node, AQI & Meteorology sensor, software 
defined radio (SDR) and compute node; powered by an on-board solar charge 
controller. Alone it is capable of running at configurable levels of battery 
consumption, combined with a solar power it could run indefinitely.

The power sub-system is made up of the SCC & the battery, with an optional 
solar panel. Our selection of the Ubiquiti SolarPoint for our SCC was based on 
familiarity with existing Ubiquiti products, and was compelled by features like 
web administration, power customization, real time readout, and SNMP. Batteries 
are two 12 VDC SLA batteries in series to produce 24 VDC. Solar panel is via 
Adam O’donnell TK and is a 100 W xxxx TK.
