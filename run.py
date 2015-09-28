#!/usr/bin/env python

import sys
sys.path.insert(0, '../..')

import db
db.initialize()

import app
app.main()
