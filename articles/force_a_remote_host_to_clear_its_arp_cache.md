# Abstract

*[ARP](http://en.wikipedia.org/wiki/Address_resolution_protocol)* (address resolution protocol) cache can normally be cleared on networks devices using commands like: "**arp -d**" on Unix, or "**clear arp cache**" on Cisco IOS & CatOS. However, on devices for which you do not have administrative access, it may not possible to clear the ARP cache using these methods. In those cases I've presented a method of forcing a remote network device to clear its ARP cache entry for a specific host's IP address.

# Overview

If you've ever changed the IP of a host - or setup a new host with the IP of an old host - you've probably noticed that the host has no network connectivity for a period of time. While frustrating, this is by-no-means an unsolvable mystery. What's happening is that a gateway network device - such as a firewall, router or switch - has cached the old *[MAC](http://en.wikipedia.org/wiki/MAC_Address)* address (*[ethernet](http://en.wikipedia.org/wiki/Ethernet)* hardware address) associated with the host's IP address. This cache will persist on the gateway network device until one of two things happen:

1. The ARP cache on the gateway network device expires.
2. You manually clear the ARP cache on the gateway network device.

# Steps
Here's an outline of the steps you can take to resolve this issue:

1. Install **[arping](http://www.habets.pp.se/synscan/programs.php?prog=arping)** ([portable version](http://www.habets.pp.se/synscan/programs.php?prog=arping) or [FreeBSD Ports](http://www.freebsd.org/cgi/cvsweb.cgi/ports/net/arping/)).
2. Use **arping** to *[arping](http://en.wikipedia.org/wiki/Arping)* the IP address of the remote network device.

# Example Usage

In this example the default gateway for our network is **10.10.1.1** - this is the device who's ARP cache we're going to clear. The IP address of the new host is **10.10.1.2**. The MAC address of the old host was **00:1a**, and the MAC address of the new host is **00:1b** (neither MAC is important, they're just here for reference).

First, let's examine our routing table:

	$ netstat -rn
	Routing tables
	Internet:
	Destination  Gateway               Flags     Refs      Use  Netif Expire
	default      10.10.1.1             UGS       0         0    fxp0
	10.10.1.0    ff:ff:ff:ff:ff:ff     UHLWb     0         3    fxp0 =>
	10.10.1/24   link#1                UC        0         0    fxp0
	10.10.1.1    00:13:60:b8:f3:7f     UHLW      0         3    fxp0   1164
	10.10.1.2    00:02:55:54:00:1b     UHLW      0         3    lo0

Here's our first failed attempt at reaching the Internet from the new host:

	$ ping -c 1 yahoo.com
	PING yahoo.com (216.109.112.135): 56 data bytes
	--- yahoo.com ping statistics ---
	1 packets transmitted, 0 packets received, 100% packet loss


Now we'll *arping* our default gateway. This will cause the gateway to flush the ARP cache for the new host's IP address. The flags we'll use for this operation are: "**-c 1**" to send one arping, and "**-S 10.10.1.2**" to set my source IP to 10.10.1.2 (this is optional but could be useful for a host with multiple [aliased](http://www.freebsd.org/cgi/man.cgi?query=ifconfig) IPs, such as eth0:1, eth0:2, etc.).

	$ arping -c 1 -S 10.10.1.2 10.10.1.1
	ARPING 10.10.1.1
	60 bytes from 00:13:60:b8:f3:7f (10.10.1.1): index=0 time=13.884 msec
	--- 10.10.1.1 statistics ---
	1 packets transmitted, 1 packets received,   0% unanswered

Now we can successfully reach the Internet from the new host:

	$ ping -c 1 yahoo.com
	PING yahoo.com (216.109.112.135): 56 data bytes
	64 bytes from 216.109.112.135: icmp_seq=0 ttl=55 time=83.822 ms
	--- yahoo.com ping statistics ---
	1 packets transmitted, 1 packets received, 0% packet loss
	round-trip min/avg/max/stddev = 83.822/83.822/83.822/0.000 ms
