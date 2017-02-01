# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from myproject import settings

class MyprojectPipeline(object):
    def process_item(self, item, spider):
        return item

class ImageDownloadPipeline(object):
    def process_item(self, item, spider):
        if 'img_urls' in item:
            dirpath = '%s/%s' % (settings.IMAGES_STORE, spider.name)
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)

            request_data = {'allow_redirects': False,
             'auth': None,
             'cert': None,
             'data': {},
             'files': {},
             'headers': {'User-Agent': settings.USER_AGENT},
             'method': 'get',
             'params': {},
             'proxies': {},
             'stream': True,
             'timeout': 30,
             'url': '',
             'verify': True}

            for url in item['img_urls']:
                print('    >> %s' % url)

                filename = '_'.join(url.split('/')[5:])
                filepath = '%s/%s' % (dirpath, filename)
                if os.path.exists(filepath):
                    continue

                request_data['url'] = url
                with open(filepath, 'wb') as handle:
                    response = requests.request(**request_data)
                    for block in response.iter_content(8192):
                        if not block:
                            break
                        handle.write(block)
        pass
