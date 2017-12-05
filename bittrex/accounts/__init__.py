from bittrex.bases.factory import ProtectedSectionBaseFactory


account_factory = ProtectedSectionBaseFactory()





from .v1 import Account_v1_1

account_factory.register("v1.1", Account_v1_1)


