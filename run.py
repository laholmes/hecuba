#!/usr/bin/env python

import sys
sys.path.insert(0, '../..')

import db
db.create_tables()

from app import app
app.run()
