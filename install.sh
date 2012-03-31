#!/usr/bin/env bash
# Installs prerequities for generating articles.
#
# @author: Greg Albrecht <gba@splunk.com>
# @copyright: Copyright 2012 Greg Albrecht
# @license: Creative Commons Attribution 3.0 Unported License.
# @url: http://ampledata.org/


pip install -r requirements.txt

# CSS, despite its faults, is good:
# http://www.w3.org/Protocols/HTTP/Performance/Pipeline.html
pygmentize -S default -f html -a html -a 'div.codehilite' > syntax.css
