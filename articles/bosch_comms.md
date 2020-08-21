# Communications Techniques in Bosch Season 5

This post analyzes some of the communications techniques employed by characters 
in season 5 of the series "Bosch" on [Amazon Video](https://www.amazon.com/Bosch-Season-5/dp/B07NSFS72Z). By way of background, "Bosch" 
is a crime series based on novels by [Michael Connelly](https://en.wikipedia.org/wiki/Michael_Connelly) depicting LAPD Detective 
Hieronymus "Harry" Bosch.

In this season, Bosch is investigating a murder suspect, who is also a shill for 
an opioid pill mill. Bosch goes undercover as opioid user 'Dominic Reilly', 
while his partner Jerry "J." Edgar and another detective, Rene Davila, surveil 
him.

Bosch and J. Edgar have pre-arranged "Hold Fast" as their [Duress Code](https://en.wikipedia.org/wiki/Duress_code). This 
Duress Code is an example of a Covert Distress Signal, a pre-arranged method of 
conveying danger that is known only to privy parties. The code is a shared 
semantic token known only by Bosch and his partner J. Edgar. If Bosch were to 
encounter danger while he is undercover as Dominic Reilly, without giving up his 
cover he could use the phrase 'hold fast' somewhere in conversation.

## Season 5, Episode 6: "The Space Between the Stars"

The first use of the Duress Code is when one of the pill mill shills admits to 
Dominic Reilly that he (having spotted Detective Davila's car) believe they're 
under surveillance. Dominic offers to help get rid of the cops, and using the 
shill's cellphone, calls 911 to report an officer down at "Hold Fast Pizza". J. 
Edgar & Davila hear an all-call go out on the radio system for an officer down 
at "Hold Fast Pizza" and know right away that their cover is blown, so they bug 
out.

In this instance, the Duress Code "Hold Fast" was passed through the 911 PSAP & 
LAPD radio system, turning them into a Covert Channel for transmitting an 
encoded message. Because Jerry had visual on Bosch, and knew he was not in 
danger, hearing the Duress Code over the LAPD radio system indicated to him that 
there was some other compromise (their surveillance cover was blown).

### Techniques
1. [Duress Code](https://en.wikipedia.org/wiki/Duress_code).
2. [Covert Channel](https://en.wikipedia.org/wiki/Covert_channel): 
As defined, these are channels for covert communications that may unknowingly 
send covert messages. Here, Bosch used the emergency response system to transmit 
an encoded message to J. Edgar.

## Season 5, Episode 7: "The Wisdom of the Desert"

Dominic befriends Lindsey, another opioid user, and while she's distracted he 
slips a note into her pocket (Brush Pass or Dead Drop). Later, while out on a 
pill harvesting run at a pharmacy, Dominic puts an item from the store into 
Lindsey's purse, and alerts a security guard that she has been shoplifting. The 
security guard apprehends Lindsey, and while the police are called, the 
remainder of the pill mill participants leave. After searching Lindsey, the 
police discover the note left by Dominic (Covert Channel), which contains J. 
Edgar's number, along with the Duress Code. The police call J. Edgar, who 
questions Lindsey in an attempt to locate Bosch.

### Techniques

1. [Brush Pass](https://worldview.stratfor.com/article/above-tearline-brush-passes-and-dead-drops): 
As the Twitter user [@SpyBlog](https://twitter.com/spyblog/status/1221327327902228480) 
points out, this method is used to covertly pass messages between individuals, 
which is similar in this case, although Lindsey wasn't privy to the pass.
2. [Dead Drop](https://en.wikipedia.org/wiki/Dead_drop): 
Typically this is a pre-arranged message nexus where there is no actual human 
interaction, and coded signals are used to indicate that there is a message to 
be sent. Here Lindsey was the Drop, while the note was the transmit Signal and 
the Message. It could also be argued that the shoplifting arrest encapsulated 
the transmit signal.
3. [Covert Channel](https://en.wikipedia.org/wiki/Covert_channel): 
While not an established channel, here Lindsey was the channel for transmitting 
the Duress Code.
