""" The containers for dependency injection """

from dependency_injector import containers, providers

from services.toggl_service.toggl_service import TogglService


class Configs(containers.DeclarativeContainer):
    """ Configuration """
    config = providers.Configuration('config')


class Services(containers.DeclarativeContainer):
    """ Services """
    toggl_service = providers.Singleton(TogglService, Configs.config)
