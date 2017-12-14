from async_bittrex.bases.factory import ProtectedSectionFactory
from async_bittrex.groups.protected_group import protected_group_factory


account_factory = ProtectedSectionFactory()





from .v1 import Account_v1_1

v1_1_endpoints = dict(BALANCE="/account/getbalance",
                      DEPOSIT_ADDRESS="/account/getdepositaddress",
                      WITHDRAW="/account/withdraw",
                      ORDER="/account/getorder",
                      ORDER_HISTORY="/account/getorderhistory",
                      WITHDRAWAL_HISTORY="/account/getwithdrawalhistory",
                      DEPOSIT_HISTORY="/account/getdeposithistory")

account_factory.register("v1.1", Account_v1_1, protected_group_factory.get_version("v1.1"), v1_1_endpoints)


