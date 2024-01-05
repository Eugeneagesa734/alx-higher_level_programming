#!/usr/bin/bash
"""A locked class is defined."""


class LockedClass:
    """
    user is prevented from initializing new locked class attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
