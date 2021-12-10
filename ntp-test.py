import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('europe.pool.ntp.org', version=3)
response.offset
response.version
ctime(response.tx_time)
ntplib.leap_to_text(response.leap)
ntplib.ref_id_to_text(response.ref_id)
