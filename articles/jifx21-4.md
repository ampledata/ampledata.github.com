# The Smart Wireless MANET
**An off-the-shelf network with edge compute and IoT capabilities.**

![JIFX 21-4 Systems Overview](file:///Users/gba/Projects/Blog/ampledata.github.com/img/jifx21-4/jifx21-4_systems_overview.png)

## Background

In August 2021 the San Francisco Wireless Emergency Mesh (SFWEM) participated 
in the week-long Naval Postgraduate School (NPS) Joint Inter-agency Field 
Experiment 21-4 (JIFX). Held quarterly at two facilities in California, JIFX 
provides several environments for experimentation, including fresh and 
saltwater tanks, an airfield, simulated cities and villages, and natural 
California hills & terrain. Every JIFX incorporates stakeholders from multiple 
different agencies across different disciplines within the federal government, 
defense department and other groups.

SFWEM conducted several experiments in collaboration with California State 
University Bakersfield’s Fab Lab, Splunk & Orion Labs. Each experiment explored 
the capabilities of a Smart Wireless Mesh across a variety of different 
missions: disaster response, situational awareness/common operating picture 
(SA/COP), unmanned vehicle command & control (C2), sensor data collection, 
real-time communication & collaboration, field experience & rapid deployment. 
Several novel capabilities were also uncovered over the course of the 
experiment week.

### Project Collaborators

- Bobby Hartsock KJ6YOA, Fab Lab at California State University Bakersfield
- Vivian Richards, Splunk
- Greg Albrecht W2GMD, SFWEM & Orion Labs

## Motivation

SFWEM utilizes commercial off-the-shelf (COTS) wireless networking equipment 
typically running the Amateur Radio Emergency Data Network (AREDN) firmware. 
AREDN transforms COTS equipment into resilient auto-configuring mobile ad-hoc 
network (MANET) nodes that can provide high-speed wireless IP connectivity 
across multiple hops, supports being hastily assembled (HFN) and dynamically 
reconfigured. Regional AREDN networks have been deployed around the work, and 
represent both steady-state/always-on infrastructure and field-deployable 
systems.

Piloting of a Unmanned Ground System (UGS) typically requires an IP based 
connection to a Ground Control Station (GCS). Similarly UGS sub-systems like 
the video feed from an on-board camera or ISR systems require IP connectivity 
to a display or collection device. This reliance on IP networking can limit the 
range of a UGS as it is constrained by the ability to establish a route between 
a UGS & GCS. AREDN can provide a UGS with IP networking & backhaul on-the-move, 
allowing both remote piloting and video streaming between the UGS & GCS. 
Additionally, because each UGS was also itself a AREDN node, every UGS is also 
able to extend the range of the existing network; combined with another UGS 
this allow a multi-hop ‘swarm’ like system were multiple different UGS could 
be augmenting each others IP network connectivity on-the-move.

Situational Awareness (SA) platforms like ATAK & WinTAK can be configured to 
share data via a local-only IP network, or pass data out to another network 
segment or to a TAK Server. AREDN allows ATAK users on-the-move to be 
continuously connected to other ATAK users, or can be configured to backhaul SA 
traffic to forward-deployed or centralized TAK Servers.

The RedTAK “Tactical Data Switchboard” or “Tactical ETL” was developed using 
Node-RED. RedTAK allows SA data like Cursor on Target (CoT), as well as 
operational data from Mesh nodes, and piloting data from the UGS, to be 
streamed into Splunk for collection & processing through machine learning.

The ability to collect both SA and operational data from participants in the 
Smart Wireless Mesh lends itself to the use of machine learning (ML) to make 
predictions about changing network and end-user (or end-device) conditions. For 
example, a signal strength reading from a mesh radio can indicate an upcoming 
Loss of Signal (LoS) event, which is critical information to the pilot of a 
GS. Splunk and Splunk ML allow for the collection of and learning from all of 
this data. Splunk also allows for the input and processing of novel data, which 
can be used to measure user inputs, for example a Damage Assessment (DA) report 
sent via smartphone application, or spoken aloud through a PTT platform like 
Orion.

## Conclusions

Using commercial off-the-shelf hardware and open source software it is possible
to establish a field expedient Smart Wireless MANET within a near-austere 
environment. With minimal up-front planning, this network can be used for 
unmanned system command & control, real-time multimedia communication, and 
internet of things or ISR applications.

## Details

### Proof-of-Concepts

Several Smart Wireless Mesh proof-of-concepts were fielded at JIFX, with 
several novel designs coming from collaboration with other JIFX participants & 
stakeholders. Some of these concepts addressed the areas of mobile on-the-go 
connectivity, edge compute, body worn networks, et al.

1. Unmanned Ground System Command, Control (C2) & Communication (C3) using mesh
2. Situational Awareness (SA), ISR & operational data collection & analysis using mesh
3. Field Expedient Mesh (“FEM”)
4. Mesh on Wheels (“MoW”)
5. Mesh On, Head Out (“MOHO”)
6. Human Attached Mesh Portable Radio (“HAMPR”)
7. Compact Rugged Unattended Mesh Box (“CRUMB”)
8. Tactical ETL

### Data

Operational data was collected from UGS’, mesh radios and ATAK clients. During 
experimentation several sources and sinks for data collection lead to 
in-the-field data transformation changes using our Node-RED based data 
pipeline. From there data was sent two one of two primary data sinks: Splunk & 
InfluxDB, with data being mirrored to COPERS. Systems that were capable of 
full-duplex data transfer were integrated so that every system could share the 
common operating picture in their native representation. Systems that were 
capable of intelligent message understanding were also able to interact through 
data or multimedia channels.

![JIFX 21-4 Data Flow Diagram](file:///Users/gba/Projects/Blog/ampledata.github.com/img/jifx21-4/jifx21-4_data_flow_diagram.png)


#### Splunk

Splunk collected all operational & SA data originating from and passing through 
the concepts fielded at JIFX 21-4. Early operational questions could be quickly 
answered with the data collected by Splunk, including tracking wireless signal 
anomalies and alerting operators to potential Loss of Signal (LoS) conditions. 
Damage Assessment reports were submitted using the ATAK WASP Plugin, which were 
then displayed on a map in real-time using a Splunk dashboard.

![JIFX 21-4 Damage Assessment statistics displayed on a map](file:///Users/gba/Projects/Blog/ampledata.github.com/img/jifx21-4/jifx21-4_damage_assessment.png)

A procedure was developed on-site to transform ArduPilot Mission Planner UGS 
location positioning data into Cursor on Target, a format used by Splunk, ATAK 
and others. In this procedure, WinTAK running on the GCS computer was used as a 
NMEA to CoT gateway. Effort was made to analyze real-time UGS operational data 
in Splunk by utilizing a Mavlink decoder with limited success.

![JIFX 21-4 UGS PLI displayed within a TAK client](file:///Users/gba/Projects/Blog/ampledata.github.com/img/jifx21-4/jifx21-4_ugs_tak.png)

### Hardware & Software

Ubiquiti Rocket M5 5 GHz radios were used universally in this experiment, all 
of which had been updated to use the AREDN mesh firmware. Radios operated in 
the Part TK portion of the 5 GHz band.

More information on ATAK, WinTAK & TAK Server can be found at www.tak.gov

#### Portable UGS ground control station (GCS)

![JIFX 21-4 UGS GCS](file:///Users/gba/Projects/Blog/ampledata.github.com/img/jifx21-4/jifx21-4_ugs_gcs.jpg)

The Portable GCS comprised the computer, software and hardware required to 
control the UGS. Piloting and Mission Planning utilized ArduPilot, “an open 
source, unmanned vehicle Autopilot Software Suite”. Manual UGS piloting 
utilizing a Logitech F310 Gamepad USB controller attached to the GCS computer, 
a Dell Latitude 12 Rugged Tablet (7202) running Windows 10. On-screen UGV video 
was transcoded & displayed using ffmpeg, VLC & gstreamer.

Additionally, WinTAK was used to transform UGS positioning data into a format 
compatible with other TAK systems, see note under Data > Splunk.

### Ad-Hoc Experimentation

NPS encouraged and promoted ad-hoc and collaborative experimentation between 
participants at every JIFX. Several novel concepts were fielded, many of which 
were developed on-site and in the field.

#### UGS mounted LIDAR & Underground Mesh

![JIFX 21-4 UGS-mounted LIDAR](file:///Users/gba/Projects/Blog/ampledata.github.com/img/jifx21-4/jifx21-4_ugs_lidar.jpg)

Working with Exyn, another JIFX participant, CSUB reconfigured a UGS to support 
carrying a LIDAR scanner payload. Once the payload was mounted, UGS were loaded 
with a Mission Plan to traverse an underground tunnel. An unexpected but 
recoverable failure encountered during this mission was the navigation and IMU 
fail safes built into the UGS Mission Planning software. This fail safe was 
encountered due to the GPS denied nature of an underground tunnel, and its 
curved walls causing a significant delta in vehicle pitch. Once bypassed the 
mission could succeed. 

Piloting the UGS into a tunnel also required extending the mesh network into an 
underground, network-denied environment. This was accomplished using several 
Compact Rugged Unattended Mesh Box (CRUMBs) placed strategically around the 
tunnel complex, each extending the mesh into the tunnel and allowing continuous 
3 while underground. 

## TK

Node-RED Flows Developed

tileserver-ns usage?
Splunk usage.
Orion use
Twilio use
RedTAK Use

JS8Call use
	Used REST API to feed into Node-RED. Node-RED transformed Maidenhead and callsign into CoT, which it then sent out to TAK Server. (Actually FT8)

InfluxDB usage
Collected & displayed local sensor data from AQI sensors.



RedTAK
Node-RED
node-red-contrib-worldmap
node-red-contrib-tcp-tls (developed for TAK)
Misc other code
RedTAK is an installation of Node-RED with Flows adapted for interoperability with other applications in the ‘TAK’ ecosystem, including ATAK, TAK Server, WinTAK, TAK Tracker, iTAK, et al. Specifically RedTAK provides a web-based map displaying CoT PLI, methods for connecting securely to TAK clients & servers, and the ability to represent CoT as native JSON.

RedTAK can run on any system capable of running Node-RED, such as small board computers like the Raspberry Pi, higher-end small form factor computers like the Intel NUC, even Android smartphones can run Node-RED.



Ad Hoc Experimentation
Send SA data to COPRS.
Send SA data to Splunk.
Send Mavlink data to Splunk [incomplete].
Read Mavlink data in Node-RED [incomplete].
Send Mission Planner control data to TAK Server via WinTAK.
Send AREDN sysinfo.json data to Splunk.
Read AREDN sysinfo.json data in Node-RED.
Scan AREDN networks in Node-RED.
Resolve AREDN specific DNS in Node-RED.
Add APRS Icons to Node-RED.
Add APRS Icons to ATAK.
Data Package into TAK Tracker.
Node-RED reading from TAK Server.
Node-RED decoding protobufs.
Adding adsbx, aprs feeds to COPRS.
Sending UGV data to COPRS.
