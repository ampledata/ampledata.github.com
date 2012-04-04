#!/usr/bin/env python
"""Generate syntax highlighted articles from Markdown.

Derived from stefanB's blog post: http://bit.ly/H0qZ3O
"""
__author__ = 'Greg Albrecht <gba@splunk.com>'
__copyright__ = 'Copyright 2012 Greg Albrecht'
__license__ = 'Creative Commons Attribution 3.0 Unported License'


import glob
import os

import markdown


def main():
    """Reads in all article content and renders to HTML."""
    index_html = ''

    with open('header.html', 'r') as header_fd:
        header = header_fd.read()

    with open('footer.html', 'r') as footer_fd:
        footer = footer_fd.read()

    articles = glob.glob('*.md')
    for article in articles:
        article_content = ''

        article_name, _ = os.path.splitext(article)
        html_file = '.'.join([article_name, 'html'])
        friendly_name = article_name.replace('_', ' ')

        index_html = ''.join((
            index_html,
            "<li><a href='%s'>%s</a></li>" % (html_file, friendly_name)))

        print "in: %s" % article
        print "out: %s" % html_file

        with open(article, 'r') as article_fd:
            article_content = article_fd.read()

        html_output = markdown.markdown(article_content, ['codehilite'])

        with open(html_file, 'w') as html_fd:
            html_fd.write(header)
            html_fd.write(html_output)
            if article_name != 'LICENSE':
                html_fd.write(footer)

    with open('index.html', 'w') as index_fd:
        index_fd.write(header)
        index_fd.write(index_html)
        index_fd.write(footer)


if __name__ == '__main__':
    main()
