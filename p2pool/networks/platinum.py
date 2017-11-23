from p2pool.bitcoin import networks

PARENT = networks.nets['platinum']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'b5fafab5fab5dfdb'.decode('hex')
PREFIX = 'd5fddffab5dfdbfd'.decode('hex')
P2P_PORT = 29926
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8926
BOOTSTRAP_ADDRS = 'platinumcrypto.com'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt '
VERSION_CHECK = lambda v: True
