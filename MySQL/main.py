# from pymysqlreplication           import BinLogStreamReader
# from pymysqlreplication.event     import QueryEvent
from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent

mysql_settings = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "root",
    "passwd": "warlock"
}

stream = BinLogStreamReader(
    connection_settings = mysql_settings,
    server_id = 1,
    blocking = True,
    only_schemas=['warlock'],
    only_events=[DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent],
    resume_stream=True,
)


for event in stream:
    print(event)
    print(event.dump())

stream.close()
