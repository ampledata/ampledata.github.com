Servers generate a lot of email. If you're a sysadmin, you already know this.
 If you work with sysadmins, then you're to blame (ok, maybe not).
 In either case, dealing with server email is time consuming, and the 
signal-to-noise ratio is low. More often than not these emails are ignored 
(procmail FTW!). 

**Is this a good thing?**

No.

**Why?**

These emails are generated for a reason, and that reason is usually that 
there's something amiss on your server. Instead of `/dev/null`'ing all of 
these useful nuggets, why not mine them with Splunk?

In this *How To* we'll setup a catch-all Postfix server and use it to Splunk 
all of your system generated email.

Overview
========

* Install and start Splunk.
* Install and start Postifx.
* Configure Postfix catch-all.
* Configure your servers(s) to use the Postfix catch-all.
* Configure Splunk to consume the catch-all email.

**Note:** Splunk need not be installed on the same system as Postfix, but for 
the purposes of this *How To*, they are co-existent.

Pre-Requisites
==============

1. Ensure you've downloaded and installed [Splunk](http://www.splunk.com/download).
2. Ensure you've installed Postfix (Ubuntu: `apt-get install postfix -f`).

Steps
=====

1. Edit Postfix's **main.cfg** configuration and set the following values:
* Set **virtual_alias_domains** to all hosts from which you're going to accept 
mail: `virtual_alias_domains = sfeserv01.splunk.com,sfeserv31.splunk.com`
* Set **virtual_alias_maps** to your virtual alias map file: 
`virtual_alias_maps = hash:/etc/postfix/virtual`
4. In Postfix's **virtual_alias_map** file create a catch-all alias for each 
host from which you'll be accepting mail:

		@sfeserv01.splunk.com  catch-all
		@sfeserv31.splunk.com  catch-all

5. In Postfix's **aliases** file create a catch-all alias and redirect it to a 
Maildir: `catch-all: /var/mail/catch-all/`
6. Refresh aliases, rehash maps, and reload Postfix configs:

		sudo newaliases
		sudo postmap /etc/postfix/virtual
		sudo postfix reload

7. In Splunk's **inputs.conf** file configure batch monitor of the catch-all 
Maildir:

		# $SPLUNK_HOME/etc/system/local/inputs.conf
		[batch:///var/mail/catch-all]
		interval = 300
		disabled = false
		index = admin_mail
		source = admin_mail
		move_policy = sinkhole
		sourcetype = admin_mail

8. In Splunk's **props.conf** file configure email event parsing:

		# $SPLUNK_HOME/etc/system/local/props.conf
		[admin_mail]
		TRUNCATE = 0
		MAX_EVENTS=200000
		TIME_PREFIX = Date:\s
		LINE_BREAKER = x6939844b3e9eae3093ed00e67a0dd33b
		BREAK_ONLY_BEFORE = x6939844b3e9eae3093ed00e67a0dd33b

9. In Splunk's **indexes.conf** file configure the email index:
			
		# $SPLUNK_HOME/etc/system/local/indexes.conf
		[admin_mail]
		homePath   = $SPLUNK_DB/admin_mail/db
		coldPath   = $SPLUNK_DB/admin_mail/colddb
		thawedPath = $SPLUNK_DB/admin_mail/thaweddb

10. Restart Splunk: `splunk restart`
11. Now configure your servers(s) to use the Postfix catch-all mail server. 
In Postfix this can be accomplished in **main.cfg**: `relayhost = mail-relay.splunk.com`

Search
======

You can now search Splunk for system emails: `index="admin_mail" ERROR`

Which should return results like these:

![admin_mail splunk search result](http://undef.files.wordpress.com/2011/01/mvg_asvnwzj.png?w=300)
