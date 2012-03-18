#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

#import argparse
from optparse import OptionParser

import shell_conf

## TODO - option params

import imports.ourairports.fetch_files

imports.ourairports.fetch_files.fetch_all()

