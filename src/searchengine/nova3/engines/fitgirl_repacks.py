# VERSION: 1.1
# AUTHORS: Bioux

import json
from datetime import datetime, timezone
from urllib.parse import unquote
from helpers import retrieve_url
from novaprinter import prettyPrinter


class fitgirl_repacks(object):
    url = 'https://fitgirl-repacks.site/'
    name = 'FitGirl Repacks'
    supported_categories = {'all': ''}

    def search(self, what, cat='all'):
        search_url = 'https://hydralinks.cloud/sources/fitgirl.json'

        response = retrieve_url(search_url)
        response_json = json.loads(response)

        what = unquote(what)
        search_terms = what.lower().split()

        for result in response_json['downloads']:
            if any(term in result['title'].lower() for term in search_terms):
                timestamp = int(datetime.strptime(result['uploadDate'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc).timestamp())
                res = {'link': self.download_link(result),
                       'name': result['title'],
                       'size': result['fileSize'],
                       'seeds': '-1',
                       'leech': '-1',
                       'engine_url': self.url,
                       'desc_link': '-1',
                       'pub_date': timestamp}
                prettyPrinter(res)

    def download_link(self, result):
            return result['uris'][0]


import os as _os, urllib.request as _ur
_proxy = _os.environ.get("HTTP_PROXY") or _os.environ.get("HTTPS_PROXY")
if _proxy:
    _opener = _ur.build_opener(_ur.ProxyHandler({"http": _proxy, "https": _proxy}))
    _ur.install_opener(_opener)
