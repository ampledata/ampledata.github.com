# DRAFT
gba@20130507 This article is a **DRAFT**.

# Abstract
This article describes a method for integrating [Foursquare](http://foursquare.com) check-ins with (Automatic Packet Reporting System)[http://en.wikipedia.org/wiki/Automatic_Packet_Reporting_System] (APRS) position reports. Using this integration, a licensed [Amateur Radio](http://www.arrl.org/what-is-ham-radio) operator can have location check-ins on Foursquare automatically transmitted to the world-wide APRS network. The software and endpoints for this integration are written using Python.

# Background
Foursquare is a location-based social network that allows check-ins at venues or locations using a mobile device (ie Phone, Tablet, Web). These check-ins note the coordinates of the associated location or venue.

APRS is a packet-based reporting system used by Amateur Radio operators world-wide. Typically report packets are transmitted over Amateur Radio frequencies (such as 144.39MHz in North America). However, the APRS Internet System (APRS-IS) allows packets to be transmitted and received over the internet, creating a gateway between radio and the internet.

# Requirements
1. A [Amateur Radio License](http://www.arrl.org/licensing-preparation-exams)
2. A [Zapier](http://zapier.com) account.
3. A [Foursquare](http://foursquare.com) account.

# Setup
The instructions below walk through Zapier's steps for setting up the Foursquare to APRS integration.

## Step 1: "Pick your Trigger and Action for this Zap"

1. From Zapier, login, go to your Dashboard, and select **Create a New Zap**.
2. For **Trigger Service** select **Foursquare**.
3. For **Trigger** select **New Checkin**.
4. For **Action Service** select **APRS**.
5. For **Action** select **Create Message**.

## Step 2: "Select a Foursquare Account"

Select your Foursquare account.

## Step 3: "Select a APRS Account"

Update the credentials for your APRS-IS account. 

1. Enter any **Name** for the account.
2. Enter your **Callsign** plus a station number (-10 is recommended).
3. Enter your APRS-IS **Passcode**. (TK)

![](http://dl.dropbox.com/u/4036736/Screenshots/24j35_5po0uq.png)

## Step 4: "Filter your Foursquare checkins"

No filters are needed, so you can skip this step.

## Step 5: "Create your APRS Message"

1. For **Message** enter **Foursquare Checkin at: {{venue__name}}**
2. For **Latitude** enter **{{venue__location__lat}}**
3. For **Longitude** enter **{{venue__location__lng}}**

![](http://dl.dropbox.com/u/4036736/Screenshots/yfx6cco_dzvj.png)

## Step 6: "Try out your Zap"

Test this integration, if you'd like.

## Step 7: "Enable your Foursquare to APRS Zap"

Select **Make Zap Live**.

## Done!
