This article is a review of the security features of various Land Mobile 
Radio Systems available presently. There are many communications products that 
offer features labeled as 'secure', and there are just as many folk ideas of 
what 'secure' means. An attempt has been made to develop a rubric through which 
and a user of a Land Mobile System can select the features of a System
 that make it 'secure' to them.

One of the primary uses of LMR systems is for Push-to-Talk voice communication, 
where human voice is the medium. Most LMR systems do not protect this medium in 
any way, sending messages in the clear for anyone to intercept & hear. For users 
who need to protect their messages from interception, they may choose a security 
feature that offers some privacy guarantee. Many of the same users also need to 
ensure the identity of other users on the System, so will choose a security 
feature that authenticates users of the system.

Potential threats to LMR systems include the ability to intercept any user's 
transmissions, which is easily achieved with commercial-off-the-shelf equipment. 
Often secondary market devices are available that can be configured to act as 
users of a System, giving the operator the ability to intercept and send messages.
Finally, edge devices like hand-held walkie-talkies can be easily misplaced, lost, 
or stolen, allowing an attacker to have direct access to the System.

Almost every LMR system is susceptible to interference, both deliberate and 
accidental. This can vary in range from a hobby kit for kids, to some nearby
electronic noise source.

Assumptions

- Systems are installed and configured per the manufacturers specifications.
- Systems adhere to the regulatory specifications ruling the region in which they 
operate (emission types, license, power, etc)

Assets

1. The 'message' in the human voice PTT
2. The authoritative & presented identity of the Speaker

Threats

1. Interception of PTT 'message'
2. Impersonating a User

###### Terms

* **CTCSS**: Continuous Tone-Coded Squelch System
* **PL**: Privacy Line
* **DCS**: Digital-Coded Squelch
* **LMR**: Land Mobile Radio 
* AES: A
* DES:
* NXDN:
* DMR:
* dPMR:
* Part 97:
* Part 15:
* GMRS:
* FRS:
* P25:

# Analog Radio Systems

This section under development, currently under review:
* DES ADP
* Tone-access & control systems (2TONE, etc)

# Digtial Radio Systems

## Kenwood NEXEDGE

> This section adopted from the following specififications:
> * NXDN Technical Specifications, TS 1-D Version 1.3. JVC KENWOOD Corporation and Icom Incorporated.

Kenwood NEXEDGE is a commercial implementation of the NXDN open standard for LMR.
Many Kenwood NXDN-compatible radios offer compatibility with other LMR systems, 
such as DMR, dPMR, P25, and conventional analog. For the purpose of this 
evaluation we're focusing on the NXDN portion of these devices. 

The NXDN specification describes three levels of 'encryption algorithm' security:

1. No Guard Level: No Encryption.
2. "Low Guard Level": Voice Scrambling/"Scramble Encryption"
3. "High Guard Level": (this level is further split into:)
    1. "DES Encryption" [FIPS 46-3](https://csrc.nist.gov/csrc/media/publications/fips/46/3/archive/1999-10-25/documents/fips46-3.pdf)
    2. "AES Encryption" [FIPS 197](https://csrc.nist.gov/publications/detail/fips/197/final) in OFB Mode [NIST 800-38A](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf)

"Low Guard" & "High Guard" encryption happen immediately after the Vocoder 
stage on the transmitting side, or immediately before the Vocoder stage on the 
receiving side. With encryption & decryption happening so early in the voice 
processing stage, this ensures that lower layers of the NXDN CAI lack access to 
the 'plaintext' voice.

![NXDN Encryption Layers](img/nxdn_encryption_layers.png)

###  NXDN DES Encryption

NXDN DES uses a 56-bit key length. Keys must be pre-loaded onto devices before 
use, and are identified by a pre-shared Key ID. The 64-bit Initialization Vector 
within the DES OFB is seeded with random data, with the generation method left 
up to the party implementing the protocol. Initialization Vector values are 
synchronized within the same frame as the shared Key ID.

`VCALL_IV` message content:

     2 bits      6 bits 64 bits
    +-----------+------+---------------------+
    |Cipher Type|Key ID|Initialization Vector|
    +-----------+------+---------------------+

Shared IV

Encryption frame

v_calliv
https://www.qsl.net/kb9mwr/projects/dv/nxdn/NXDN-TS-1-B_v0103.pdf


https://www.dropbox.com/s/zt0vxv6k2xprowc/Screenshot%202020-07-24%2013.45.51.png?dl=0

https://www.dropbox.com/s/v5bpc2w7kdlam06/Screenshot%202020-07-24%2013.46.14.png?dl=0
  
 NXDN Technical Specifications, TS 1-D Version 1.3. JVC KENWOOD Corporation and Icom Incorporated.
 


### NXDN Voice Scrambling




https://kenwoodcommunications.co.uk/acc/modules/KWD-AE31%20AES/DES%20Encryption%20Module/


NX-5400: 
* Built-in 56-bit DES & Optional 256-bit AES Encryption (NXDN & P25)
* "NXDN Digital Scrambler"
* Encryption Key Zeroize & Retention 
* • P25 Over-the-Air Re-keying
* • Built-in Voice Inversion Scrambler
* KWD-AE31 Secure Cryptographic Module (AES&DES)
# https://comms.kenwood.com/en/common/pdf/products/accessories.pdf#zoom=170

KPG-94
https://rfguys.com/products/keyloader-kvl-cable-kenwood-tk5710-tk5810-etc-kpg-94
Motorola KVL-3000
KWD-AE31K
https://www.ameradio.com/product/101094/description.html
AES/DES Encryption Software Key Loader for KWD-AE31K

Authentication by KPT-300LMC is required

Note: KPG-AE1 is a U.S. DOC/BIS Export Controlled Item (ECCN 5D002A)
https://github.com/KFDtool/KFDtool

https://d3cz7oi6fhv94u.cloudfront.net/adbc-27815757-FSB-0417-VK5000-02.pdf?versionId=ex9vRe4ognJlSnfz0KoZi4h4VcdCTGMa

https://www.dropbox.com/s/qpsy2hz6dv9gdqt/Screenshot%202020-07-24%2013.17.02.png?dl=0
https://comms.kenwood.com/common/pdf/download/1000_NEXEDGE_Ability_K.pdf



Notes
-----

co-channel

COMSEC
- Access 
- Brevity
- Clarity
- Speed
- Flexibility
- Simplicity


Confidentiality
Privacy
Authenticity

