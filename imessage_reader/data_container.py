#!/usr/bin/env python3

"""
Data Container
Python 3.9+
Author: niftycode
Modified by: figbert
Date created: February 19th, 2022
Date modified: November 21, 2024
"""

from typing import override
from dataclasses import dataclass


@dataclass
class MessageData:
    """This dataclass is the store for the data:
    user id, text, date, service and account (caller id).
    """

    user_id: str
    text: str
    date: str
    service: str
    account: str
    is_from_me: int
    is_read: int

    @override
    def __str__(self) -> str:
        """String representation

        :return: the representation of this object
        """
        return (
            f"user id:\t\t{self.user_id}\n"
            f"date and time:\t\t{self.date}\n"
            f"service:\t\t{self.service}\n"
            f"caller id:\t\t{self.account}\n"
            f"is_from_me:\t\t{self.is_from_me}\n"
            f"is_read:\t\t{self.is_read}\n"
            f"\n"
            f"text:\n"
            f"=====\n"
            f"{self.text}\n"
            f"\n"
            f"----------------------------------------------------------------\n"
        )
