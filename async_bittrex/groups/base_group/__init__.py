
from async_bittrex.bases.factory import BaseGroupFactory



basegroup_factory = BaseGroupFactory()


from .v1 import BaseGroup_v1_1
basegroup_factory.register("v1.1", BaseGroup_v1_1)
