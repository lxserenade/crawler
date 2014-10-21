#!/use/bin/env python
#-*- coding:utf8 -*-
import os,sys
import urllib
import re
import json
import csv


fl=open('data.txt')
data=fl.readlines()

print len(data)

fl.close()

