Here's a dead simple splunkd health check. It uses an auth token
returned by splunkd's
[login endpoint](http://docs.splunk.com/Documentation/Splunk/latest/RESTAPI/RESTaccess#authentication.2Fhttpauth-tokens)
to double check daemon health. (excuse my awk ignorance)

    :::bash
    SPL_USER="admin";
    SPL_PASS="xxx";
    STATUS="err";
    TOKEN=$(curl --max-time 60 -f -o /dev/null -s -k -u $SPL_USER:$SPL_PASS -d username=$SPL_USER -d password=$SPL_PASS https://localhost:8089/services/auth/login|egrep '<sessionKey>[[:alnum:]]+</sessionKey>'|awk -F'>' '{print $2}'|awk -F'<' '{print $1}');
    curl --max-time 60 -f -o /dev/null -s -k -u $SPL_USER:$SPL_PASS https://localhost:8089/services/authentication/httpauth-tokens/$TOKEN;
    [[ $? == 0 ]] && STATUS="ok";
    logger -p local1.debug -t splunkd_auth_status $STATUS

I've intentionally left the semicolon at the end of each line for one
reason: This entire script can be concatinated into a single line and
executed via crontab:

    :::bash
    */5 * * * * SPL_USER="admin";SPL_PASS="xxx";STATUS="err";TOKEN=$(...

This command will print a line similar to this when there's an error:

    Apr  4 05:55:01 domU-12-31-39-00-E5-32 splunkd_auth_status: err

Using a Splunk Saved Search with Alerting, you could easily match this event
and trigger and alert.


Alternatively, if you're using Cloudkick you could change the logger
call at the end of this command to a simple echo:

    :::bash
    echo "status $STATUS"

-------------
Greg Albrecht <gba@splunk.com></br>

April 3rd, 2012


<div id="disqus_thread"></div>
<script type="text/javascript">
    var disqus_shortname = 'ampledata';

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
<a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>
