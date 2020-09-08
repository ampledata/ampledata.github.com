# PodSwapping

I came across a tweet from Louis Anslow featuring a TikTok video from @_leilanaa:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Kids are swapping AirPods in class then using text to speech to ‘talk’ without talking 🤩🤩🤩 <a href="https://t.co/moLxK1rzbv">pic.twitter.com/moLxK1rzbv</a></p>&mdash; Louis Anslow (@LouisAnslow) <a href="https://twitter.com/LouisAnslow/status/1219643485902508036?ref_src=twsrc%5Etfw">January 21, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

In this video, two people with iPhones and wireless AirPods swap one of the two 
left/right AirPods with each other, and use a text-to-speech app to “speak” to 
the other person. I’m going to break-down how this works and why it might be 
utilized.

First, the normal state:

![Normal State](img/podswapping/normal_state.png)

Sam & Pat both have iPhones and a set of left & right AirPods. In this diagram 
each of their iPhones are connect to each of their own AirPods over Bluetooth.

The Swap:

![The Swap](img/podswapping/the_swap.png)

Sam & Pat have swapped their left AirPods. In this diagram each of their 
iPhones are still connected to each of their own AirPods over Bluetooth, but 
the left AirPod is being worn by the other person, so Sam would hear Pat’s left 
audio channel, and Pat would hear Sam’s left audio channel. The right AirPod 
remains as it was in the normal diagram.

The video goes on to show the use of an application like Google Translate 
performing a Text to Speech operation on each phone.

This works as follows:

1. Sam types a message to Pat in the Google Translate app.
2. Sam hits the ‘Speak’ button in the app.
3. The App synthesizes the text into voice, and plays the resulting audio over 
the phone’s audio output, in this case, Bluetooth.
4. Sam hears the spoken message in the right AirPod she is wearing (which she 
can ignore)
5. Pat, the intended recipient, hears the spoken message in the left AirPods 
she is wearing.
6. Pat can reply in kind.

The advantages of this method are:

1. It works in a Denied Connectivity environment. This could be a school or 
facility that blocks or jams cellular and WiFi connections, or an area with no 
connectivity to begin with (out in the woods, power outage, etc). One could 
argue that Google Translate requires internet connectivity, but there are many 
other apps for Text-to-Speech that do not.
2. Deniability & Concealment: There is no “communication” log as there might 
normally be with a text messaging app. While a Text-to-Speech history may 
exist, there is no way to know about the recipient.

A possible shortcoming of this method is the visual reveal of the phone itself. 
If you’re trying to have a discrete exchange with someone in and environment 
where outside communication is denied, you’ve signaled your intention to 
communicate by taking out your phone. If you’re in a library where noise is 
denied, you’ve got the right solution. If you’re in a classroom or conference 
room, you might stand out.
This is a very clever technique and I applaud whoever came up with it. It could 
easily be replicated to non-Apple devices.
