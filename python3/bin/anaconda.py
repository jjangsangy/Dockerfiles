#!/usr/bin/env python
from __future__ import print_function

import json
import sys
from os.path import abspath

try:
    from urllib.request import urlopen, Request, urlparse
    from urllib.parse import urljoin
except ImportError:
    from urllib2 import Request, urlopen
    from urlparse import urlparse, urljoin

from functools import wraps

def connect(func):

    @wraps(func)
    def wrap(*args, **kwargs):
        prepared = func(*args, **kwargs)
        req  = urlopen(prepared)
        if req.msg != 'OK':
            raise IOError('Bad Request')
        raw  = req.read()
        return json.loads(raw.decode('utf-8'))

    return wrap

@connect
def get_content(parsed_url):
    headers = {
        'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json; charset=utf-8;',
        'Accept-Language': 'en-US,en;q=0.8', 'Accept-Charset': 'utf-8',
    }
    params = {
        "headers": headers,
        "origin_req_host": parsed_url.hostname
    }

    return Request(parsed_url.geturl(), **params)


def main(url):
    parsed_url    = urlparse(url)
    conda_files   = get_content(parsed_url)
    return max(urljoin(url, i) for i in conda_files if i.endswith('Linux-x86_64.sh'))


if __name__ == '__main__':
    print(main('http://repo.continuum.io/archive/.files.json'), file=sys.stdout, end='')

