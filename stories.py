#!/usr/bin/env python

import glob
import sys

import jeb


def main():
    stories = []
    
    story_files = glob.glob('stories/*.md')
    
    for story_file in story_files:
        stories.append(jeb.generate_article_names(story_file))
    
    jeb.generate_articles(stories)


if __name__ == '__main__':
    sys.exit(main())
