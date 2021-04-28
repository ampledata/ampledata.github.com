# Adding a Network GPS to WinTAK & ATAK for GPS Denied Environments

![Screenshot of ATAK using External GPS](img/network_gps/screenshot_31016_x50.png)

This article describes a method for integrating an External / Network GPS 
into ATAK and WinTAK using a Raspberry Pi running Node-RED & GPSD, with an
outboard GPS antenna and sufficient GPS satellite coverage. This integration 
provides GPS location information GPS Denied environments such as in-building, 
on-the-move, or underground / subterranean.

## Background

ATAK & WinTAK End User Devices (EUDs) can use on-board GPS capabilities of most 
smartphone and PCs. In GPS-denied environments this capability can be replaced by 
a network-capable GPS to provide ongoing location awareness. The integration described 
in this article uses Node-RED to convert NMEA output from GPSD to a Cursor-on-Target (CoT) 
Events compatible with ATAK & WinTAK. (Of note: As of writing (Apr-27-2021), WinTAK 
supports raw NMEA input over network, while ATAK does not).

![Node-RED Flow](img/network_gps/node-red-flow.png)

## Requirements

While this integration method can be run on any host system, this article describes 
using a Raspberry Pi running Raspbian OS, with an attached USB GPS and outdoor antenna.

While GPSD is used on the Raspberry Pi to connect to the USB GPSD, it's also possible to 
connect to the USB GPS device directly from Node-RED, but that is outside the scope of 
this article.

1. [Raspberry Pi running Raspberry Pi OS](https://www.raspberrypi.org/)
2. [USB GPS](https://smile.amazon.com/dp/B07P8YMVNT)
3. [GPSD](https://gpsd.gitlab.io/gpsd/)
4. [Node-RED](http://nodered.org/)
5. [node-red-contrib-nmea](https://github.com/nootropicdesign/node-red-contrib-nmea): A Node-RED node to decode NMEA format messages.
6. [WinTAK or ATAK](https://takmaps.com/)

# Node-RED Steps

Below are a directly downloadable version of this integration, as well as a walk-through 
of the Node-RED Flow itself.

## Node-RED Flow Download

You can download an example of this integration at: [https://gist.github.com/ampledata/a44a4d0279489f15b6fb5a3c0afb25c9](https://gist.github.com/ampledata/a44a4d0279489f15b6fb5a3c0afb25c9)
## Node-RED Flow Walk-through

The Node-Red Flow for this integration can be described as 4 total steps.

### Step 1 - Connect-to & Configure GPSD
![Node-RED Flow, Part 1](img/network_gps/node-red-flow-part1.png)

This step connects to the GPSD Network port 2947 on localhost (127.0.0.1), and configures
the port to send NMEA:

`?WATCH={"enable":true,"json":true,"nmea":true,"raw":0,"scaled":false,"timing":false,"split24":false,"pps":false}`

### Step 2 - Parse output from GPSD
![Node-RED Flow, Part 2](img/network_gps/node-red-flow-part2.png)

We'll need to convert the Javascript Buffer to a Javascript String, and we'll also split 
the network payload by newline into individual messages. This allow us to filter NMEA 
sentence type later.

Buffer.toString() Function Node code content:

    :::js
    let oldPayload = msg.payload;
    msg.payload = oldPayload.toString();
    return msg;


### Step 3 - Filter NMEA Sentence type, send NMEA directly to WinTAK
![Node-RED Flow, Part 3](img/network_gps/node-red-flow-part3.png)

We're only interested in NMEA GPGGA Sentences, and WinTAK can read those over the network 
on port 4349. 

![Node-RED UDP Node WinTAK Configuration](img/network_gps/node-red_udp-node_wintak.png)

If you're only using WinTAK, you're done! Otherwise, move to the next step.

### Step 4 - Extract NMEA, Serialize as CoT
![Node-RED Flow, Part 4](img/network_gps/node-red-flow-part4.png)

Using the NMEA Parsing Node we'll serialize the NMEA as JSON. Then we'll create a new 
CoT Precision Location Event in JSON, and covert it to XML. Finally, we'll send it over 
the network to ATAK on port 4349. 

![Node-RED UDP Node ATAK Configuration](img/network_gps/node-red_udp-node_atak.png)

CoT Precision Location Serialization Javascript code follows:

    :::js
    /*
    Create a CoT XML serializable JSON payload from NMEA JSON input.
    
    Author:: Greg Albrecht W2GMD <oss@undef.net>
    Source:: https://ampledata.org/network_gps.html
    */
    
    // Geenrate a timestamp for the CoT Event
    const dt = Date.now();
    const dtD = new Date(dt).toISOString();
    // "stale" Period (mostly ignored for this type of Event)
    const dtD5 = new Date(dt + 250000).toISOString();
    
    // Copy old event for reference
    let oldPayload = msg.payload;
    
    msg.payload = {
        event: {
            $: {
                version: "2.0",
                uid: "External-GPS",
                type: "a-f-G-E-S",
                time: dtD,
                start: dtD,
                stale: dtD5,
                how: "m-g"
            },
            point: [ { 
                $: {
                    lat: oldPayload.lat,
                    lon: oldPayload.lon,
                    hae: parseFloat(oldPayload.alt) + parseFloat(oldPayload.geoidalSep),
                    ce: oldPayload.horDilution,
                    le: 0
                }
            } ],
            detail: [ {
                precisionlocation: [ {
                    $: {
                        geopointsrc: "GPS",
                        altitudesrc: "GPS"
                    }
                } ],
                remarks: ["External GPS"],
                extendedGpsDetails: [ {
                    $: {
                        fixQuality: 1,
                        numSatellites: oldPayload.numSat,
                        time: oldPayload.timestamp
                    }
                } ]
            } ]
        }
    }
    
    return msg;

# ATAK Steps

1. From ATAK, select **Settings**: ![ATAK Settings](img/network_gps/atak_settings_x50.png)
2. Select **Show All Preferences**: ![ATAK Settings Screen](img/network_gps/screenshot_6310_x50.png)
3. Select **Device Preferences**:  ![ATAK All Preferences Screen](img/network_gps/screenshot_10369_x50.png)
4. Select **GPS Preferences**: ![ATAK Devices Preferences](img/network_gps/screenshot_30359_x50.png)
5. Select **GPS Option**: ![ATAK GPS Preferences](img/network_gps/screenshot_17580_x50.png)
6. For GPS Option, select **External or Network GPS / Fallback Internal GPS**: ![ATAK GPS Option](img/network_gps/screenshot_20731_x50.png)
7. Exit Settings (possibly restart ATAK).

# WinTAK Steps

WinTAK steps and menu are identical to ATAK Steps.
