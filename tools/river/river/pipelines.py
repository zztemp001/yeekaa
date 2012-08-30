# coding=utf-8

import sqlite3
from os import path

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

class DBPipeline(object):
    filename = 'river\\data\\data.sqlite'

    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)

    def process_item(self, item, spider):
        self.conn.execute('insert into origin values (?,?,?)', (item['url'], item['body'], item['timestamp']))
        return item

    def initialize(self):
        if path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = sqlite3.connect(self.filename)
            self.conn.execute("""create table origin (link text primary key, body text, timestamp text)""")
            self.conn.commit()

        # 没有这一句，会报错。参考：http://python.6.n6.nabble.com/CPyUG-sqlite3-td2828909.html
        self.conn.text_factory = 'utf-8'

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None