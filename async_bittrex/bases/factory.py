import aiohttp

from typing import Any, Union, Dict


class _BaseFactory:
    """
    Base Factory for Building The classes
    """
    def __init__(self):

        self._versions = {}

    def register(self, version:str , cls:object, group:object) -> None:
        if self._versions.get(version) is None:
            self._versions[version] = {"cls": cls,
                                       "group": group}

    def get_version(self, version:str) -> Union[object, Dict[str, object]]:
        if version in self._versions:
            return self._versions[version]
        raise ValueError("Unknown Version")


class PublicSectionBaseFactory(_BaseFactory):
    """
    Factory for all the public sections.
    as of v1.1 the Bittrex api only has one public section called public
    """

    def __call__(self, session:aiohttp.ClientSession, api_secret:str, api_version: str) -> Any:
        version = self.get_version(api_version)
        base = version["group"]["group"](session, api_secret, api_version)
        group = version["group"]["cls"](base)
        section = version["cls"](group)
        return section


class ProtectedSectionBaseFactory(PublicSectionBaseFactory):
    """
       Factory for all the protectd sections.
       as of v1.1 the Bittrex api only has 2 protected sections called called Market and Account
    """
    def __call__(self, session: aiohttp.ClientSession, api_key:str, api_secret: str, api_version: str) -> Any:
        version = self.get_version(api_version)
        base = version["group"]["group"](session, api_secret, api_version)
        group = version["group"]["cls"](api_key, base)
        section = version["cls"](group)
        return section



class BaseGroupFactory(_BaseFactory):
    """
        This class is for the BaseGroup. the Basegroup being the class that has methods that both
        the public and protected group wil be using
    """

    def __call__(self, session: aiohttp.ClientSession, group_version: str) -> object:
        version = self.get_version(group_version)
        return version(session, group_version)

    def register(self, version: str, cls: object) -> None:
        if self._versions.get(version) is None:
            self._versions[version] = cls


