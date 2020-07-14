TL;DR: You can implement FIPS 140-2 compliant VoIP with RFC 3711 media
 and RFC 4568 signaling using [baresip](http://www.creytiv.com/baresip.html).

This article describes implementing (and testing!) secure VoIP using the [baresip](http://www.creytiv.com/baresip.html) library. 
Verification steps avoid intercepting or decrypting transport media, and instead 
rely on the protocol negotiation parameters of TLS and SIP to ensure compliance.

The intention is to configure a baresip User Agent to comply with the following 
standards for signaling & media:

Signaling
- [FIPS 140-2 Annex A](https://csrc.nist.gov/publications/detail/fips/140/2/final), 
[FIPS 197](https://csrc.nist.gov/publications/detail/fips/197/final) Advanced 
Encryption Standard (AES) with a 256 bit key (AES256).
- [SP 800-38D](https://csrc.nist.gov/publications/detail/sp/800-38d/final) Galois Counter Mode (GCM).
- [FIPS 140-2 Annex A](https://csrc.nist.gov/publications/detail/fips/140/2/final), [FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final) Secure Hash Algorithm (SHA) with a Message Digest Size of 384 bits (SHA384).
- [FIPS 186-4 Appendix D](https://csrc.nist.gov/publications/detail/fips/186/4/final) Elliptic Curve P-384.
- [NIST SP 800-56A](https://csrc.nist.gov/publications/detail/sp/800-56a/rev-3/final) Elliptic-curve Diffie–Hellman Key Agreement Protocol (ECDHE)
- [FIPS 186-4](https://csrc.nist.gov/publications/detail/fips/186/4/final) Elliptic-curve Digital Signature Algorithm (ECDSA)

Our Signaling Cipher Suite is: `ECDHE-ECDSA-AES256-GCM-SHA384`  

Media
- [RFC 3711](https://tools.ietf.org/html/rfc3711) The Secure Real-time Transport Protocol (SRTP)
- [RFC 4568](https://tools.ietf.org/html/rfc4568) Session Description Protocol (SDP) Security Descriptions for Media Streams (SDES)
- [RFC 4568](https://tools.ietf.org/html/rfc4568) SDES-SRTP Crypto-Suites

Our Media "Crypto-Suite" is: `AES_CM_128_HMAC_SHA1_80`

Many of these standards are also applicable to the [National Information 
Assurance Program (NIAP) Protection Profile (PP) for Voice over IP (VoIP)](https://www.niap-ccevs.org/Profile/Info.cfm?PPID=399&id=399).

# Overview

Voice over IP (VoIP) is a broad term that can refer to any method of transmitting 
voice communications over an IP network. When implemented out-of-the-box, the 
most common VoIP protocol, SIP, lacks any security provisions for this these 
voice communcations. Fortunately the flexibility of SIP allows for enhancements 
that provide a level of security, and when configured correctly, allows the 
protocol to meet certain standards of security as selected by the US Government, 
et al.

We'll work through the following steps to build an environment that applies 
these enhancements to a Baresip UA, and verify the environment meets certain 
security standards:

1. Generate a compliant client & server security certificate.
2. Compile & Run the baresip UA with the security parameters set.
3. Simulate a remote SIP endpoint using OpenSSL's `s_client` & `s_server`.
4. Verify the exchange between OpenSSL & Baresip.

# Terms

- Elliptic Curve Private Key (ECPK)
- P-384 Elliptic Curve (P-384)
- X.509 Public Key Certificate (Cert)
- SIP User Agent (UA)
- Session Description Key Exchange (SDES)
- Secure RTP (SRTP)
- Session Initiation Protocol (SIP)
- Test Workstation (TW)

# Steps

SIP, by default, passes traffic unencrypted over UDP on port 5060. When used 
RTP transport, the media is also passed in unencrypted UDP (typically on a 
random port). We're going to encrypt our media using SDES-SRTP, and wrap our 
SIP signaling in TLS over TCP on port 5061. This ensures that bout our voice 
traffic, as well as the keys used to encrypt that voice traffic, is secure.

To enable SIP over TLS with baresip, we'll need to configure the baresip UA 
with an X.509 Public Key Certificate. Once configured, baresip will be capable 
of sending and receiving calls over SIP TLS on port 5061.

All of these steps can take place on a single TW running both baresip & the 
OpenSSL Simulated SIP End-points.

These steps are broken down as follows:

* [Generate a Private Key & Certificate](#certificate-generation)
* [Build & Run Baresip](#build--run-baresip-ua)
* [Create Simulated SIP End-points](#create-simulated-sip-endpoints)
* [Test & Verify Configuration]()

# Certificate Generation

An end-user would be expected to generate (or provide) their own Cert for use by 
their UA, but for this example we'll generate our own self-signed Cert. 

We're also going to generate our own ECPK using P-384.

## Generate an ECPK using P-384

This section describes the process of generating an ECPK using P-384 on the TW. 
Additional prerequisite steps are provided to ensure the TW is capable of 
generating ECPKs using P-384.

All of the commands in this section must be executed on the same TW.

### Prerequisites

The following steps verify the OpenSSL library on the TW is (1) installed and (2)
capable of generating an ECPK using P-384:

1. Ensure OpenSSL's command-line tool 'openssl' is installed:  
   _The command:_  
   `$ openssl version && echo ''openssl' installed!'`  
   _Should return:_  
   `openssl installed!`
2. Ensure OpenSSL includes support for the P-384:  
  _The command:_  
  `$ openssl ecparam -list_curves|grep 384`  
  _Should return at least:_  
  `secp384r1 : NIST/SECG curve over a 384 bit prime field`

### Steps

1. Generate an ECPK using P-384.  
  _The command:_  
  `$ openssl ecparam -genkey -name secp384r1 -param_enc explicit -out example.key -param_enc named_curve`  
  _Should create the file ‘*example.key*’, as verified with:_  
  `$ ls example.key`  
  _Should return:_  
  `example.key`

### Verification
1. Display the curve used to create the ECPK.  
  _The command:_  
  `$ openssl ecparam -in example.key -text -noout`  
  _Should return:_  
  `ASN1 OID: secp384r1`  
  `NIST CURVE: P-384`

## Create a Self-Signed Cert using an ECPK with P-384
### Steps
1. Create the Cert using the OpenSSL command-line tool 'openssl':  
  _The command:_  
  `$ openssl req -x509 -new -sha384 -days 30 -nodes -key example.key -out example.cert -subj "/C=US/ST=California/L=San Francisco/O=Example Co./OU=IT/CN=example.com"`  
  _Should create the file ‘example.cert', as verified with:_  
  `$ ls example.cert`  
  _Should return:_  
  `example.cert`

## Create a combined PEM file

Baresip requires the Cert be provided in PEM format, with the Cert & ECPK 
concatenated together into a single file:  
  _The command:_  
  `$ cat example.key example.cert > example.pem`  
  _Should create the file ‘example.pem’, as verified with:_  
  `$ ls example.pem`  
  _Should return:_  
  `example.pem`

# Build & Run Baresip UA

Baresip requires the libre and librem libraries as well as a complete build 
environment. For simplicy, we're going to use a Docker container to build and 
run the UA.

1. Create a Dockerfile with the following content:  
    ```dockerfile
    FROM python:3-buster
    
    WORKDIR /baresip-docker
    
    RUN git clone https://github.com/creytiv/re.git && \
      cd re && \
      make RELEASE=yes install
    
    RUN git clone https://github.com/creytiv/rem.git && \
      cd rem && \
      make install
    
    RUN git clone https://github.com/baresip/baresip.git && \
      cd baresip && \
      make USE_TLS=yes USE_SRTP=yes install
    
    RUN ldconfig
    
    CMD ["baresip", "-f", "/dev_volume"]
    ```  
2. Build the container: `$ docker build -t baresip-docker .`
3. Run the container: `$ docker run -itv $(pwd):/dev_volume baresip-docker:latest baresip -f /dev_volume`
4. With the Baresip UA running, you should see the following output:
    ```shell script
    baresip v1.0.0 Copyright (C) 2010 - 2020 Alfred E. Heggestad et al.
    Local network address:  IPv4=eth0|192.168.1.1
    SIP Certificate: /dev_volume/example.pem
    Populated 0 accounts
    account: No SIP accounts found
     -- check your config or add an account using 'uanew' command
    Populated 0 contacts
    aucodec: PCMU/8000/1
    aucodec: PCMA/8000/1
    mediaenc: srtp
    mediaenc: srtp-mand
    mediaenc: srtp-mandf
    Populated 2 audio codecs
    Populated 0 audio filters
    Populated 0 video codecs
    Populated 0 video filters
    baresip is ready.
    ```
   Notice that the UA has enabled SRTP: `mediaenc: srtp`

# Create Simulated SIP Endpoints

## Call Receiver

Using the same Cert & ECPK we generated for the Baresip UA, we're going to use 
OpenSSL's `s_server` to simulate a SIP Endpoint. This will allow the Baresip UA 
to create a TLS connection and send an initial SDP with SDES.

`$ openssl s_server -accept 5071 -cert example.cert -key example.key -cipher ECDHE-ECDSA-AES256-GCM-SHA384 -named_curve secp384r1 -no_dhe`

This command should provide the following output:
```
Using default temp ECDH parameters
ACCEPT
```

## Call Sender

Using the same Cert & ECPK we generated for the Baresip UA, we're going to use 
OpenSSL's `s_client` to simulate a SIP Endpoint. This will allow the Baresip UA 
to receive a TLS connection.

TK

# Test & Verify Configuration

## Sending (originating) a Call from the Baresip UA
1. On the Baresip UA, dial our Simulated SIP Endpoint: `/dial sip:b@192.168.1.2:5071;transport=tls;mediaenc=srtp-mand`  
  (Where `192.168.1.1` is the IP of the TW)
2. On the Simulated SIP Receive Endpoint you should see the following output:  
    ```
    -----BEGIN SSL SESSION PARAMETERS-----
    MFUCAQECAgMDBALALAQABDCRfmQvTRw1xZZ0MJKtS2Vf7FG9J0/TVZnF+YNzGx/H
    xRuNTXrsClwHITWaTDQEB0yhBgIEXw0JLqIEAgIcIKQGBAQBAAAA
    -----END SSL SESSION PARAMETERS-----
    Shared ciphers:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES128-SHA:AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256:AES256-SHA:AES128-SHA
    CIPHER is ECDHE-ECDSA-AES256-GCM-SHA384
    Secure Renegotiation IS supported
    INVITE sip:xb192.168.1.2:5071;transport=tls;mediaenc=srtp-mand SIP/2.0
    Via: SIP/2.0/TLS 192.168.1.1:5061;branch=z9hG4bKc141b65f66cd0e02;rport
    Contact: <sip:user-0x55dc09027150@192.168.1.1:5061;transport=tls>
    Max-Forwards: 70
    To: <sip:b@192.168.1.2:5071;transport=tls;mediaenc=srtp-mand>
    From: <sip:a@example.com>;tag=0a94555cd2c228dd
    Call-ID: f9595791e9191927
    CSeq: 59280 INVITE
    User-Agent: baresip v1.0.0 (x86_64/linux)
    Allow: INVITE,ACK,BYE,CANCEL,OPTIONS,NOTIFY,SUBSCRIBE,INFO,MESSAGE,REFER
    Supported:
    Content-Type: application/sdp
    Content-Length: 429
    
    v=0
    o=- 1975181172 1106161735 IN IP4 192.168.1.1
    s=-
    c=IN IP4 192.168.1.1
    t=0 0
    a=tool:baresip 1.0.0
    m=audio 16796 RTP/SAVP 0 8 101
    a=rtpmap:0 PCMU/8000
    a=rtpmap:8 PCMA/8000
    a=rtpmap:101 telephone-event/8000
    a=fmtp:101 0-15
    a=sendrecv
    a=label:1
    a=rtcp-rsize
    a=ssrc:2736692082 cname:sip:b@example.com
    a=crypto:1 AES_CM_128_HMAC_SHA1_80 inline:vXMep/SIW4iMD21StWgrmy024dJZfOAM7qFFJfsJ
    a=minptime:20
    a=ptime:20
    ```

This output provides the following verifications:

Signaling
- [FIPS 140-2 Annex A](https://csrc.nist.gov/publications/detail/fips/140/2/final), 
[FIPS 197](https://csrc.nist.gov/publications/detail/fips/197/final) Advanced 
Encryption Standard (AES) with a 256 bit key (AES256): `CIPHER is ECDHE-ECDSA-AES256-GCM-SHA384`
- [SP 800-38D](https://csrc.nist.gov/publications/detail/sp/800-38d/final) Galois Counter Mode (GCM): `CIPHER is ECDHE-ECDSA-AES256-GCM-SHA384`
- [FIPS 140-2 Annex A](https://csrc.nist.gov/publications/detail/fips/140/2/final), [FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final) Secure Hash Algorithm (SHA) with a Message Digest Size of 384 bits (SHA384): `CIPHER is ECDHE-ECDSA-AES256-GCM-SHA384`
- [FIPS 186-4 Appendix D](https://csrc.nist.gov/publications/detail/fips/186/4/final) Elliptic Curve P-384: `Server Temp Key: ECDH, P-384, 384 bits`
- [NIST SP 800-56A](https://csrc.nist.gov/publications/detail/sp/800-56a/rev-3/final) Elliptic-curve Diffie–Hellman Key Agreement Protocol (ECDHE): `CIPHER is ECDHE-ECDSA-AES256-GCM-SHA384`
- [FIPS 186-4](https://csrc.nist.gov/publications/detail/fips/186/4/final) Elliptic-curve Digital Signature Algorithm (ECDSA): `CIPHER is ECDHE-ECDSA-AES256-GCM-SHA384`

Media
- [RFC 3711](https://tools.ietf.org/html/rfc3711) The Secure Real-time Transport Protocol (SRTP): `m=audio 33334 RTP/SAVP 0 8 101`
- [RFC 4568](https://tools.ietf.org/html/rfc4568) Session Description Protocol (SDP) Security Descriptions for Media Streams (SDES): `a=crypto:1 AES_CM_128_HMAC_SHA1_80 inline:gm+5A2moV/ylsWsC8GP1pg7BAbNrGQ8sKDr5HlFi`
- [RFC 4568](https://tools.ietf.org/html/rfc4568) SDES-SRTP Crypto-Suites: `a=crypto:1 AES_CM_128_HMAC_SHA1_80 inline:EFkFgnEbQwJrLhDKyMgzuJl2SLYDI1uW45CKyr6X`, specifically: `AES_CM_128_HMAC_SHA1_80`

## Receiving a Call in Baresip UA
1. On the Simulated SIP Sending Endpoint, enter the following command:  
  `$ openssl s_client -connect localhost:5061 -cert example.cert -key example.key -cipher ECDHE-ECDSA-AES256-GCM-SHA384 -groups P-384`
2. This will provide the following output:  
    ```shell script
    CONNECTED(00000005)
    depth=0 C = US, ST = California, L = San Francisco, O = Example Co., OU = IT, CN = example.com
    verify error:num=18:self signed certificate
    verify return:1
    depth=0 C = US, ST = California, L = San Francisco, O = Example Co., OU = IT, CN = example.com
    verify return:1
    ---
    Certificate chain
     0 s:/C=US/ST=California/L=San Francisco/O=Example Co./OU=IT/CN=example.com
       i:/C=US/ST=California/L=San Francisco/O=Example Co./OU=IT/CN=example.com
    ---
    Server certificate
    -----BEGIN CERTIFICATE-----
    MIICEjCCAZkCCQDyk1urbYgWmTAKBggqhkjOPQQDAzBzMQswCQYDVQQGEwJVUzET
    MBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzEUMBIG
    A1UECgwLRXhhbXBsZSBDby4xCzAJBgNVBAsMAklUMRQwEgYDVQQDDAtleGFtcGxl
    LmNvbTAeFw0yMDA3MTAyMzE1MDlaFw0yMDA4MDkyMzE1MDlaMHMxCzAJBgNVBAYT
    AlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2Nv
    MRQwEgYDVQQKDAtFeGFtcGxlIENvLjELMAkGA1UECwwCSVQxFDASBgNVBAMMC2V4
    YW1wbGUuY29tMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEk7CKiDcMIzgGvuCk15dL
    ehSuyRNfx/1qafjmAd0abH7NEMEgPITFd9oSK01kf2pfYRhIBWK1sWYd06dp9Ts5
    i5l4Mk1UOgaz+TzKEjM3yTg43LzzzZoQq23O2CzvWEe7MAoGCCqGSM49BAMDA2cA
    MGQCMAcL3m+Snelzz8uOrLRt1eZHbMRZc3C4hL05M7FC7DL+jxCokyfWnPU5KhyL
    RWov7wIweWQPr9Uvtovsov+39eGU42Fitqqfv70o2SoXvRQ/9XgDBKcHiKsQImPH
    Opagnxks
    -----END CERTIFICATE-----
    subject=/C=US/ST=California/L=San Francisco/O=Example Co./OU=IT/CN=example.com
    issuer=/C=US/ST=California/L=San Francisco/O=Example Co./OU=IT/CN=example.com
    ---
    No client certificate CA names sent
    Server Temp Key: ECDH, P-384, 384 bits
    ---
    SSL handshake has read 1068 bytes and written 262 bytes
    ---
    New, TLSv1/SSLv3, Cipher is ECDHE-ECDSA-AES256-GCM-SHA384
    Server public key is 384 bit
    Secure Renegotiation IS supported
    Compression: NONE
    Expansion: NONE
    No ALPN negotiated
    SSL-Session:
        Protocol  : TLSv1.2
        Cipher    : ECDHE-ECDSA-AES256-GCM-SHA384
        Session-ID: 0966C0600004F9A7DF9F67EF90FAAF412191E5239F38929CE80F495FEDD78352
        Session-ID-ctx:
        Master-Key: AF01D67E554CF8B8BED9732CE8DEFD02C97FFBA9F7B1DF36E7E37163F3E1633250BD9E96FEBB35217BF3FC0ACB1668F8
        TLS session ticket lifetime hint: 7200 (seconds)
        TLS session ticket:
        0000 - 39 65 eb dd 81 b8 07 1f-2b 0e a3 52 c1 c2 3e f1   9e......+..R..>.
        0010 - ba 41 2a 58 6e b0 16 28-56 e5 a4 81 c3 7c a3 ee   .A*Xn..(V....|..
        0020 - 8d ba 7f 4e ff 65 53 ef-be 80 c8 98 ca 12 0a 8c   ...N.eS.........
        0030 - c9 e1 f8 c7 cc d7 f5 6c-8d bc f1 3e 53 09 43 2f   .......l...>S.C/
        0040 - b9 7c 3f 0a 9e 39 30 cf-f2 eb 72 fd f3 51 08 25   .|?..90...r..Q.%
        0050 - f1 4a 58 49 f0 11 c1 75-03 ef 79 93 9f 20 85 ba   .JXI...u..y.. ..
        0060 - d2 80 73 2d 9e 6a 03 7e-a6 38 2c 75 f4 d1 c5 67   ..s-.j.~.8,u...g
        0070 - 44 09 ae f0 7d ad 0e b5-6c b2 3c b0 ca 28 4d 1c   D...}...l.<..(M.
        0080 - e0 04 c9 5e 6b dd 8d e1-a6 81 19 03 c4 b9 77 4b   ...^k.........wK
        0090 - 2f 61 5f 72 2d d7 f9 c0-65 18 30 72 85 10 99 55   /a_r-...e.0r...U
    
        Start Time: 1594689170
        Timeout   : 7200 (sec)
        Verify return code: 18 (self signed certificate)
    ---
    ```

This output provides the following verification:

- [FIPS 140-2 Annex A](https://csrc.nist.gov/publications/detail/fips/140/2/final), 
[FIPS 197](https://csrc.nist.gov/publications/detail/fips/197/final) Advanced 
Encryption Standard (AES) with a 256 bit key (AES256): `Cipher    : ECDHE-ECDSA-AES256-GCM-SHA384`
- [SP 800-38D](https://csrc.nist.gov/publications/detail/sp/800-38d/final) Galois Counter Mode (GCM): `Cipher    : ECDHE-ECDSA-AES256-GCM-SHA384`
- [FIPS 140-2 Annex A](https://csrc.nist.gov/publications/detail/fips/140/2/final), [FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final) Secure Hash Algorithm (SHA) with a Message Digest Size of 384 bits (SHA384): `Cipher    : ECDHE-ECDSA-AES256-GCM-SHA384`
- [FIPS 186-4 Appendix D](https://csrc.nist.gov/publications/detail/fips/186/4/final) Elliptic Curve P-384: `Server Temp Key: ECDH, P-384, 384 bits`
- [NIST SP 800-56A](https://csrc.nist.gov/publications/detail/sp/800-56a/rev-3/final) Elliptic-curve Diffie–Hellman Key Agreement Protocol (ECDHE): `Cipher    : ECDHE-ECDSA-AES256-GCM-SHA384`
- [FIPS 186-4](https://csrc.nist.gov/publications/detail/fips/186/4/final) Elliptic-curve Digital Signature Algorithm (ECDSA): `Cipher    : ECDHE-ECDSA-AES256-GCM-SHA384`
