# Mesh On, Head Out (MOHO)
**A field deployable wireless mobile ad-hoc network platform with compute, 
virtualization, data transformation and software defined network/backplane.**

[![MOHO](img/moho/moho_25p.jpg)](img/moho/moho.jpg)

MOHO is an all-in-one flight-case based edge compute and network backplane 
asset combining all of the elements needed to stand up an Smart Wireless Mesh.

designed containing edge compute capability, network backplane with PoE, fail-over internet connectivity, and AREDN node.

## Notable Contributions

MOHO was developed by [Greg Albrecht W2GMD](http://ampledata.org) for the Bay 
Area Mesh [www.sfwem.net](http://www.sfwem.net).

AREDN is Copyright © 2015-2021 Amateur Radio Emergency Data Network Inc. More 
information on AREDN can be found at [www.arednmesh.org](http://www.arednmesh.org)

Funds for the development of MOHO were provided by a grant from [Amateur Radio Digital Communications (ARDC)](http://ampr.org). 

Experiments with MOHO were conducted at the [Naval Postgraduate School (NPS)](https://www.nps.edu)'s 
[Joint Inter-agency Field Experiment 21-4 (JIFX)](https://nps.edu/web/fx) in 
August 2021.

## Bill of Materials

1. Dell SFF PC: i7/16GB/512SSD
2. [MikroTik hAP ac lite (RB952Ui-5ac2nD-US)](https://www.amazon.com/d/Wireless-Access-Points/MikroTik-Dual-concurrent-Access-Point-RB952Ui-5ac2nD-US/B019PCF3QY) ($49)
3. [Ubiquiti airMAX RocketM 5 GHz BaseStation](https://store.ui.com/collections/wireless/products/rocket-m5) 
   ($89), running the [AREDN](https://www.arednmesh.org/) firmware
4. Ubiquiti Switch
5. Cradlepoint
6. Shallow 2U Flight Case
7. Spare Intel NUC i5 (Debian)

## Motivation

MOHO is an all-in-one flight-case based edge compute and network backplane asset combining all of the elements needed to stand up an smart wireless MANET.
An all-in-one flight case (modeled after the ViaSAT Move Out Jump Out MOJO concept) was designed containing edge compute capability, network backplane with PoE, fail-over internet connectivity, and AREDN node.

The ability for the MOHO to provide management of both the network connectivity, as well as the data flow into and out of the connected networks, allowed for quick reconfiguration of existing data sources and sink across different network segments and services.

For example, some ATAK clients send CoT SA data as UTF-8 encoded UDP Broadcast, while others send Protobuf TLS. Node-RED running on the compute module allowed the CoT data to be automatically translated between these disparate ATAK clients, even across different network segments.

The on-board HAP provided connectivity to the AREDN network, uplink to a WAN network, local DHCP leases. During the event we developed a Node-RED Flow to query sysinfo.json from this local HAP, as well as use it to do auto-discovery of all network nodes, and query their sysinfo.json as well. We fed this sysinfo.json data into Splunk ML, which gave predictive feedback on LoS signal readings into our 

## System Description

### Virtualization & Compute

A small form factor (SFF) computer running Proxmox serves as the primary host 
for a Debian and CentOS virtual machine. Additional virtual machines can be 
added directly to Proxmox, or using Docker within an existing virtual machine. 

### Network Backplane

* Ubiquiti Rocket M5
* EdgeSwitch thing
* HAP

### Data Collection & Analytics

* Node-RED
* Splunk
* InfluxDB

### Situational Awareness

* TAK Server
* ownCloud
* PyTAK Suite
  * adsbxcot
  * aprscot
  * stratuxcot
  * aiscot
  * spotcot
  * inrcot
* RedTAK
* tileserver-gl
