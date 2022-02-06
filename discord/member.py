# -*- coding: utf-8 -*-
# cython: language_level=3
# Copyright (c) 2021-present VincentRPS

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE
"""Represents a Discord Member

ref: https://discord.dev/resources/guild#guild-member-object
"""
from typing import Any, List, Optional, Union

from .user import User

__all__: List[str] = ["Member"]


class Member:
    """Represents a Discord Guild Member

    .. versionadded:: 0.7.0

    Parameters
    ----------
    data
        The member data, a :class:`dict`
    factory
        The current instance of :class:`RESTFactory`

    Attributes
    ----------
    from_dict
        The raw :class:`dict` object of the Member.
    """

    def __init__(self, data: dict, guild: Union[int, Any], factory):
        self.from_dict = data
        self.guild_id = guild
        self._factory = factory

    @property
    def user(self):
        """Returns the members :class:`User` object

        Returns
        -------
        :class:`User`
        """
        return User(self.from_dict["user"])

    def nick(self) -> str:
        """Returns the members nick name, if any

        Returns
        -------
        :class:`str`
        :class:`None`
        """
        return self.from_dict["nick"]

    def avatar(self) -> str:
        raise NotImplementedError

    def roles(self):
        raise NotImplementedError

    def joined_at(self) -> str:
        """Gives a timestamp of when the member joined the server

        Returns
        -------
        :class:`str`
        """
        return self.from_dict["joined_at"]

    def premium_since(self) -> str:
        """Gives a timestamp of when the member started boosting

        Returns
        -------
        :class:`str`
        :class:`None`
        """
        return self.from_dict["premium_since"]

    def deaf(self) -> bool:
        """Returns a bool if the member is deaf in a voice channel or not.

        Returns
        -------
        :class:`bool`
        """
        return self.from_dict["deaf"]

    def mute(self) -> bool:
        """Returns if the member it muted from a channel

        Returns
        -------
        :class:`bool`
        """
        return self.from_dict["mute"]

    def pending(self) -> bool:
        """Returns if the user is pending verification or not

        Returns
        -------
        :class:`bool`
        """
        return self.from_dict["pending"]

    def permissions(self) -> dict[str, Any]:
        """Returns a dict of the users permissions

        Returns
        -------
        :class:`dict`
        """
        return self.from_dict["permissions"]

    def communication_disabled_until(self):
        """Returns a `communication_disabled_until` dict object

        Returns
        -------
        :class:`dict`
        """
        return self.from_dict["communication_disabled_until"]

    def edit(
        self,
        nick: Optional[str] = None,
        roles: Optional[List[int]] = None,
        mute: Optional[bool] = False,
        deaf: Optional[bool] = False,
        channel_id: Optional[int] = None,
        timeout: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> None:
        """Edits the member

        Parameters
        ----------
        nick: :class:`Optional`[:class:`str`]
            Change the members nickname
        roles: :class:`Optional`[:class:`list`[:class:`int`]]
            Chaneg the members roles
        mute: :class:`Optional`[:class:`bool`]
            If the member should be muted
        deaf: :class:`Optional`[:class:`bool`]
            If the member should be deafend
        channel_id: :class:`Optional`[:class:`int`]
            The channel id to move the member to
        timeout: :class:`Optional`[:class:`str`]
            Set a timeout for the member,
            has to be a ISO8601 timestanp
        reason: :class:`Optional`[:class:`str`]
            A reason why you are editing this member

        Returns
        -------
        :class:`None`
        :class:`Forbidden`
        """
        return self._factory.modify_guild_member(
            guild_id=self.guild_id,
            member=self.user.id,
            nick=nick,
            roles=roles,
            mute=mute,
            deaf=deaf,
            channel_id=channel_id,
            timeout=timeout,
            reason=reason,
        )
