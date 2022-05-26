#!/usr/bin/env python3

from firePlace import FirePlace
import time

fp = FirePlace()

fp.start()
time.sleep(5)
fp.stop()