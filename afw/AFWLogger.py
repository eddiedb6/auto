import logging

__prefix = "[AFW] "

def Debug(log):
    logging.debug(__prefix + log)

def Info(log):
    logging.info(__prefix + log)

def warning(log):
    logging.warning(__prefix + log)

def Error(log):
    logging.error(__prefix + log)

def Critical(log):
    logging.critical(__prefix + log)
