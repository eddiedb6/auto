import sys
import os
import logging

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], ".."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../afw"))

from AFW import AFW

auto = AFW()
auto.LogLevel = logging.DEBUG
auto.BreakTime = 200 # ms

if auto.Load(os.path.join(os.path.split(os.path.realpath(__file__))[0], "scripts/Config.py")):
    if auto.Execute():
        pass
auto.Destroy()


