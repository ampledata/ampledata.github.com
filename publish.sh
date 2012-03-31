#!/usr/bin/env bash
# Publishes articles.
#
# @author: Greg Albrecht <gba@splunk.com>
# @copyright: Copyright 2012 Greg Albrecht
# @license: Creative Commons Attribution 3.0 Unported License.
# @url: http://ampledata.org/


git commit -m 'publishing articles' *.md *.html
git push origin
