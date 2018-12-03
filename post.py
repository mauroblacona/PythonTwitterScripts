#!/usr/bin/python

import random

from data import api

api.PostUpdate("Tweet automatico: {}".format(random.randint(1, 100)))
