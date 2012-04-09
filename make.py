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


def generate_header():
    with open('header.html', 'r') as header_fd:
        generic_header = header_fd.read()
    return generic_header


def generate_index(articles):
    generic_header = generate_header()
    generic_footer = generate_footer()
    index_body = "<h1>Greg Albrecht's ampledata.org</h1>"
    index_body = '\n'.join([index_body, '<h2>Articles</h2>'])
    index_body = '\n'.join([index_body, '<ul>'])

    for article in articles:
        article_item = (
            "<li><a href='%s'>%s</a></li>"
            % (article['html_file'], article['friendly_name']))
        index_body = '\n'.join([index_body, article_item])
    index_body = '\n'.join([index_body, '</ul>'])

    index_title = "<title>Greg Albrecht's ampledata.org</title>"
    index_header = '\n'.join(
        ['<head>', generic_header, index_title, '</head>'])

    with open('index.html', 'w') as index_fd:
        index_fd.write('\n'.join(['<!DOCTYPE html>', '<html lang="en">']))
        index_fd.write(index_header)
        index_fd.write('<body>\n')
        index_fd.write(index_body)
        index_fd.write(generic_footer)
        index_fd.write('\n</body>')
        index_fd.write('\n'.join(['</html>']))


def generate_footer():
    with open('footer.html', 'r') as footer_fd:
        generic_footer = footer_fd.read()
    return generic_footer


def generate_article_names(article_file):
    article = {}
    article['name'], _ = os.path.splitext(article_file)
    article['file'] = article_file
    article['html_file'] = '.'.join([article['name'], 'html'])
    article['friendly_name'] =  article['name'].replace('_', ' ')
    return article


def generate_articles(articles):
    generic_header = generate_header()
    generic_footer = generate_footer()
    for article in articles:
        article_content = ''

        print "in: %s" % article['file']
        print "out: %s" % article['html_file']

        with open(article['file'], 'r') as article_fd:
            article_content = article_fd.read()

        article_body = markdown.markdown(article_content, ['codehilite'])
        article_headline = "<h1>%s</h1>" % article['friendly_name']
        article_title = "<title>%s</title>" % article['friendly_name']

        header = '\n'.join(
            ['<head>', generic_header, article_title, '</head>'])

        body = '\n'.join(
            ['<body>', article_headline, article_body, generic_footer,
            '</body>'])

        with open(article['html_file'], 'w') as html_fd:
            html_fd.write('\n'.join(['<!DOCTYPE html>', '<html lang="en">']))
            html_fd.write(header)
            html_fd.write(body)
            html_fd.write('\n'.join(['</html>']))


def main():
    """Reads in all article content and renders to HTML."""
    article_files = glob.glob('*.md')
    articles = []
    for article_file in article_files:
        articles.append(generate_article_names(article_file))

    generate_articles(articles)
    generate_index(articles)


if __name__ == '__main__':
    main()
