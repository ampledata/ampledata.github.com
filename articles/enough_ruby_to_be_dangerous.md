Introduction
============

I am a recovering System Administrator. It's a title I was chained to for the 
first decade of my career. I've only recently decided to tackle Software 
Engineering full-time, and despite the challenges of changing careers, it has
kept me free of on-call pager duties.

That was until my company decided to start a new cloud-based service 
offering. This service was to be run 'DevOps' style - a perfect hybrid of
my experience in both System Administration and Software Engineering. To
scale this new service, we were going to use Chef for infrastructure
automation.

At this point, I was becoming well versed in Python. I had little or no
interest learning any other language, be it Chef's Ruby DSL, or Ruby itself.
However, I knew the pains of repetitive System Administration tasks. So Chef,
and Ruby, it would be.

I'm going to have to learn _Enough Ruby to be Dangerous_.


Ruby
====

What is Ruby, right?
--------------------

Ruby is a Python DSL for Hipsters.

j/k.

According to Yukihiro 'Matz' Matsumoto, the creator of Ruby:

> An interpreted scripting language for quick and easy object-oriented 
> programming.

Matz created Ruby in the 90's from a desire for a language more powerful
than Perl, and more object-oriented than Python.

Remember the mantra
-------------------

At it's heart, Ruby is meant to be *quick and easy*. It's an important
mantra to remember as you learn the language.

Why Ruby for Chef?
------------------

According to Adam, the creator of Chef, it comes down to ease-of-use:

1. Ruby has minimal syntax, so it takes very little code to get most common 
activities done.
2. The code should look as close to a configuration as possible. 
e.g. `package 'foo'`
3. Many of Adam's initial customers were Rails shops, so there was little
opposition to the adoption of yet-another Ruby app.

What's so different about Ruby?
-------------------------------

When Matz describes Ruby as an object-orient language, he really means that 
everything is an object.

For example, imagine the number '1'. There are various ways to describe the
number, for example, as an Integer. There are also a number of things that 
can be done to the number, such as changing it into a Floating Point Integer. 

This is how Ruby sees the world.

The line of Ruby below converts the integer 1 into a floating point integer:

    :::ruby
    1.to_f
     => 1.0

What about Strings? What can we do to strings? Well, they're objects too:

    :::ruby
    'taco'.reverse
     => "ocat"

In fact, everything you do something to an object in Ruby, you're really
just getting that object back, but changed. You can continue this recursion
almost indefinitely:

    :::ruby
    'taco'.reverse.reverse
     => "taco"

This is a little different than how other languages behave. In Python, for
example, it might look something like this:

    :::python
    >>> float(1)
    1.0
    >>> 'taco'[::-1]
    'ocat'

It's about the same amount of code, but unless you're reversing a string
every day in Python, are you really going to remember what `[::-1]` does? 

Ruby's `reverse` seems much more intuitive.


Style
=====

Once I grasped that everything in Ruby was an object, I started flexing my
object-oriented programming prowess. I would browse the [Ruby Standard Library](http://www.ruby-doc.org)
and chain together ridiculous programs, which, upon later inspection, even I
couldn't understand:

    :::ruby
    # I have no idea what this does:
    build = (url_body/'a').collect do |l|
      l.inner_html if l.inner_html.start_with? "#{name}-" 
    end.select{|i|!i.nil?}.sort{|x,y|y<=>x}.first


What did I learn?
-----------------

It's important to write code that other people can read. A great guideline 
for writing readable code is the [community-driven Ruby coding style guide](https://github.com/bbatsov/ruby-style-guide).

If you never go to another Ruby talk or read another Ruby book, do one thing: 
**Read & Use the Style Guide!**


Walk the Walk
=============

Aside from helping you write better code as a new developer, the Style Guide 
has the added benefit of training you in the descriptive lexicon of Ruby.
Speaking in the context and the convention of any language is a prerequisite 
for knowledge. Without integrating these conventions into your discussions
of Ruby, you'll be hard-pressed to find a forum guidance and support.

I consider this the classic problem of the verbosity of tech support requests.
Akin to the difference between "The website is down." and "I'm getting
'no route to host' when I try to ping the server."


Smoke some irb
==============

If you're ready to start flexing your own Ruby muscle, I recommend starting
with **irb**, Ruby's Interactive Shell. This tool allows a developer to
explore the language - experiment with code, test new ideas - all without
risking introducing bugs into existing programs (or production systems!):

Below are some examples of running some Ruby code through the irb Interactive
Shell. You'll see that irb provides a wide variety of information on the code 
being executed, the environment it's being executed in, and more:

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


irb comes installed with most standard Ruby distributions.


Primitive Primer
================

Before we dig any deeper, lets have a look at some of Ruby's primitive types. 
These are the fundamental - atomic - types of knowledge representation in
any language.

Below are some of primitive object types you'll be dealing with in Ruby:

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


The power of these primitives can be seen in the types of actions we can take
on them. We can introspect into this object and see what it's capable of
with the `method` method.

Here's a sample of some of the dozens of built-in things we can do to an
object type 'string':

    :::ruby
    'taco'.methods
     => ["upcase!", "zip", "find_index", "between?", "unpack", ...]

You've already seen an example of this with `reverse`:

    :::ruby
    'taco'.reverse
     => 'ocat'

In addition to the methods listed for each of the primitives, Ruby also
includes many built-in methods.

    :::ruby
    methods
    => ["irb_print_working_binding", "inspect", "workspaces", "tap", ...]

There are also many methods inherited from Unix system calls & Kernel:

    :::ruby
    Kernel.methods
    => ["inspect", "name", "private_class_method", "exit!", "chomp!", ...]


Libraries
=========

Languages gain their power through their extensibility, including their
ability to support incorporating external libraries. Ruby too has this power.
Using the `require` statement we can easily import libraries included in both 
the standard Ruby distribution, and those created by external authors. 

Here we're importing the `open-uri` library, which extends the
built-in `open` method to support.. opening URIs!:

    :::ruby
    require 'open-uri'
    gba = open('http://ampledata.org')


Files & Exceptions
==================

On to the fun stuff. Lets actually do something. Lets start by opening a
file. Since we've probably all got access to a Unix system, lets check 
out what our BOFH has left in our MOTD:

    open('/etc/motd', 'r')
     => Errno::ENOENT: No such file or directory - /etc/motd
      from (irb):1:in `initialize'
      from (irb):1:in `open'
      from (irb):1


Something's gone awry here. We raised an exception, or a program interrupt.
There's no shell return-codes here!

There's a lot of information contained in this exception. First, we can see
the name of this exception: **Errno::ENOENT**. Second, we've got a
helpful error message in **No such file or directory**. Finally the
path leading back to the code that caused our exception.

I was a sysadmin, I know that files (and filesystems) are never eternal. If 
our attempt to open a missing MOTD were actually a chunk of code running on a 
production server, we'd definitely get a page at 3AM. Luckily, we can 
proactively avoid this by catching this exception using Ruby's 
`begin`, `rescue` and `end` statements.

Here we're telling Ruby that we want to rescue the specific error 
**Errno::ENOENT**, and when it does happen, we actually just want to return
a friendlier message:

    :::ruby
    begin
      open('/etc/motd', 'r')
    rescue Errno::ENOENT
      "dude the file isn't there"
    end
     => "dude the file isn't there"

Awesome. Our pager is quiet, back to drinking.

But wait, we still don't have a MOTD!


RI & RDoc
=========

Since we're using `open` to try and read our MOTD, maybe we can also use it
to write our MOTD, here too Ruby can help. From the command line we can 
invoke the `ri` utility to look at the embedded documentation for `open`.

Here we're using `ri IO.open` to understand `open`'s capabilities:

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


The page above tell us that `IO.open` is really a synonym of `IO.new`, so
lets use `ri IO.new` to check out it's capabilities:

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

It looks like we can pass the `w` flag to `open` to write to files.


Will the real MOTD please stand up?
===================================

Where are we going to get the content for our MOTD? Luckily I know an
inspirational source:


    :::ruby
    require 'open-uri'
    fd = open('https://api.twitter.com/1/statuses/user_timeline.json?screen_name=georgetakei')
    fd.read
     => "[{\"created_at\":\"Sat May 05 15:27:11 +0000 2012\",\"id\":198795...

I have an idea for a Chef lightweight resource provider!


Of Resources & Men
==================

Real quick lets break down the components of a Chef Lightweight Resource
Provider, or LWRP:

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
      tw = 'https://api.twitter.com/1/statuses/user_timeline.json?screen_name='
      tweet = ''
    
      # Connect to twitter, ask them for the goods, parse the JSON:
      open(tw + new_resource.name, 'r'){ |t| tweet = JSON(t.read) }
    
      # Write only the text of the tweet to our file:
      open('/etc/motd', 'w'){ |m| m.write(tweet.first['text']) }
    
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
    [Sun, xxx -0700] DEBUG: Processing motd[georgetakei] on jupiter.splunk.com
    [Sun, xxx -0700] INFO: Processing motd[georgetakei] action create (motd::default line 1)
     => true
    chef:recipe > open('/etc/motd').read
     => "Ke$ha dubs herself \"Pop's dirty little sister.\" Didn't realize she was from\nthe Ozarks."


Testing
=======

> Nothing in possible in programming if it's not tested.
Lets refactor our MOTD Provider out to a Library that we can then 
test it at the unit level: `vi motd/libraries/default.rb`

    :::ruby
    require 'open-uri'
    require 'json'
    
    tw = 'https://api.twitter.com/1/statuses/user_timeline.json?screen_name='
    
    # Connects to twitter, retrieves tweets for screen_name.
    def get_tweet(screen_name)
      open(tw + screen_name, 'r'){ |t| JSON(t.read) }
    end
    
    # Writes tweet out to /etc/motd.
    def write_motd(tweet)
      open('/etc/motd', 'w'){ |m| m.write(tweet) }
    end

Now lets create some tests for our Library: `vi motd/libraries/default.rb`

    :::ruby
    require 'test/unit'
    
    class TestMOTDLibrary < Test::Unit::TestCase
      def test_get_tweet
        tweets = get_tweets('georgetakei')
        tweet = tweets.first['text']
    
        assert_kind_of(String, tweet)
        assert_match(/Shields Up!/, tweet)
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
    </Shields Up!/>.
    
    2 tests, 3 assertions, 1 failures, 0 errors

Oh, right :)


References
==========

* [MOTD Chef Cookbook](https://github.com/ampledata/cookbook-motd)
* [A community-driven Ruby coding style guide](https://github.com/bbatsov/ruby-style-guide)
* [Unit Testing in Ruby](http://en.wikibooks.org/wiki/Ruby_Programming/Unit_testing)
* [Just Enough Ruby for Chef](http://wiki.opscode.com/display/chef/Just+Enough+Ruby+for+Chef)
* [_why's (poignant) Guide to Ruby](http://mislav.uniqpath.com/poignant-guide/)
* [Programming Ruby](http://www.rubycentral.com/pickaxe/)