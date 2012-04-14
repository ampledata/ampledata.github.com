Create an eventtype for the conditions you want to alert on, for
example from eventtypes.conf:

    :::ini
    [nbx]
    search = "status err"

Then create a Saved Search that Alerts if there are any events with this
eventtype in savedsearch.conf:

    :::ini
    [nbx]
    action.email = 1
    action.email.inline = 1
    action.email.sendresults = 1
    action.email.to = gba@splunk.com
    alert.digest_mode = False
    alert.severity = 4
    alert.suppress = 0
    alert.track = 1
    counttype = number of events
    cron_schedule = */5 * * * *
    description = gba's nbx experiment
    dispatch.earliest_time = -6m@m
    dispatch.latest_time = -1m@m
    enableSched = 1
    quantity = 0
    relation = greater than
    search = eventtype="nbx"

Going forward, anytime Splunk indexes an event with the string **status err**,
I'll receive an email alert.

---
Greg Albrecht <gba@splunk.com>

April 4th, 2012
