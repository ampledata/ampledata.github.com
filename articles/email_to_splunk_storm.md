Using my [Splunk Storm
Webhook](https://github.com/ampledata/splunkstorm-webhook) and an email
service provider like [Email Yak](http://www.emailyak.com/) we can
easily index, search and report on email messages using [Splunk
Storm](https://www.splunkstorm.com). I chose Email Yak for this
tutorial because they offer a 'Free' account level and allow Email Push
notifications via HTTP POST (aka [Webhooks](http://webhooks.org/)).

# Steps

1. Follow the instructions for setting up the [Splunk Storm
   Webhook](https://github.com/ampledata/splunkstorm-webhook).
2. Sign up with [Email Yak](http://www.emailyak.com/) and register a new domain:

  ![Email Yak New Domain Control Panel](http://dl.dropbox.com/u/4036736/Screenshots/g-9w.png)</br>
3. Send a test email: `echo 'this is a test email'| mail -s 'test email' gba@emailtostorm.simpleyak.com`</br>
4. Search for and report on your email with Splunk Storm:

  ![Email in Splunk Storm](http://dl.dropbox.com/u/4036736/Screenshots/48d-.png)

# Bonus
Here's another useful search that extracts the message body and displays it
as a table:

    *simpleyak* | spath output=TextBody TextBody | table TextBody

---
Greg Albrecht <gba@splunk.com>

April 16th, 2012
