# Makefile for http://ampledata.org/ blog.
#
# @author: Greg Albrecht <gba@splunk.com>
# @copyright: Copyright 2012 Greg Albrecht
# @license: Creative Commons Attribution 3.0 Unported License.
# @url: http://ampledata.org/


.DEFAULT: init


init:
	pip install -r requirements.txt --use-mirrors
	pygmentize -S default -f html -a html -a 'div.codehilite' > syntax.css

build:
	python bin/make.py

publish:
	git commit -m 'publishing articles' articles/*.md *.html *.xml
	git push origin

lint:
	pylint -f parseable -i y -r y bin/*.py | tee pylint.log

flake8:
	flake8 --exit-zero  --max-complexity 12 bin/*.py | \
		awk -F\: '{printf "%s:%s: [E]%s\n", $$1, $$2, $$3}' | tee flake8.log

pep8: flake8

clonedigger:
	clonedigger --cpd-output .

nosetests:
	nosetests -c nosetests.cfg bin/*.py

test: init lint flake8 clonedigger nosetests
