#!/usr/bin/env bash
# Makefile for http://ampledata.org/ blog.
#
# @author: Greg Albrecht <gba@splunk.com>
# @copyright: Copyright 2012 Greg Albrecht
# @license: Creative Commons Attribution 3.0 Unported License.
# @url: http://ampledata.org/


init:
	pip install -r requirements.txt
	pygmentize -S default -f html -a html -a 'div.codehilite' > syntax.css

build:
	python bin/make.py

publish:
	git commit -m 'publishing articles' articles/*.md *.html
	git push origin
