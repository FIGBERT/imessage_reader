#!/usr/bin/env python3

"""
Fetch data, print data, show recipients or export data.
Python 3.9+
Author: niftycode
Modified by: thecircleisround
Date created: October 8th, 2020
Date modified: June 27th, 2023
"""

import sys
import logging

from imessage_reader import common, data_container


# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)


# noinspection PyMethodMayBeStatic
class FetchData:
    """
    This class contains the methods to fetch,
    print and export the messages.
    """

    db_path: str
    operating_system: str

    # The SQL command
    SQL_CMD: str = (
        "SELECT "
        "text, "
        "datetime((date / 1000000000) + 978307200, 'unixepoch', 'localtime'),"
        "handle.id, "
        "handle.service, "
        "message.destination_caller_id, "
        "message.is_from_me, "
        "message.is_read, "
        "message.attributedBody, "
        "message.cache_has_attachments "
        "FROM message "
        "JOIN handle on message.handle_id=handle.ROWID"
    )

    def __init__(self, db_path: str, system: str | None = None):
        """Constructor method

        :param db_path: Path to the chat.db file
        :param system: Operating System
        """
        self.db_path = db_path
        if system is None:
            self.operating_system = common.get_platform()

    def _check_system(self):
        if self.operating_system == "WINDOWS":
            sys.exit("Your operating system is not supported yet!")

    def _read_database(self) -> list:
        """Fetch data from the database and store the data in a list.

        :return: list containing the user id, messages, the service and the account
        """

        rval = common.fetch_db_data(self.db_path, self.SQL_CMD)

        data = []
        for row in rval:
            text = row[0]
            if row[7] == 1:
                text = "<Message with no text, but an attachment.>"
            # the chat.db has some weird behavior where sometimes the text value is None
            # and the text string is buried in a binary blob under the attributedBody field.
            if text is None and row[6] is not None:
                try:
                    text = row[6].split(b"NSString")[1]
                    text = text[
                        5:
                    ]  # stripping some preamble which generally looks like this: b'\x01\x94\x84\x01+'

                    # this 129 is b'\x81, python indexes byte strings as ints,
                    # this is equivalent to text[0:1] == b'\x81'
                    if text[0] == 129:
                        length = int.from_bytes(text[1:3], "little")
                        text = text[3 : length + 3]
                    else:
                        length = text[0]
                        text = text[1 : length + 1]
                    text = text.decode()

                    logging.debug(text)

                except Exception as e:
                    print(e)
                    sys.exit("ERROR: Can't read a message.")

            data.append(
                data_container.MessageData(row[2], text, row[1], row[3], row[4], row[5])
            )

        return data

    def get_messages(self) -> list:
        """Create a list with tuples (user id, message, date, service, account, is_from_me)
        (This method is for module usage.)

        :return: list with tuples (user id, message, date, service, account, is_from_me)
        """
        fetched_data = self._read_database()

        users = []
        messages = []
        dates = []
        service = []
        account = []
        is_from_me = []
        is_read = []

        for data in fetched_data:
            users.append(data.user_id)
            messages.append(data.text)
            dates.append(data.date)
            service.append(data.service)
            account.append(data.account)
            is_from_me.append(data.is_from_me)
            is_read.append(data.is_read)

        data = list(zip(users, messages, dates, service, account, is_from_me, is_read))

        return data
