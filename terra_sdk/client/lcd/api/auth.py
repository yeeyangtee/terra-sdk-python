from typing import Union

from terra_sdk.core import AccAddress
from terra_sdk.core.auth import Account, PeriodicVestingAccount

from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncAuthAPI", "AuthAPI"]


class AsyncAuthAPI(BaseAsyncAPI):
    async def account_info(
        self, address: AccAddress
    ) -> Union[Account, PeriodicVestingAccount]:
        """Fetches the account information.

        Args:
            address (AccAddress): account address

        Returns:
            Union[Account, PeriodicVestingAccount]: account information
        """
        result = await self._c._get(f"/auth/accounts/{address}")
        if result["type"] == "core/Account":
            return Account.from_data(result)
        else:
            return PeriodicVestingAccount.from_data(result)


class AuthAPI(AsyncAuthAPI):
    @sync_bind(AsyncAuthAPI.account_info)
    def account_info(
        self, address: AccAddress
    ) -> Union[Account, PeriodicVestingAccount]:
        pass

    account_info.__doc__ = AsyncAuthAPI.account_info.__doc__
