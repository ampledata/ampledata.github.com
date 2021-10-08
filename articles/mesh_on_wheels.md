# Mesh on Wheels (MoW)
**A portable Smart Wireless Mesh node with edge compute, data transformation & 
sensor capability.**

[![MoW with solar panel mounted on a vehicle roof](img/mow/roof_25p.jpg)](img/mow/roof.jpg)

Mesh on Wheels (MoW) is a portable vehicle mountable Smart Wireless Mesh 
“node”. The MoW is capable of connecting to & extending a mobile ad-hoc network 
(MANET) and enabling edge-compute, ISR data transformation, sensor/IoT, SDN & 
SDR. MoW includes an on-board solar-charge controller and batteries, allowing 
for power on-the-go or fixed installation.

MoW was developed by [Greg Albrecht W2GMD](http://ampledata.org) for the Bay 
Area Mesh [www.sfwem.net](http://www.sfwem.net).

AREDN is Copyright © 2015-2021 Amateur Radio Emergency Data Network Inc. More 
information on AREDN can be found at [www.arednmesh.org](http://www.arednmesh.org)

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
11. Pelican-style rugged outdoor enclosure
12. "fish tank grids" for structural reinforcement

A follow-up design included a Ubiquiti NanoBeam to offload establishing an 
IP-tunnel connection to a larger mesh network.

## System Description
[![MoW systems diagram](img/mow/systems_diagram_50p.png)](img/mow/systems_diagram.png)

### Mesh radio

The mesh radio sub-system consists of a Ubiquiti Rocket M5 5 GHz wireless 
radio running the AREDN mesh firmware and an off-the-shelf omnidirectional 
MIMO 5 GHz antenna permanently mounted to the lid of a Pelican-style rugged 
enclosure.

### Power

The power sub-system consists of a solar panel, solar charge controller and 
batteries. Run-time & power consumption can be tuned to meet mission need by 
adding or removing other sub-components (such as environmental sensors or 
edge-compute). Given sufficient sunlight a MoW can run unattended for an 
indefinite amount of time.

[![SolarSwitch UI](img/mow/solarswitch_25p.png)](img/mow/solarswitch.png)

The Ubiquiti SolarSwitch was chosen based on familiarity with existing Ubiquiti 
products, and was compelled by features like web administration, power 
customization, real time readout, and SNMP. Batteries are two 12 VDC SLA 
batteries in series to produce 24 VDC. 

Special thanks to Adam O'Donnell N3RCS for contributing the solar panel used in 
the proof-of-concept prototype MoW.

### Edge Compute

[![MoW Data Flow Diagram](img/mow/data_flow_diagram_25p.png)](img/mow/data_flow_diagram.png)

Edge compute capabilities are provided by a Raspberry Pi running Raspberry OS 
with Node-RED. This allows for a rapid SA or ISR data-pipeline reconfiguration, 
fitting new mission or end-user needs. 

For example, the on-board SDR can be quickly tasked to receive and parse 
aircraft ADS-B, making it available to all users of the connected MANET through 
their COP or SA platform of choice (ATAK, WinTAK, etc).

[![Node-RED UI](img/mow/nodered_25p.png)](img/mow/nodered.png)

The addition of a GPS and SDR allowed real-time RF intercept and positional 
data to be collected and transformed locally or back-hauled to a a InfluxDB or 
Splunk data collection system.

[![Real-time InfluxDB graph](img/mow/influxdb_25p.png)](img/mow/influxdb.png)

[![uRadmonitor UI](img/mow/urad.png)](img/mow/urad.png)


