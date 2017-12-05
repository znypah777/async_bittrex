from bittrex.bases.factory import ProtectedSectionBaseFactory



market_factory = ProtectedSectionBaseFactory()


from .v1 import Market_v1_1

market_factory.register("v1.1", Market_v1_1)