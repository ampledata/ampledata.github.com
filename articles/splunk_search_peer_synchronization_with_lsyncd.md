# DRAFT
gba@20120928 This article is a **DRAFT**.

Abstract
----
This article discusses a method of synchronizing Splunk Search Peers using  lsyncd.

Overview
----
As a it's installation scales out, different components of a [Splunk](http://www.splunk.com/) can be distributed to separate systems across a network. For example, the Search Head and Indexer components of a Splunk Installation can be configured on two different servers. In this setup the Indexer component is known as a 'Search Peer' of the Search Head.

Out of the box Splunk supports two different methods of synchronizing the configuration between a Search Head and its Search Peers: Bundle Replication and [Mounted Bundles](http://docs.splunk.com/Documentation/Splunk/latest/Deploy/Mounttheknowledgebundle). Each of these methods has its advantages, but for Splunk Storm we needed a method that scaled in a slightly different way, so we developed a method that uses [lsyncd](http://code.google.com/p/lsyncd/) for synchronizing configuration.

lsyncd is a Lua-based daemon that monitors [inotify](http://en.wikipedia.org/wiki/Inotify) Linux kernel filesystem changes. Based on the changes it's been configured to watch, lsyncd, via [rsync](http://en.wikipedia.org/wiki/Rsync), can synchronize the deltas (changes) of files. We've utilized this to replace the existing behavior of bundle replication between Search Peers.


Pre-Requisites
----
* Linux Operating System.
* A Splunk Search Head.
* One or more Splunk Search Peers (indexers, etc).


Steps Overview
----
1. Setup & Configure Splunk.
2. Install lsyncd.
3. Configure lsyncd.
4. Configure Splunk.


Detailed Steps
----
Assuming you've already configured [Distributed Search](http://docs.splunk.com/Documentation/Splunk/latest/Deploy/Configuredistributedsearch):

1. Disable Bundle Replication on the Search Head, where SEARCH_PEER is the IP or Hostname of the Search Peer from your distributed search setup:

        # $SPLUNK_HOME/etc/system/local/distsearch.conf
        [distributedSearch]
        shareBundles = false
        servers = SEARCH_PEER:8089

2. Configure lsyncd to monitor the $SPLUNK_HOME/etc/ directory for changes, where SEARCH_PEER is the IP or Hostname of the Search peer from your distributed search setup:

        # /etc/lsyncd.conf.lua
        sync{
          rsyncssh,
          source='/opt/splunk/etc',
          host='spsync@SEARCH_PEER',
          targetdir='/opt/searchpeer'
        }

3. Enable Mounted Bundles on the Search Peer, where SEARCH_HEAD is the IP or Hostname of the Search Head from your distributed search steup:

        # $SPLUNK_HOME/etc/system/local/distsearch.conf
        [searchhead:SEARCH_HEAD]
        mounted_bundles=true
        bundles_location=/opt/searchpeer

References
----
* [Distributed Splunk Overview](http://docs.splunk.com/Documentation/Splunk/latest/Deploy/Distributedoverview)
* [Components of a Splunk Deployment](http://docs.splunk.com/Documentation/Splunk/latest/Installation/ComponentsofaSplunkdeployment)
