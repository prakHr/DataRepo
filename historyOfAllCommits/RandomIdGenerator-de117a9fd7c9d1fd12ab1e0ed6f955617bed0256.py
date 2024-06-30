import random
import six

_AUTO_ID_CHARS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
def _auto_id():
    return ''.join(random.choice(_AUTO_ID_CHARS) for _ in six.moves.xrange(20))

print(_auto_id())

