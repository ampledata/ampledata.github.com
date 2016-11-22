# Makefile for http://ampledata.org/ blog.
#
# @author: Greg Albrecht <gba@gregalbrecht.com>
# @copyright: Copyright 2012 Greg Albrecht
# @license: Creative Commons Attribution 3.0 Unported License.
# @url: http://ampledata.org/
#


.DEFAULT_GOAL: all


all: install_requirements create_css build

install_requirements:
	pip install -r requirements.txt

create_css:
	pygmentize -S default -f html -a html -a 'div.codehilite' > syntax.css

build:
	jeb
	python stories.py

publish:
	git commit -m 'publishing articles' articles/*.md *.html *.xml
	git commit -m 'publishing stories' stories/*.md *.html *.xml
	git push origin
