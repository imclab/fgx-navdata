#!/usr/bin/env python

import yaml

f = open("fields.yaml", "r")

y = yaml.load( f.read() )

print y
f.close()


f = open("models.yaml", "r")

y = yaml.load( f.read() )

print y
f.close()
