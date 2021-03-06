#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to create skeleton posts
"""

import os
import argparse
from datetime import datetime
from pytz import timezone
from string import Template

from slugify import slugify


def parse_argument():
    parser = argparse.ArgumentParser(description='Create skeleton posts.')
    parser.add_argument('title', help="title of the the post")
    parser.add_argument('category', help="category of this post")
    parser.add_argument('tags', nargs='*',
                        help="tags for this post")
    parser.add_argument('--output', help="output folder default=./content",
                        default="content")
    return parser.parse_args()


def get_post_date():
    loc_tz = timezone('Asia/Manila')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    loc_dt = loc_tz.localize(datetime.today())
    return loc_dt.strftime(fmt)


header = """Title: $title
Date: $date
Category: $category
Slug: $slug
Tags: $tags
Authors: Blue Cuenca
Summary:


<!-- start here -->
"""


def normalize_tags(category, tags_str):
    if isinstance(tags_str, basestring):
        tags = [tag.strip() for tag in tags_str.split(',')]
    else:
        tags = tags_str
    cat = category.strip()
    while cat in tags:
        tags.remove(cat)
    return ",".join(tags)


def get_post_header(cargs):
    tags = cargs.tags
    title = cargs.title
    slug = slugify(title)
    category = cargs.category
    tags_str = normalize_tags(category, tags)
    template = Template(header)
    return template.substitute({
            'title': title,
            'tags': tags_str,
            'category': category,
            'slug': slug,
            'date': get_post_date(),
           })


def get_filename(title):
    return "%s.md" % slugify(title)


def main():
    args = parse_argument()
    output = args.output

    p = os.getcwd()
    outpath = os.path.join(p, output)

    filename = get_filename(args.title)
    if os.path.exists(outpath):
        filename = os.path.join(outpath, filename)

    content = get_post_header(args)

    prefixes = ["_posts", "content", ""]
    for prefix in prefixes:
        if os.path.isdir(prefix):
            break

    filespec = os.path.join(prefix, filename)

    with open(filespec, 'wxt') as f:
        f.write(content)
    print filespec


if __name__ == "__main__":
    import sys
    sys.exit(main())
