#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import datetime, calendar
import argparse

import shell_conf


"""
parser = argparse.ArgumentParser(description='Process files.')
parser.add_argument('--year', action='store', nargs="?", help='year to process or --year= for current')
parser.add_argument('--month', action='store', nargs="?", help='month to process or --month= for current')
parser.add_argument('--day', action='store', nargs="?", help='day to process or --day= for current')

args = parser.parse_args()

"""

from imports.ourairports import process_runways

process_runways.run()


