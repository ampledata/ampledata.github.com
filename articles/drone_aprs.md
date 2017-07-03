# Drone APRS - UAVPRS

This article is still under development. For more information please contact:

- Greg Albrecht W2GMD
- Email: <a href="mailto:oro-net@undef.net">oro-net@undef.net</a>
- Phone: 310-621-9598


## Concept: Drone-based APRS Platform.

UAVPRS is an Unmanned Arial Vehicle (UAV/Drone)-based APRS platform for both
beaconing and gating APRS traffic from the RF APRS network.

This concept has thus-far been tested once using a DJI Mavic Pro 2 drone and
simple 2W APRS beacon.

### Example telemetry

In this example, a tactical APRS beacon was tethered to a drone and flown a few
dozen feet into the air to test beaconing capability.

```
2017-07-02 16:23:25 CDT: OROTAC-4>S7TTVV,WIDE1-1,WIDE2-1,qAR,GLNVW-1:`26Dl <0x1c>>/"4s}W2GMD Oro-Net.org Tactical 4.05V  23.3C X
2017-07-02 16:23:45 CDT: OROTAC-4>S7TTVV,N6WKZ-3*,WIDE2-1,qAR,GLNVW-1:`26Dl <0x1c>>/"4s}W2GMD Oro-Net.org Tactical 4.05V  23.2C X
2017-07-02 16:25:38 CDT: OROTAC-4>S7TTVU,WIDE1-1,WIDE2-1,qAR,KC6SSM-5:`26El"q>/"4x}W2GMD Oro-Net.org Tactical 4.05V  23.1C X
2017-07-02 16:26:18 CDT: OROTAC-4>S7TTVU,WIDE1-1,WIDE2-1,qAR,KC6SSM-5:`26Hl W>/"5k}W2GMD Oro-Net.org Tactical 4.06V  23.1C X
2017-07-02 16:27:22 CDT: OROTAC-4>S7TTVU,WIDE1-1,WIDE2-1,qAR,KC6SSM-5:`26Hl*)>/"5`}W2GMD Oro-Net.org Tactical 4.05V  23.0C X
2017-07-02 16:27:38 CDT: OROTAC-4>S7TTVV,WIDE1-1,WIDE2-1,qAR,GLNVW-1:`26Il!'>/"5g}W2GMD Oro-Net.org Tactical 4.05V  23.0C X
2017-07-02 16:27:54 CDT: OROTAC-4>S7TTVV,WIDE1-1,WIDE2-1,qAR,GLNVW-1:`26Il!'>/"5i}W2GMD Oro-Net.org Tactical 4.06V  23.0C X
2017-07-02 16:28:26 CDT: OROTAC-4>S7TTVV,WIDE1-1,WIDE2-1,qAR,GLNVW-1:`26Il!'>/"5j}W2GMD Oro-Net.org Tactical 4.05V  23.0C X
2017-07-02 16:29:01 CDT: OROTAC-4>S7TTVV,N6WKZ-3*,WIDE2-1,qAR,NZ6J-13:`26Il $>/"5h}W2GMD Oro-Net.org Tactical 4.06V  23.1C X
```

```

2017-07-02 16:23:25 CDT: OROTAC-4>S7TTVV,WIDE1-1,WIDE2-1,qAR,GLNVW-1:`26Dl <0x1c>>/"4s}W2GMD Oro-Net.org Tactical 4.05V  23.3C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVV
   latitude: 37.74433333333333 °
   longitude: -122.44 °
   course: 0 °
   speed: 0 km/h
   altitude: 92 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.05V  23.3C X


2017-07-02 16:23:45 CDT: OROTAC-4>S7TTVV,N6WKZ-3*,WIDE2-1,qAR,GLNVW-1:`26Dl <0x1c>>/"4s}W2GMD Oro-Net.org Tactical 4.05V  23.2C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVV
   latitude: 37.74433333333333 °
   longitude: -122.44 °
   course: 0 °
   speed: 0 km/h
   altitude: 92 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.05V  23.2C X


2017-07-02 16:25:38 CDT: OROTAC-4>S7TTVU,WIDE1-1,WIDE2-1,qAR,KC6SSM-5:`26El"q>/"4x}W2GMD Oro-Net.org Tactical 4.05V  23.1C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVU
   latitude: 37.74416666666666 °
   longitude: -122.4401666666667 °
   course: 285 °
   speed: 0 km/h
   altitude: 97 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.05V  23.1C X


2017-07-02 16:26:18 CDT: OROTAC-4>S7TTVU,WIDE1-1,WIDE2-1,qAR,KC6SSM-5:`26Hl W>/"5k}W2GMD Oro-Net.org Tactical 4.06V  23.1C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVU
   latitude: 37.74416666666666 °
   longitude: -122.4406666666667 °
   course: 59 °
   speed: 0 km/h
   altitude: 175 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.06V  23.1C X


2017-07-02 16:27:22 CDT: OROTAC-4>S7TTVU,WIDE1-1,WIDE2-1,qAR,KC6SSM-5:`26Hl*)>/"5`}W2GMD Oro-Net.org Tactical 4.05V  23.0C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVU
   latitude: 37.74416666666666 °
   longitude: -122.4406666666667 °
   course: 13 °
   speed: 1.852 km/h
   altitude: 164 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.05V  23.0C X


2017-07-02 16:27:38 CDT: OROTAC-4>S7TTVV,WIDE1-1,WIDE2-1,qAR,GLNVW-1:`26Il!'>/"5g}W2GMD Oro-Net.org Tactical 4.05V  23.0C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVV
   latitude: 37.74433333333333 °
   longitude: -122.4408333333333 °
   course: 111 °
   speed: 0 km/h
   altitude: 171 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.05V  23.0C X


2017-07-02 16:27:54 CDT: OROTAC-4>S7TTVV,WIDE1-1,WIDE2-1,qAR,GLNVW-1:`26Il!'>/"5i}W2GMD Oro-Net.org Tactical 4.06V  23.0C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVV
   latitude: 37.74433333333333 °
   longitude: -122.4408333333333 °
   course: 111 °
   speed: 0 km/h
   altitude: 173 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.06V  23.0C X


2017-07-02 16:28:26 CDT: OROTAC-4>S7TTVV,WIDE1-1,WIDE2-1,qAR,GLNVW-1:`26Il!'>/"5j}W2GMD Oro-Net.org Tactical 4.05V  23.0C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVV
   latitude: 37.74433333333333 °
   longitude: -122.4408333333333 °
   course: 111 °
   speed: 0 km/h
   altitude: 174 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.05V  23.0C X


2017-07-02 16:29:01 CDT: OROTAC-4>S7TTVV,N6WKZ-3*,WIDE2-1,qAR,NZ6J-13:`26Il $>/"5h}W2GMD Oro-Net.org Tactical 4.06V  23.1C X
   type: location
   format: mice
   srccallsign: OROTAC-4
   dstcallsign: S7TTVV
   latitude: 37.74433333333333 °
   longitude: -122.4408333333333 °
   course: 8 °
   speed: 0 km/h
   altitude: 172 m
   symboltable: /
   symbolcode: >
   mbits: 101
   posresolution: 18.52 m
   posambiguity: 0
   comment: W2GMD Oro-Net.org Tactical 4.06V  23.1C X
```

![aprs.fi Screen Capture](http://ampledata.org/img/uavprs1.png)
![aprs.fi Screen Capture](http://ampledata.org/img/uavprs2.png)

## Next Steps

Arial Digipeater/Gateway.
