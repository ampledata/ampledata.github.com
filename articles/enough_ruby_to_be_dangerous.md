Introduction
============

I am a recovering System Administrator. It's a title I was chained to for the 
first 10 or so years of my career. I've only recently decided to tackle 
Software Engineering full-time, and it's kept me clear of on-call duties for 
the past 4 years!

This was until the company I work at, Splunk, decided to start a new 'cloud'
based service, Splunk Storm. This project was going to be run 'DevOps' style,
which was a perfect hybridization of my skills as a Sys Admin and Software 
Engineer! In addition, we were going to be using Chef for infrastructure 
automation!

So, at this point, I was becoming pretty versed at Python. I had no interest 
in taking on the task of learning Ruby, or a DSL there-of. I wanted to 
continue getting really good at Python. I mean, I need SOME Pythonic fodder 
on my resume.

But, I knew the pains of repetitive System Administration tasks. So Chef, 
and Ruby, it was.

I figured I was going to have to learn _Enough Ruby to be Dangerous_.


Ruby
====

What is Ruby, right?
--------------------

Ruby is a Python DSL for Hipsters.

j/k.

> An interpreted scripting language for quick and easy object-oriented 
> programming. -Matz

That's Yukihiro 'Matz' Matsumoto, the creator of Ruby. He created Ruby in
the 90's because he wanted something more powerful than Perl and more OOP
Python.

Remember the mantra
-------------------

It's *quick and easy* (and big in Japan).

Why Ruby for Chef?
------------------

Well, it comes down to ease-of-use. 

1. Ruby has minimal syntax, so it takes very little code to get most common 
activities done.
2. The code should look as close to a configuration as possible.
        package 'foo'
3. When Adam and Co were writing Chef many of their initial customers were 
Rails shops, so adoption of another Ruby app was a no-brainer.

What's so different about Ruby?
-------------------------------

Well, when Matz describes it as an object-orient language, he literally 
means that everything is an object. For example, the line of code below
converts the integer 1 into a floating point integer:

    :::ruby
    1.to_f
     => 1.0

Everything is an object. It really is that simple:

    :::ruby
    'taco'.reverse
     => "ocat"

Everything.

    :::ruby
    'taco'.reverse.reverse
     => "taco"

Everything!
That's a little different, right?

I mean, how would we do this in Python?

    :::python
    >>> float(1)
    1.0
    >>> 'taco'[::-1]
    'ocat'

Yeah, it's about the same amount of coding, but unless you've reversed a
string 100 times in Python, are you really going to remember what `[::-1]`
does?


Style
=====

Once I grasped that everything in Ruby was an object, I started exploring 
my OOP prowess by browsing the Ruby Standard Library and writing obscure 
shit that even I didn't understand (and my co-workers loathed):

    :::ruby
    # I have no idea what this does:
    build = (url_body/'a').collect do |l|
      l.inner_html if l.inner_html.start_with? "#{name}-" 
    end.select{|i|!i.nil?}.sort{|x,y|y<=>x}.first

That was until I had to go back and fix it.

What did I learn?
-----------------

Well, it's important to write code that other people can read, and a really 
good guideline for writing readable code is the Style Guide.

Even if you never go another Ruby talk, even if you never read a Ruby book: 
Use the Style Guide!


Walk the Walk
=============

Aside from helping you write better code as a new developer, the Style Guide 
has the added benefit of training you the lexicon of the language. Speaking 
in the context and the convention of a language is a prerequisite for 
knowledge.

> Teaching conventions in isolation is ineffective at best, because students 
> need opportunities to apply their knowledge of conventions to their writing. 
>
> Even daily oral language activities are a waste of time for students 
> without procedural knowledge of how and when to use conventions in writing.
>
> Consequently, the most effective way to teach conventions is to integrate 
> instruction directly into the writing process.

I mean we've all had to describe bugs to other people. In fact, we've had to
have people describe their bugs to us. Think of the difference between "The 
website is down." and "I'm getting 'no route to host'." Big difference. Huge.


Smoke some irb
==============

Ok, we know what good Ruby looks like, and we've got an idea of how we can 
express ideas in Ruby. Where do we start? I recommend smoking some **irb**, 
Ruby's Interactive Shell. For example, the examples above look something
like this in irb:

    :::ruby
    $ irb
    ruby-1.8.7-p352 :001 > puts 'this is irb'
    this is irb
     => nil 
    ruby-1.8.7-p352 :002 > me = 'gba'
     => "gba" 
    ruby-1.8.7-p352 :003 > puts "hi #{me}, welcome to irb."
    hi gba, welcome to irb.
     => nil 
    ruby-1.8.7-p352 :004 > quit()

You're going to experiment a lot. In fact, I highly recommend you experiment 
before even beginning to write actual deployable code. Your options are 
writing an entire program and finding a syntax error on a production system, 
or incrementing through each code block in your terminal.


Primitive Primer
================

We've gotten a quick view of what Ruby looks like through my awesome OOP
examples above, but before we get any deeper, lets have a look at some of the
language primitives. These are the fundamental - atomic - types of 
knowledge representation in any language:

    :::ruby
    # String
    'taco'
    
    # Integer
    1
    
    # Float
    1.0
    
    # Array
    ['taco', 'burrito']
    
    # Hash
    {'lunch' => 'taco', 'price' => 1}

Shit just got real. 

So where does the OOP come in? Well, lets look at what we can do with these
primitive types:

    :::ruby
    'taco'.methods
     => ["upcase!", "zip", "find_index", "between?", "unpack", "each_slice", ...]

This lists just about everything you can do to a primitive of type String.
You've already seen an example of this with `reverse`:

    :::ruby
    'taco'.reverse
     => 'socat'

In addition to the methods listed for each of the primitives, Ruby also
includes many built-in methods.

    :::ruby
    >> methods
    => ["irb_print_working_binding", "inspect", "workspaces", "tap", "clone", ...]

    :::ruby
    >> Kernel.methods
    => ["inspect", "name", "private_class_method", "exit!", "chomp!", "tap", ...]


Library Hell
============

Any language gains its power through it's extensibility, including it's
ability to support importing external libraries. Ruby is not immune. Using
the `require` builtin method we can easily import libraries
included in both the standard Ruby distribution, and those created by external
authors. 

Here we're importing the `open-uri` library, which extends the
built-in `open` method to support.. opening URIs!:

    :::ruby
    require 'open-uri'
    gba = open('http://ampledata.org')

Files & Exceptions
==================

On to the fun stuff. Lets actually do something. Lets start by opening a
file. Since we've all got access to a Unix system, lets check out what our
BOFH has left in our MOTD:

    open('/etc/motd', 'r')
     => Errno::ENOENT: No such file or directory - /etc/motd
      from (irb):1:in `initialize'
      from (irb):1:in `open'
      from (irb):1

What the crap happened here? 

We raised an exception, or a program interrupt. Apparently it's what big
kids to in programming languages... no return codes here!

What can we glean from this Exception? Well, for starters we can see what
this exception is called: **Errno::ENOENT**. Additionally we've got a
friendly error message in **No such file or directory**, and finally the
code path leading back to our error.

Ok, we're all System Administrators, we know that files and filesystems are 
never eternal. If this were a chunk of code we were deploying to a 
server, how would we keep this from causing our pager to go off at 
3AM? We'll catch it!

    :::ruby
    begin
      open('/etc/motd', 'r')
    rescue Errno::ENOENT
      "dude the file isn't there"
    end
     => "dude the file isn't there"

We're telling Ruby that we want to rescue the specific error 
**Errno::ENOENT** and if it happens, return a friendlier error message.

Awesome. Our pager is quiet, back to drinking.

But wait, we still don't have a MOTD. TOFIX!


RI & RDoc
=========

Since we're using `open` to try and read our MOTD, maybe we can also use it
to write our MOTD. We've got some tools that can help us with that too. From
the command line we can invoke the `ri` utility to look at the embedded
documentation for `open`:

    :::ruby
    --------------------------------------------------------------- IO::open
         IO.open(fd, mode_string="r" )               => io
         IO.open(fd, mode_string="r" ) {|io| block } => obj
    ------------------------------------------------------------------------
         With no associated block, +open+ is a synonym for +IO::new+. If the
         optional code block is given, it will be passed _io_ as an
         argument, and the IO object will automatically be closed when the
         block terminates. In this instance, +IO::open+ returns the value of
         the block.


Here's the ri for **IO.new**:

    :::ruby
    ---------------------------------------------------------------- IO::new
         IO.new(fd, mode)   => io
    ------------------------------------------------------------------------
         Returns a new +IO+ object (a stream) for the given integer file
         descriptor and mode string. See also +IO#fileno+ and +IO::for_fd+.
    
            a = IO.new(2,"w")      # '2' is standard error
            $stderr.puts "Hello"
            a.puts "World"
    
         _produces:_
    
            Hello
            World

Sweet. We now know how to open files, and write to files.


Back to the real MOTD
=====================

Where are we going to get the content for our MOTD? Luckily I know an
inspirational source:


    :::ruby
    require 'open-uri'
    fd = open('https://api.twitter.com/1/statuses/user_timeline.json?count=1&screen_name=georgetakei')
    fd.read
     => "[{\"created_at\":\"Sat May 05 15:27:11 +0000 2012\",\"id\":198795988947...

I have an idea for a Chef LWRP!


Of Resources & Men
==================

Real quick lets break down the components of a Chef LWRP:

1. **Resource**: Where we define the actions and parameters of an LWRP.
2. **Provider**: The actual implementation & code for an interface.

You can think of a Resource as a method definition, and the Provider as the
method itself:

    :::ruby
    def resource(a, b, c)
      provider
    end

First, lets create a new Cookbook: `knife cookbook create motd`

Now lets create our Resource: `vi motd/resources/default.rb`

    :::ruby
    actions :create
    
    def initialize(*args)
      super
      @action = :create
    end

Finally, we'll create our Provider: `vi motd/providers/default.rb`

    :::ruby
    require 'open-uri'
    require 'json'
    
    action :create do
      twitter = 'https://api.twitter.com/1/statuses/user_timeline.json?count=1&screen_name='
      tweet = ''
    
      # Connect to twitter, ask them for the goods, parse the JSON:
      open(twitter + new_resource.name, 'r'){ |tfd| tweet = JSON(tfd.read) }
    
      # Write only the text of the tweet to our file:
      open('/etc/motd', 'w'){ |mfd| mfd.write(tweet.first['text']) }
    
      # Let the other Resources know we did some work today:
      new_resource.updated_by_last_action(true)
    end

As an added bonus, we'll include a base recipe: `vi motd/recipe/default.rb`

    :::ruby
    motd 'georgetakei'

Cool, lets see if it works with **shef**:

    :::ruby
    chef > recipe
    chef:recipe > include_recipe 'motd'
    chef:recipe > run_chef
    [Sun, 06 May 2012 11:57:43 -0700] DEBUG: Processing motd[georgetakei] on karman.home
    [Sun, 06 May 2012 11:57:43 -0700] INFO: Processing motd[georgetakei] action create (motd::default line 1)
     => true
    chef:recipe > open('/etc/motd').read
     => "Ke$ha dubs herself \"Pop's dirty little sister.\" Didn't realize she was from\nthe Ozarks."


Testing
=======

Having any amount of code in a Provider can lead down a dangerous path of
having a code path that lacks coverage, or testing. Lets abstract our
MOTD Provider out to a Library that we can then test: `vi motd/libraries/default.rb`

    :::ruby
    require 'open-uri'
    require 'rubygems'
    require 'json'
    
    TWITTER = 'https://api.twitter.com/1/statuses/user_timeline.json?count=1&screen_name='
    
    # Connects to twitter, retrieves tweets for screen_name.
    def get_tweet(screen_name)
      open(TWITTER + screen_name, 'r'){ |tfd| JSON(tfd.read) }
    end
    
    # Writes tweet out to /etc/motd.
    def write_motd(tweet)
      open('/etc/motd', 'w'){ |mfd| mfd.write(tweet) }
    end

Now lets create some tests for our Library: `vi motd/libraries/default.rb`

    :::ruby
    require 'test/unit'
    
    class TestMOTDLibrary < Test::Unit::TestCase
      def test_get_tweet
        tweets = get_tweets('ampledata')
        tweet = tweets.first['text']
    
        assert_kind_of(String, tweet)
        assert_match(/Ruby Testing/, tweet)
      end
    
      def test_write_motd
        tweets = get_tweets('georgetakei')
        tweet = tweets.first['text']
    
        write_motd(tweet)
        motd = open('/etc/motd').read
    
        assert_equal(tweet, motd)
      end
    end

And lets run our tests `ruby libraries/default.rb`:

    :::ruby
    Loaded suite libraries/default
    Started
    F.
    Finished in 0.428887 seconds.
    
      1) Failure:
    test_get_tweet(TestMOTDLibrary) [libraries/default.rb:26]:
    <Ke$ha dubs herself \"Pop's dirty little sister.\" Didn't realize she was from\nthe Ozarks.> expected to be =~
    </Ruby Testing/>.
    
    2 tests, 3 assertions, 1 failures, 0 errors

Oh, right :)


References
==========

* [A community-driven Ruby coding style guide](https://github.com/bbatsov/ruby-style-guide)
* [Unit Testing in Ruby](http://en.wikibooks.org/wiki/Ruby_Programming/Unit_testing)

* [Just Enough Ruby for Chef](http://wiki.opscode.com/display/chef/Just+Enough+Ruby+for+Chef)
* [_why's (poignant) Guide to Ruby](http://mislav.uniqpath.com/poignant-guide/)
* [Programming Ruby](http://www.rubycentral.com/pickaxe/)
