# OpenWRT Remote ID Receiver

This guide describes the process of creating a FAA Remote ID receiver using commercial off the shelf components and open source software. This receiver captures & analyzes Remote ID beacons from FAA compliant UAV, UAS, Drones & other unmanned and uncrewed aircraft. Captured Remote ID beacons contain pertinant telemetry about the airborne object, including position, operator location, speed, heading & more. Remote ID data is viewed within the Wireshark packet capture software.

There are many RF waveforms for Remote ID. This receiver uses the 2.4 GHz WiFi Remote ID waveform - additional waveforms and frequencies are possible with further development.

## Prerequisites

1. An OpenWRT compatible device with a WiFi chipset that supports Monitor Mode.
2. A computer with Wireshark software.
3. A LAN IP network connecting the Wireshark computer & the OpenWRT device.

## Steps

### OpenWRT device

1. Install OpenWRT.
2. Install tcpdump OPKG (via Internet access or manual copy): `opkg update;opkg install tcpdump`

### Wireshark computer

1. Install Wireshark.
2. Ensure network connectivity to OpenWRT device: `ping 192.168.0.20`
3. Download the openwrt_remoteid.sh script.
4. Run the openwrt_remoteid.sh command: `bash openwrt_remoteid.sh 192.168.0.20`