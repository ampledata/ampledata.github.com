# Oro Net

Oro Net is still under development. For more information please contact:

- Greg Albrecht W2GMD
- Email: <a href="mailto:oro-net@undef.net">oro-net@undef.net</a>
- Phone: 310-621-9598


## Concept: An 'APRS of Things'

Oro Net is an Amateur Radio-based telemetry & messaging system for dense urban environments. It is build using Commercial-off-the-Shelf (COTS) equipment and uses the Automatic Packet Reporting System (APRS) network and protocols.

Oro Net should allow transmitting stations ("things") to broadcast any type of message or telemetry from any location at any time and have it received and delivered to the APRS-IS network. This is accomplished using numerous receiver stations dispersed in an urban geographic area.

Current generations of Oro Net Receiver Nodes are built using the Raspberry Pi single-board computer and the RTL-based Software Defined Radio (SDR). A bill-of-materials is forthcoming.

Oro Net is named for the motto on San Francisco's flag: "Oro en paz. Fierro en guerra.".


### Frequently Asked Questions (FAQ)

- Q: Why not use the existing APRS network?
- A: The existing APRS network:
  * Does not penetrate dense urban environments well.
  * Is over subscribed with powerful (5w+) Mobile stations.


- Q: Why not build digipeaters instead?
- A: Digipeaters would only add to the existing network congestion and would require an Amateur Radio Operating License, where-as the Oro Net is a receive-only network, thus requiring no Amateur license.


- Q: Why not OTHER_SINGLE_BOARD_COMPUTER (Odroid, Beagle, etc.)?
- A: The RPi is the reference design for this project. Any internet-connected computer should work. For the interest of power, heat and size, consider any ARM single-board computer.


- Q: Do I need an Amateur Radio License to participate?
- A: Yes and No. To transmit on Amateur Radio frequencies you need a license. To receive Amateur Radio frequencies you do not need a license.


### Diagram

```
[APRS Transmitter] >~~~RF~~~> [RTL_SDR]->[RPi]->[APRS-IS]
```


### Cost & Bill-of-Materials (BOM)

BOM:

- Raspberry Pi: $35
- RTL SDR: $15 ($5~$20)
- VHF Antenna: $9 ($9~$20)
- SMA-MCX Adaptor: $6 ($6~$10)
- USB WiFi Adaptor: $3 ($3~$8)
- 8GB Micro SD: $4 ($4~$6)
- 5V 2A Power Supply: $6 ($2~$6)
- Pelican 1010 Case: $10 ($10~$14)

Total Cost: $88

Range: $74-$120


### Similar projects:

* ADS-B Receiver Networks (e.g. <a href="http://flightaware.com/adsb/piaware/build">PiAware</a>).
* AIS Receiver Networks (e.g. <a href="http://www.satsignal.eu/raspberry-pi/AIS-receiver.html">AIS Receiver for RPi</a> and <a href="http://www.stripydog.com/kplex/examples/marinetraffic.html">RPi Marine Traffic Server</a>).


### Current Oro Net Nodes:

- <a href="http://aprs.fi/info/a/ORO01">ORO01</a>: Initial Proof-of-Concept Node in San Francisco's Mission District.
