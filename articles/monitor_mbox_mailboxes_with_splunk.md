### Overview
I hate reading email. So much. I do however enjoy searching email. Using
Splunk I can monitor and index my email. This is incredibly useful for
administrators of Unix boxes where cron jobs very often generate an
unprecidented amount of email messages.


### Steps

1. Download & Install [Splunk](http://www.splunk.com/download).
2. Configure Splunk to monitor your mailboxes:

        :::ini
        # $SPLUNK_HOME/etc/system/local/inputs.conf
        [batch:///var/mail]
        disabled = false
        move_policy = sinkhole
        sourcetype = mbox

3. Configure Splunk to properly extract messages from your mailbox:

        :::ini
        # $SPLUNK_HOME/etc/system/local/props.conf
        [mbox]
        LINE_BREAKER = ([\r\n]+)From\s
        SHOULD_LINEMERGE = false

You're now ready to search and view your email messages in Splunk:

![email message in Splunk](http://dl.dropbox.com/u/4036736/Screenshots/g8tg.png "Email messsage as a Splunk event.")
