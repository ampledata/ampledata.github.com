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
    index_body = '<h1>ampledata.org articles</h1>'

    with open('header.html', 'r') as header_fd:
        generic_header = header_fd.read()

    with open('footer.html', 'r') as footer_fd:
        generic_footer = footer_fd.read()

    articles = glob.glob('*.md')
    for article in articles:
        article_content = ''

        article_name, _ = os.path.splitext(article)
        html_file = '.'.join([article_name, 'html'])
        friendly_name = article_name.replace('_', ' ')

        if not article_name == 'LICENSE':
            index_body = '\n'.join((
                index_body,
                "<li><a href='%s'>%s</a></li>" % (html_file, friendly_name)))

        print "in: %s" % article
        print "out: %s" % html_file

        with open(article, 'r') as article_fd:
            article_content = article_fd.read()

        article_body = markdown.markdown(article_content, ['codehilite'])
        article_headline = "<h1>%s</h1>" % friendly_name
        article_title = "<title>%s</title>" % friendly_name

        header = '\n'.join(
            ('<head>', generic_header, article_title, '</head>'))

        body = '\n'.join(
            ('<body>', article_headline, article_body, generic_footer,
            '</body>'))

        with open(html_file, 'w') as html_fd:
            html_fd.write(header)
            html_fd.write(body)

    index_title = '<title>ampledata.org</title>'
    index_header = '\n'.join(
        ('<head>', generic_header, index_title, '</head>'))

    with open('index.html', 'w') as index_fd:
        index_fd.write(index_header)
        index_fd.write(index_body)
        index_fd.write(generic_footer)


if __name__ == '__main__':
    main()
