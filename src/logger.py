import logging

'''
    Following are 5 major logging levels

    1. DEBUG     -  detailed info, used typically incase of diagnosing problems.
    2. INFO      -  confirmation that things are working as expected.
    3. WARNING   -  an indication that something unexpected happened, or something in near future may go wrong.
                    software is still working as expected. (default level)
    4. ERROR     -  due to some serious problem, software has not been able to perfom some function. (exception)
    5. CRITICAL  -  some serious error, software itself may not be able to continue running.

'''

class ColorFormatter(logging.Formatter):
    colors = {
        'info': dict(fg='green'),
        'debug': dict(fg='blue'),
        'warning': dict(fg='yellow'),
        'error': dict(fg='red'),
        'critical': dict(fg='red'),
    }

    def format(self, record):
        import click
        s = super(ColorFormatter, self).format(record)
        if not record.exc_info:
            level = record.levelname.lower()
            if level in self.colors:
                s = click.style(s, **self.colors[level])
        return s


class CustomFormatter(logging.Formatter):
    def format(self, record):
        s = super(CustomFormatter, self).format(record)
        if record.levelno == logging.ERROR:
            s = s.replace('[.]', '[x]')
        return s
        

def setup(name=__name__, level=logging.INFO):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    if logger.handlers:
        return logger
    
    try:
        import click
        formatter = ColorFormatter('[.]%(message)s')
    except ImportError as error:
        formatter = CustomFormatter('[.]%(message)s')

    handler = logging.StreamHandler()
    # handler = logging.FileHandler('log.txt')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
    