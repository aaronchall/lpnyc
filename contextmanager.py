import logging
import sys

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.level = logging.WARNING
# logger.level = logging.INFO # set to see info
# logger.level = logging.DEBUG # set to see info and debug

class ContextBase(object):
    def __enter__(self):
        logger.info('we have entered the context manager')

    def __exit__(self, exception_type, exception, traceback):
        logger.info('in exit, exception type, value, and traceback logged below')
        logger.debug(repr(exception_type))
        logger.debug(repr(exception))
        logger.debug(repr(traceback))

class ContextPassesFails(ContextBase):
      
    def __exit__(self, *args):
        super(ContextPassesFails, self).__exit__(*args)
        return False

class ContextSuppressFails(ContextBase):
      
    def __exit__(self, *args):
        super(ContextSuppressFails, self).__exit__(*args)
        return True

