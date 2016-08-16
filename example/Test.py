import sys
import logging
sys.path.append("..")

from afw.AFW import AFW

auto = AFW()
auto.LogLevel = logging.DEBUG
auto.BreakTime = 100 # ms
if auto.Load("scripts/Config.py"):
    auto.Execute()

