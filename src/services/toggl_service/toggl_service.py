"""The service to communication with Toggl."""
from services.service import Service


class TogglService(Service):

    """The service to communication with Toggl"""

    def __init__(self, config):
        """Constructor"""
        self.config = config

    def start(self):
        """Starts service"""

    def shutdown(self):
        """Shuts service down"""
