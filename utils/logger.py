import logging


class Logger(object):
    def __init__(self, name='logger', level=logging.DEBUG):
        FORMATTER = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        fh = logging.FileHandler('%s.log' % name, 'w')
        fh.setFormatter(FORMATTER)
        self.logger.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setFormatter(FORMATTER)
        self.logger.addHandler(sh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg,stack_info=True)


logger = Logger()
