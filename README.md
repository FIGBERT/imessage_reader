# imessage_reader

A Python library to fetch content from the iMessage database on macOS
10.14 and above.

The following information is currently being read from the database:

* Sender (phone number or email address)
* Message
* Date and time
* Service (iMessage or SMS)
* Account (destination caller ID)
* `is_from_me`
* `is_read`

## Background

Received messages (iMessage or SMS) and attachments will be saved in
`~/Library/Messages`. This directory contains a `chat.db` file (SQLite3)
with two tables of interest: `handle` and `message`. The `handle` table
contains the recipients (email address or phone number). The received
messages are in the `message` table.

## Usage

The following simplistic example shows the library in use to fetch
messages:

```python3
from imessage_reader import fetch_data

DB_PATH = /home/bodo/Downloads/chat.db

# Create a FetchData instance
fd = fetch_data.FetchData(DB_PATH)

# Store messages in my_data
my_data = fd.get_messages()
print(my_data)
```

## Note

Of course, the `chat.db` file is only created under macOS. Nevertheless,
this program can also be used under Linux. In contrast to use under
macOS, the path to the `chat.db` file must then be specified (see
below).

On macOS you need access to the `~/Library` folder in order to read the
iMessage database file. You can grant access for your terminal in:

```
> System Preferences > Security & Privacy > Privacy > Full Disk Access
```
