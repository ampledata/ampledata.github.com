# The Smart Wireless Mesh
**An off-the-shelf mobile ad-hoc network with edge compute and IoT capabilities.**

![JIFX 21-4 Systems Overview](img/jifx21-4/jifx21-4_systems_overview-25p.png)

## Background

In August 2021 the [Bay Area Mesh (BAM)](http://www.sfwem.net) (née San 
Francisco Wireless Emergency Mesh/SFWEM) participated in the week-long 
[Naval Postgraduate School (NPS)](https://www.nps.edu) Joint Inter-agency Field 
Experiment 21-4 (JIFX). This event, held quarterly at two facilities in 
California, provides numerous environments for experimentation, including 
freshwater & saltwater tanks, an airfield, simulated cities and villages, and 
natural California hills & terrain. Every JIFX incorporates stakeholders from 
multiple different organizations across disciplines within the federal 
government, including defense, homeland security, and others.

BAM conducted several experiments in collaboration with the Fab Lab at 
California State University Bakersfield, Splunk & Orion Labs. Every experiment 
explored the capabilities of the Smart Wireless Mesh across a variety of 
different missions:

- Disaster Response (DR/DRO)
- Situational Awareness (SA) & Common Operating Picture (COP)
- Unmanned Systems (UxS) Command & Control (C2)
- Sensor Data Collection (ISR) & IoT
- Real-time multimedia communications & collaboration

For each of these missions the Smart Wireless Mesh was tested both for 
feasibility of conducting this type of mission, and the ability for the 
network to be field expedient or rapidly deployed within an austere 
environment.

Several novel capabilities were also uncovered over the course of the 
experiment week.

### Collaborators

- Bobby Hartsock KJ6YOA, Fab Lab at California State University Bakersfield
- Vivian Richards, Splunk
- Greg Albrecht W2GMD, SFWEM & Orion Labs

## Themes & Motivation

Experiments can be best categorized under the themes of:

* Hastily Formed Networks
* Unmanned Systems
* Situational Awareness
* Smart Team Communications

### Hastily Formed Networks

BAM utilizes commercial off-the-shelf (COTS) wireless networking equipment 
typically running the 
[Amateur Radio Emergency Data Network (AREDN)](http://www.arednmesh.org) 
firmware. 

The AREDN firmware transforms COTS equipment into resilient auto-configuring 
mobile ad-hoc network (MANET) "Nodes" that provide high-speed wireless IP 
connectivity - including across multiple hops, support being hastily assembled 
(HFN) & dynamically redeployed. Regional AREDN networks have been deployed 
around the continental United States as well as abroad and represent both 
steady-state/always-on infrastructure & field-deployable systems.

### Unmanned Systems

Piloting of an Unmanned Ground System (UGS) typically requires an IP based 
connection to a Ground Control Station (GCS). Similarly, UGS sub-systems like 
the video feed from an on-board camera or ISR systems require IP connectivity 
to a display or collection device. The reliance on wireless line-of-site radio 
signals can constrain the range of a UGS. Similarly, the reliance on static or 
point-to-point IP routing between a UGS & GCS can constrain the ability of the 
IP network to recover from a routing fault.

AREDN can provide a UGS with IP networking and back-haul on-the-move, 
allowing both remote piloting and video streaming between the UGS & GCS. 
Additionally, because each UGS was also itself a AREDN node, every UGS is also 
able to extend the range of the existing network. Combined with another UGS 
this allows a multi-hop ‘swarm’ like system were multiple different UGS can 
extend or augment the existing network in real-time.

### Situational Awareness

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

### Smart Team Communications

Smart Team and group communications systems are equipped not-only to facilitate 
real-time messaging between disparate users, but act on those messages at a 
System level. 

Given a user engaging in team collaboration at various "bandwidths" both 
physiologically and as a measure of information throughput, can a Smart Team 
Communications component of a Smart Wireless Mesh act on an end-users message 
metadata and provide a communications force multiplier. Can this Smart Team 
Communications platform present operational data to other organizational units 
or command?

## Conclusions

Using commercial off-the-shelf hardware & open-source software, it is possible
to stand-up a field expedient Smart Wireless Mesh using AREDN. This Smart 
Wireless Mesh provides unmanned systems command & control, group communication 
support, real-time sensors/IoT, and SA or ISR applications. Standards-based 
network end-points can be used immediately, and others integrated rapidly 
using Node-RED. Integration with Smart Team Communications platforms like Orion 
and operational intelligence platforms like Splunk enabled expedient knowledge 
and SA propagation to all users of the Smart Wireless Mesh.

## Details

### Proof-of-Concepts Demonstrations

Several Smart Wireless MANET proof-of-concepts were fielded at JIFX, with 
several novel designs coming from collaboration with other JIFX participants & 
stakeholders. Concepts addressed mobile on-the-go connectivity, edge compute, 
body worn networks, sensor deployment, and unmammed systems:

1. Unmanned Ground System (UGS) Command, Control (C2) & Communication (C3) using Smart Wireless Mesh
2. Situational Awareness (SA), ISR & operational data collection / analysis using Smart Wireless Mesh
3. [FEM: Field Expedient Mesh](https://docs.google.com/document/d/e/2PACX-1vRyGsw-RGppwFkW2Hl2Mvyr_1tCyZlY9DcAW-5aExY2DaQULdS9K9BDHQ4m5f6-9IjNANNyMiEzPkIA/pub)
4. [MoW: Mesh on Wheels](https://ampledata.org/mesh_on_wheels.html): Portable Smart Wireless Mesh node with edge compute, data transformation & 
sensor capability.
5. [MOHO: Mesh On, Head Out](https://docs.google.com/document/d/e/2PACX-1vQ3Ifm22DDEpWOroPbiniyFwpm9VnEg6Mle1H32S-YZcqxm_PcNKZcz8nVdV4PXIDQGBh4dp-R1Hb_E/pub)
6. [HAMPR: Human Attached Mesh Portable Radio](https://docs.google.com/document/d/e/2PACX-1vQ-CQPKQoxwUs22BxCVVWEgoi6T5WjK5gj4A6dTuFdoL3xQOzWndhEsBhI49IOAK_8EMrfJ6XgIs75I/pub)
7. [CRUMB: Compact Rugged Unattended MANET Box](https://docs.google.com/document/d/e/2PACX-1vQ9hizd-hBS7pmzbBaGV4_r0oLnm_-1yrTiFp2eHsgGJ4Frk10f46fv1rpx3IOwkm6VV1A-eb-SKC8C/pub)
8. [RedTAK: Tactical ETL](https://docs.google.com/document/d/e/2PACX-1vRoeGoHn6uTSmykPAltiWmhUnpA2jpKAya5xn4vYNiq9gM6AiZNzb9Sbct45mnOUoxpDXrIFpgNTFAW/pub)
9. BLoS using COTS

### Data

Operational data was collected from UGS C2, mesh radios and ATAK clients. 
During experimentation several data collection sources (or destinations) were 
reconfigured in-the-field using using RedTAK. RedTAK was configured to forward 
data to both Splunk & InfluxDB, with SA data mirored to COPERS.

Several remote systems that were capable of full-duplex data transfer were also 
integrated into RedTAK, allowing the RedTAK system to transform any real-time 
SA data into a format compatible with another remote system - allowing each to 
render a COP in their native representation.

Systems like Orion & Twilio that were capable of sending, receiving and 
understanding human voice, typing and multimedia messaging were able to 
interact through either their own, or a native CoT channels.

[![JIFX 21-4 Data Flow Diagram](img/jifx21-4/jifx21-4_data_flow_diagram_25p.png)](img/jifx21-4/jifx21-4_data_flow_diagram.png)


#### Splunk

Splunk collected all operational & SA data originating from and passing through 
the experiments at JIFX. Early operational questions could be quickly answered 
with Splunk. All data passing through RedTAK could be transformed and indexed 
by Splunk. This data pipeline allow a wireless RF anomoly enountered early in 
experimentation with our UGS to be quickly isolated. Using a Splunk Alert with 
RedTAK allowed us to delivery an instant LoS condition alert to the GCS.

Of interest to our collaboration with Splunk was to test the ability to act as 
a data force multiplier for DSCA operations, particular within the disaster 
response and evaucation planning missions.

Using ATAK with the WASP Plugin, rescuers were able to populate a damage 
assessment dashboard within Splunk in real-time. For users operating in a 
heads-up mode, Orion was used to understand PTT conversations between rescuers. 
Finally, for users with limited message capability within LTE denied 
environments, SMS text messages with damage assessment reports & locations 
could be sent & received by Twilio.

[![JIFX 21-4 Damage Assessment statistics displayed on a map](img/jifx21-4/jifx21-4_damage_assessment_25p.png)](img/jifx21-4/jifx21-4_damage_assessment.png)

A procedure was developed on-site to transform ArduPilot Mission Planner UGS 
location positioning data into Cursor on Target, a format used by Splunk, ATAK 
and others. In this procedure, WinTAK running on the GCS computer was used as a 
NMEA to CoT gateway. Effort was made to analyze real-time UGS operational data 
in Splunk by utilizing a Mavlink decoder with limited success.

[![JIFX 21-4 UGS PLI displayed within a TAK client](img/jifx21-4/jifx21-4_ugs_tak_25p.png)](img/jifx21-4/jifx21-4_ugs_tak.png)

### Hardware & Software

Ubiquiti Rocket M5 5 GHz radios were used universally in this experiment, all 
of which had been updated to use the AREDN mesh firmware. Radios operated in 
the Part TK portion of the 5 GHz band.

More information on ATAK, WinTAK & TAK Server can be found at www.tak.gov

#### Portable UGS ground control station (GCS)

[![JIFX 21-4 UGS GCS](img/jifx21-4/jifx21-4_ugs_gcs_25p.jpg)](img/jifx21-4/jifx21-4_ugs_gcs.jpg)

The Portable GCS comprised the computer, software and hardware required to 
control the UGS. Piloting and Mission Planning utilized ArduPilot, “an open 
source, unmanned vehicle Autopilot Software Suite”. Manual UGS piloting 
utilizing a Logitech F310 Gamepad USB controller attached to the GCS computer, 
a Dell Latitude 12 Rugged Tablet (7202) running Windows 10. On-screen UGV video 
was transcoded & displayed using ffmpeg, VLC & gstreamer.

Additionally, WinTAK was used to transform UGS positioning data into a format 
compatible with other TAK systems, see note under Data > Splunk.

#### Other Software Used

* Debian
* Node-RED
* TAK Server
* ATAK
* Orion
* ArduPilot
* pycot
* Proxmox
* CentOS
* gstreamer
* ffmpeg
* Splunk
* tileserver-gl
* Docker

### Ad-Hoc Experimentation

NPS encouraged and promoted ad-hoc and collaborative experimentation between 
participants at every JIFX. Several novel concepts were fielded, many of which 
were developed on-site and in the field.

#### UGS mounted LIDAR & Underground Mesh

[![JIFX 21-4 UGS-mounted LIDAR](img/jifx21-4/jifx21-4_ugs_lidar_25p.jpg)](img/jifx21-4/jifx21-4_ugs_lidar.jpg)

Working with Exyn, CSUB reconfigured a UGS to support carrying a LIDAR scanner 
payload. Once the payload was mounted, UGS were tasked by Mission Plan to 
traverse an underground tunnel. An unexpected but recoverable failure 
encountered during this mission was the navigation and IMU fail safes built 
into the UGS Mission Planning software. This fail safe was encountered due to 
the GPS denied nature of an underground tunnel, and its curved walls causing a 
significant delta in vehicle pitch. Once bypassed the mission could succeed. 

Piloting the UGS into a tunnel also required extending the mesh network into an 
underground, network-denied environment. This was accomplished using several 
CRUMBs placed strategically around the tunnel complex, each extending the mesh 
into the tunnel and allowing continuous C2 while underground. 

#### Other Ad-Hoc Experimentation

* Collecting Mavlink data with Splunk [incomplete].
* Transforming Mavlink data with Node-RED [incomplete].

### Novel Capabilities

Several novel capabilities were developed during experimentation.

1. **Sending SA data to COPERS.** This was the first time we've intereacted with 
   this system. Using RedTAK we were able to establish a bidirectional data 
   connection with COPERS, allowing us to send SA data to, as well as receive 
   SA data from all other users of COPERS (including other experimenters).
2. **Collecting & learning AREDN sysinfo.json telemetry data.** Early 
   experimentation showed an emerging wireless RF anomoly. A RedTAK flow was 
   created to search for & collect AREDN sysinfo.json data from all MANET 
   nodes - forwarding all collected data to Splunk. A hastily constructed 
   discovery method allowed new MANET participants to be queried, or old ones 
   pruned.
3. **Sending SA data to Splunk.** The n-dimensional nature of SA data, relying 
on both time and 3D space, allow index, search and machine learning across all 
   dimensions using Splunk. Indexed geographical data can be displayed using a 
   Splunk map dashboard, and temporal data can be analyized in real-time by 
   a human or using a Splunk ML process.

An attempt was made to integrate Mavlink data into both Node-RED & Splunk with 
limited success. Further research is recommended in this area.




