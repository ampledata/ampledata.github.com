As a it's installation scales out, different components of a Splunk install can be distributed to disparate systems across a network. For example, the Search Head and Indexer components of a Splunk Installation can be configured on two different servers. In this setup the Indexer component is known as a 'Search Peer' of the Search Head. Out of the box Splunk supports two different methods of synchronizing the configuration between a Search Head and its Search Peers: Bundle Replication and Mounted Bundles. Each of these methods has its advantages, but for Splunk Storm we needed a method that scaled in a slightly different way, so we developed a method that uses lsyncd for synchronizing configuration.

lsyncd is a Lua-based daemon that monitors inotify Linux kernel inode actions. Based on its configuration and the action it's been configured to watch, lsyncd, using rsync, can synchronize the deltas of file system changes. Utilizing this we can replace the existing behavior of bundle replication between Search Peers.

Pre-Requisites
----
* Linux Operating System (sorry windows)
* A Splunk Search Head.
* One or more Splunk Search Peers (indexers, etc).

Steps
----
1. Setup & Configure Splunk
2. Build & Install lsyncd.
3. Configure lsyncd.

