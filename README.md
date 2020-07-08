# Just Enough Blog

[![Build Status](https://secure.travis-ci.org/ampledata/ampledata.github.com.png?branch=master)](http://travis-ci.org/ampledata/ampledata.github.com)

## Manifesto

> I just wanted a way of sharing my ideas with the internet. I didn't want
> a full featured 'blog' platform. I will know this project succeeded when
> I can create an article of ideas using no more than my favorite text
> editor in the world, vim.


## The Deal

- I want to create articles of ideas using vim.
- I want to write these articles in Markdown format.
- I want to include code snippets in these articles.
- I want these code snippets to include syntax highlighting.


## How

1. By whatever means, download the contents of this directory.
2. Install the prerequisite Python Modules and generate some CSS.
3. Write an article and render it into HTML.
4. Publish.

As seen from the command line:

```bash
git clone https://github.com/ampledata/ampledata.github.com.git
cd ampledata.github.com
make init
vi articles/how_does_beer_work.md
make build
make publish
```


## Meta

- Author: Greg Albrecht <gba@gregalbrecht.com>
- Copyright: Copyright 2020 Greg Albrecht
- License: Creative Commons Attribution 3.0 Unported License.
- URL: <http://ampledata.org/>
- Twitter: [@ampledata](http://twitter.com/ampledata)
- Github: [ampledata](https://github.com/ampledata)
