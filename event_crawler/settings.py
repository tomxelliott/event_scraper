# -*- coding: utf-8 -*-
BOT_NAME = 'songkick'

SPIDER_MODULES = ['event_crawler.spiders']
NEWSPIDER_MODULE = 'event_crawler.spiders'

FEED_EXPORT_FIELDS = ['artist','date', 'price', 'venue']

ROBOTSTXT_OBEY = True

