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
import jinja2


JINJA2_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates']))


def generate_article_names(article_file):
    article = {}
    article['name'] = os.path.basename(os.path.splitext(article_file)[0])
    article['file'] = article_file
    article['html_file'] = '.'.join([article['name'], 'html'])
    article['friendly_name'] =  article['name'].replace('_', ' ')
    return article


def generate_index(articles):
    index_title = "Greg Albrecht's ampledata.org"

    index_template = JINJA2_ENV.get_template('index.html')

    rendered_index = index_template.render(title=index_title, articles=articles)

    with open('index.html', 'w') as index_fd:
        index_fd.write(rendered_index)


def generate_articles(articles):
    article_template = JINJA2_ENV.get_template('article.html')

    for article in articles:
        article_content = ''

        print "in: %s" % article['file']
        print "out: %s" % article['html_file']

        with open(article['file'], 'r') as article_fd:
            article_content = article_fd.read()

        article_content = markdown.markdown(article_content, ['codehilite'])

        rendered_article = article_template.render(
            title=article['friendly_name'], article_content=article_content)
        
        with open(article['html_file'], 'w') as article_fd:
            article_fd.write(rendered_article)


def main():
    """Reads in all article content and renders to HTML."""
    article_files = glob.glob('articles/*.md')
    articles = []
    for article_file in article_files:
        articles.append(generate_article_names(article_file))

    generate_articles(articles)
    generate_index(articles)


if __name__ == '__main__':
    main()
