#!/usr/bin/env python

import sys
sys.path.insert(0, '../..')

import db
db.initialize()

from app import app
app.run()
