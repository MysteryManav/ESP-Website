import httplib
from sys import stdout, stderr

from esp.tagdict.decorators import require_tag
from esp.tagdict.models import Tag

#@require_tag('varnish_purge')
def purge_page(url, host = None):
    if Tag.getTag('varnish_purge', default='false') == 'false':
        return None

    print "purge_page called"
    if host == None:
        try:
            from esp.settings import VARNISH_HOST, VARNISH_PORT
            host = VARNISH_HOST + ":" + str(VARNISH_PORT)
        except ImportError:
            stderr.write("No proxy cache!\n")
            return False

    stdout.write("Purging: " + str(url) + "\n")
    stdout.write("Host: " + host + "\n")
    conn = httplib.HTTPConnection(host)
    conn.request("PURGE", url)
    ret = conn.getresponse()
    return (ret.status, ret.reason)
