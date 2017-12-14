import aiohttp

from typing import Any, Union, Dict


class _BaseFactory:
    """
    Base Factory for Building The classes
    """
    def __init__(self):

        self._versions = {}

    def get_version(self, version:str) -> Union[object, Dict[str, object]]:
        if version in self._versions:
            return self._versions[version]
        raise ValueError("Unknown Version")


class AccessLevelGroupFactory(_BaseFactory):
    def register(self, version:str , cls:object, group:object) -> None:
        if self._versions.get(version) is None:
            self._versions[version] = {"access_level": cls,
                                       "internal_group": group}



class _SectionFactory(_BaseFactory):
    """
    Base Factory for the actual Sections. e.g Public Market and Account
    """
    def register(self, version:str , cls:object, group:object, endpoints: Dict[str, str]) -> None:
        if self._versions.get(version) is None:
            self._versions[version] = {"section": cls,
                                       "access_group": group,
                                       "endpoints": endpoints}

class PublicSectionFactory(_SectionFactory):
    """
    Factory for all the public sections.
    as of v1.1 the Bittrex api only has one public section called public
    """



    def __call__(self, session:aiohttp.ClientSession, api_secret:str, api_version: str) -> Any:
        version = self.get_version(api_version)
        internal_group = version["access_group"]["internal_group"](session, api_secret, api_version)
        access_group = version["access_group"]["access_level"](internal_group)
        section = version["section"](access_group, version["endpoints"])
        return section


class ProtectedSectionFactory(_SectionFactory):
    """
       Factory for all the protectd sections.
       as of v1.1 the Bittrex api only has 2 protected sections called called Market and Account
    """
    def __call__(self, session: aiohttp.ClientSession, api_key:str, api_secret: str, api_version: str) -> Any:
        version = self.get_version(api_version)
        base = version["access_group"]["internal_group"](session, api_secret, api_version)
        group = version["access_group"]["access_level"](api_key, base)
        section = version["section"](group, version["endpoints"])
        return section



class InternalGroupFactory(_BaseFactory):
    """
        This class is for the InternalGroup. the InternalGroup being the class that has methods that both
        the public and protected group wil be using
    """

    def __call__(self, session: aiohttp.ClientSession, group_version: str) -> object:
        version = self.get_version(group_version)
        return version(session, group_version)

    def register(self, version: str, cls: object) -> None:
        if self._versions.get(version) is None:
            self._versions[version] = cls


