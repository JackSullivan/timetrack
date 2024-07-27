from time import sleep
from datetime import datetime, timedelta, timezone

from aw_core.models import Event
from aw_client import ActivityWatchClient

client = ActivityWatchClient("test-client", testing=True)


now = datetime.now(timezone.utc)

start = now

query = "RETURN=0;"

res = client.query(query, "1970-01-01" "2100-01-01")

print(res)
