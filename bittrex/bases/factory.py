import aiohttp

from typing import Any


class _BaseFactory:
    def __init__(self):

        self._versions = {}


    def register(self, version, cls):
        if self._versions.get(version) is None:
            self._versions[version] = cls

    def get_version(self, version):
        if version in self._versions:
            return self._versions[version]
        raise ValueError("Unknown Version")

class PublicSectionBaseFactory(_BaseFactory):

    def __call__(self, session:aiohttp.ClientSession, api_secret:str, api_version: str) -> Any:
        version = self.get_version(api_version)
        return version(session, api_secret, api_version)
        # if api_version in self._versions:
        #     return self._versions[api_version](session, api_secret, api_version)
        # raise ValueError("Unknown Version")



class ProtectedSectionBaseFactory(PublicSectionBaseFactory):
    def __call__(self, session: aiohttp.ClientSession, api_key:str, api_secret: str, api_version: str) -> Any:
        version = self.get_version(api_version)
        return version(session, api_key, api_secret, api_version)
        # if api_version in self._versions:
        #     return self._versions[api_version](session, api_key, api_secret, api_version)
        # raise ValueError("Unknown Version")



class BaseGroupFactory(_BaseFactory):
    def __call__(self, session: aiohttp.ClientSession, group_version: str) -> None:
        version = self.get_version(group_version)
        return version(session, group_version)
        # if group_version in self._versions:
        #     return self._versions[group_version](session, group_version)
        # raise ValueError("Unknown Version")


