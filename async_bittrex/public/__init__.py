from async_bittrex.bases.factory import PublicSectionBaseFactory



public_factory = PublicSectionBaseFactory()




from .v1 import Public_v1_1

public_factory.register("v1.1", Public_v1_1)