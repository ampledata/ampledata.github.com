Preface
=======
While I believe some of the statements I've made leading up to this experiment 
were gender bias (sexist), this article is my mea culpa, in the form of data 
and graphs.

Introduction
============
A few days ago, The Cure's ["A Forest"](http://www.youtube.com/watch?v=7ZwVgQ4Wq7E) 
(from ['Seventeen Seconds'](http://en.wikipedia.org/wiki/Seventeen_Seconds)) 
came on the radio. It had an unfamiliar intro, so I asked 
[@curikim](twitter.com/curikim) *"Do you know who this is?"*, to which she 
quickly responded *"The Cure"*. *"Of course"* I said, *"you're a girl, girls 
always know Cure tracks."* 

*"In fact, I'm going to conduct an experiment: "*
> Who's the lead singer of The Cure?

I proceeded to posted this question on Facebook & Twitter and collect the results. 

Results
=======
Respondents gender was determined by public profile data. Data was collected
manually and graphed with [Splunk Storm](https://www.splunkstorm.com/)

All Responses
-------------
First lets look at who actually responded. These weren't necessarily correct 
answers (more like people trolling me).

![Percentage of Respondents by Sex](http://dl.dropbox.com/u/4036736/Screenshots/06fh.png)

Out of 13 responses, 8 identified as male, and 5 identified as female.

This graph shows that, despite the lack of a correct answer, respondents were
more likely to identify as male.

Correct Responses
-----------------
Now lets look at correct responses.

![Correct Responses by Sex](https://dl.dropbox.com/u/4036736/Screenshots/inwn.png)

Out of 5 correct responses, 3 identified as male, and 2 identified as female.

This graph shows that correct answers were more likely to come people who 
identify as male. This follows the trend of more responses overall coming people
who identify as male.

Selection Bias
==============
This section calls for further research, but I'll guess that I have a higher
percentage of followers who identify as male, leading to the higher percentage
of overall results coming from that gender.

Conclusion
==========
Gender identity does not determine Cure affinity.

Furthermore, blanket statements and generalizations rarely do anyone any good.

Data
====
Here's the anonymized and normalized response data:

	2012-06-02 11:27:42.585077 sex=male answer=''
	2012-06-02 11:27:42.586611 sex=female answer=''
	2012-06-02 11:27:42.586630 sex=male answer=''
	2012-06-02 11:27:42.586645 sex=male answer=''
	2012-06-02 11:27:42.586660 sex=male answer=''
	2012-06-02 11:27:42.586674 sex=male answer='robert smith'
	2012-06-02 11:27:42.586689 sex=female answer='robert smith'
	2012-06-02 11:27:42.586704 sex=female answer=''
	2012-06-02 11:27:42.586719 sex=female answer=''
	2012-06-02 11:27:42.586733 sex=male answer='robert smith'
	2012-06-02 11:27:42.586748 sex=male answer=''
	2012-06-02 11:27:42.586762 sex=male answer='robert smith'
	2012-06-02 11:27:42.586777 sex=female answer='robert smith'

