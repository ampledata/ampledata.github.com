![Ubiquiti Bullet M2](img/remoteid/bullet.jpg)

# OpenWRT Remote ID Receiver

This guide describes the process of creating a [FAA Remote ID](https://www.faa.gov/uas/getting_started/remote_id) broadcast receiver using commercial off the shelf components, and open-source software. The receiver captures & analyzes Remote ID broadcasts from [compliant](https://uasdoc.faa.gov/listDocs) UAV, UAS, Drones & other unmanned and uncrewed aircraft. Captured Remote ID broadcasts contain pertinant telemetry about the airborne object, including position, operator location, speed, heading & more. Remote ID data is viewed within the Wireshark packet capture software.

There are many [RF waveforms for Remote ID](https://drone-remote-id.com/). This receiver uses the 2.4 GHz WiFi Remote ID waveform - additional waveforms and frequencies are possible with further development.

![CONOP](img/remoteid/wand_conop.png)

## Prerequisites

1. An [OpenWRT](https://openwrt.org/) compatible device with a WiFi chipset that supports [Monitor Mode](https://wiki.wireshark.org/CaptureSetup/WLAN).
2. A computer with [Wireshark](https://www.wireshark.org/) software.
3. A LAN IP network connecting the Wireshark computer & the OpenWRT device.

Compatible & Verified devices:

* [Ubiquiti Rocket M2 2.4 GHz Radio](https://amzn.to/3u01S3S) (AR9342)
* [Ubiquiti Bullet M2 2.4 GHz Radio](https://amzn.to/4aWZrzT) (AR9283)

[Other compatible/unverified devices](https://deviwiki.com/wiki/List_of_Wireless_Adapters_That_Support_Monitor_Mode_and_Packet_Injection)

## Steps

### OpenWRT device

1. Install OpenWRT.
2. Install [tcpdump](https://openwrt.org/docs/guide-user/firewall/misc/tcpdump_wireshark) OPKG (via Internet access or manual copy):

        :::sh linenums=True
        opkg update
        opkg install tcpdump

3. Enable monitor mode:

        :::sh linenums=True
        uci set wireless.@wifi-device[0].disabled=0
        uci commit
        iw phy phy0 interface add mon0 type monitor;
        ifconfig mon0 up
        
### Wireshark computer

1. Install [Wireshark](https://www.wireshark.org/).
2. Install the [Wireshark Remote ID Dissector](https://github.com/opendroneid/wireshark-dissector).
2. Ensure network connectivity to OpenWRT device: `ping 192.168.0.1`
3. Run tcpdump on the OpenWRT host and pipe output to Wireshark, using ssh:

        :::sh linenums=True
        ssh -o StrictHostKeyChecking=no root@192.168.0.1 tcpdump -i mon0 -U -s0 -w - 'not port 22'|\
        /Applications/Wireshark.app/Contents/MacOS/Wireshark -k -i -

> * Change `192.168.0.1` to the IP address of your OpenWRT device.
> * Change  `/Applications/Wireshark.app/Contents/MacOS/Wireshark` to the path to the Wireshark executable on your computer.

## Results

Within Wireshark you should begin to see OPENDRONEID packets in the Protocol column. You can filter for these packets by using the filter: `opendroneid`

![Wireshark displaying Remote ID packet](img/remoteid/wireshark1.png)

### Remote ID packet details

![Wireshark displaying Remote ID packet details](img/remoteid/wireshark_details.png)

### Capture Remote ID with tshark

tshark is Wireshark's command-line tool.

![tshark displaying a decoded Remote ID packet](img/remoteid/tshark.png)

### Capture Remote ID as JSON with tshark

tshark can transform (serialize) Remote ID packets as JSON by adding the `-T json` flag.

![tshark displaying Remote ID packet serialized as JSON](img/remoteid/tshark_json.png)

### Analyze Remote ID with Node-RED

Options:

1. Remote ID can be saved to a JSON file using the `-T json` transform and read-into Node-RED using the `file-in` Node.
2. Remote ID can be transformed to JSON using `-T json` and piped to Node-RED with Netcat & a `tcp-in` Node.
3. Remote ID can be transformed to JSON using `-T json` and piped into Node-RED via an `exec` Node.

![Node-RED displaying Open ](img/remoteid/node-red.png)
