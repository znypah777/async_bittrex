
<<<<<<< HEAD
from async_bittrex.bases.factory import InternalGroupFactory



internalgroup_factory = InternalGroupFactory()


from .v1 import BaseGroup_v1_1, BaseGroupV2_2
internalgroup_factory.register("v1.1", BaseGroup_v1_1)
internalgroup_factory.register("v2.0", BaseGroupV2_2)
=======
from async_bittrex.bases.factory import BaseGroupFactory



basegroup_factory = BaseGroupFactory()


from .v1 import BaseGroup_v1_1
basegroup_factory.register("v1.1", BaseGroup_v1_1)
>>>>>>> 2848be7fbd43c38bbf7a58905e918fd5508c0b4b
