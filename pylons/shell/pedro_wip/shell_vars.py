
import memcache


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Max number of servers to look
MAX_MPSERVER_ADDRESS = 20

MC = memcache.Client(['127.0.0.1:11211'])

