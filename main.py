#!/usr/bin/python3

from modules.Monitoring import *
from modules.Logging import *
from modules.Utils import *

if __name__ == "__main__":
    logger.info(log("Starting monitoring user keyboard's input"))
    start_input_monitoring()
