"""Overtime"""

import atexit
import json

import QLog
from QLog import LogLevel
from QLog.console_logger import ConsoleLogger

from containers import Configs, Services


def main():
    """ Main """
    QLog.loggers = [ConsoleLogger(LogLevel.DEBUG)]

    # Load the config
    with open('../config/config.json') as config_file:
        Configs.config.from_dict(json.load(config_file))

    atexit.register(exit_handler)

    Services.toggl_service().start()


def exit_handler():
    """Exit handler"""
    Services.toggl_service().shutdown()


if __name__ == "__main__":
    main()
