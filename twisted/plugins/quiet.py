from zope.interface import implementer
from twisted.logger import ILogObserver, LogLevel, formatEvent

@implementer(ILogObserver)
class ErrorObserver(object):
    def __call__(self, event):
        if event['log_level'] == LogLevel.error:
            print(formatEvent(event))