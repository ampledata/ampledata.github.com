Abstract
----
This article describes a method for manually detecting the maximum transmission unit (MTU) of interconnected systems on an IP network. It is derived from the process the author used to detect the MTU of off-site customer DSL connection.

Overview
----
The MTU of Ethernet v2 is [1500](http://en.wikipedia.org/wiki/Maximum_transmission_unit). This is a typical setting for office LANs where traffic does not traverse links of different capacities - that is, an entire office will usually all be on ethernet of some size. However, traffic that must cross non-ethernet links, such as DSL, will encounter capacities, and thus MTUs, of different sizes. 

When a network device receives a packet larger than its MTU two things can happen:

1. If the packet has the ['do not fragment'](http://en.wikipedia.org/wiki/IP_fragmentation) flag set the device will drop the packet and reply back to the packet originator with an error message.
2. If the packet does not have the 'do not fragment' flag set the device will break the packet down into identical-but-smaller sterilized packets that fit within the MTU requirements of that link.

Steps Overview
----
What follows is a example of process for detecting the MTU between your current computer and a remote computer.

In this example I've used:

* My Mac at home to test the MTU to yahoo.com.
* The 'ping' command with the '-D' (do not fragment) and '-s' (packet size) flags.

Steps
----
Normally when I ping yahoo.com I see:

    $ ping -c 1 yahoo.com
    PING yahoo.com (66.94.234.13): 56 data bytes
    64 bytes from 66.94.234.13: icmp_seq=0 ttl=47 time=256.573 ms
    --- yahoo.com ping statistics ---
    1 packets transmitted, 1 packets received, 0% packet loss
    round-trip min/avg/max/stddev = 256.573/256.573/256.573/0.000 ms

Now I'll ping yahoo.com with a packet size of 1492 bytes:

    $ ping -c 1 -D -s 1500 yahoo.com
    PING yahoo.com (66.94.234.13): 1500 data bytes
    ping: sendto: Message too long
    --- yahoo.com ping statistics ---
    1 packets transmitted, 0 packets received, 100% packet loss

Next I'll ping yahoo.com with a smaller packet size:

    $ ping -c 1 -D -s 1300 yahoo.com
    PING yahoo.com (66.94.234.13): 1300 data bytes
    1308 bytes from 66.94.234.13: icmp_seq=0 ttl=47 time=172.396 ms
    --- yahoo.com ping statistics ---
    1 packets transmitted, 1 packets received, 0% packet loss
    round-trip min/avg/max/stddev = 172.396/172.396/172.396/0.000 ms

From our testing so far we can safely assume that our MTU is less than 1500 bytes and more than 1300 bytes. We can continue testing until we find a happy medium. 

Lets try 1329 bytes:

    $ ping -c 1 -D -s 1329 yahoo.com
    PING yahoo.com (66.94.234.13): 1329 data bytes
    ping: sendto: Message too long
    --- yahoo.com ping statistics ---
    1 packets transmitted, 0 packets received, 100% packet loss

Lets try 1328 bytes:

    $ ping -c 1 -D -s 1328 yahoo.com
    PING yahoo.com (66.94.234.13): 1328 data bytes
    1336 bytes from 66.94.234.13: icmp_seq=0 ttl=48 time=288.600 ms
    --- yahoo.com ping statistics --
    1 packets transmitted, 1 packets received, 0% packet loss
    round-trip min/avg/max/stddev = 288.600/288.600/288.600/0.000 ms

Got it!

Our MTU is going to be a number less than 1336 bytes that is a multiple of 8:

* NO: 1336 / 8 = 167
* NO: 1334 / 8 = 166.75
* YES: 1332 / 8 = 166.5

The MTU between us and yahoo.com is 1332 bytes.

Here's some more information on fragmentation:

["Internetworking with TCP/IP" Pg 81 - 6.7.6 Fragmentation Control](http://tinyurl.com/6xunt8)