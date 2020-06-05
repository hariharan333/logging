import logging


class createlog(object):
    def __init__(self):
        self.count = 0

        #create logger
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        #create handler for logfile
        loger_handler = logging.FileHandler('data.log')

        #create formatter for formatting the log file
        loger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #add the formatter to handler
        loger_handler.setFormatter(loger_formatter)

        #add the handler to logger
        self.logger.addHandler(loger_handler)
        self.logger.info("this is complete")

    def increment(self):
        self.count+=1
        self.logger.warning("increate count")
        self.logger.info("still increate count")

    def decrement(self):
        self.count-=1

    def close(self):
        self.count = 0
        self.logger.warning("close count")
        self.logger.info("still close count")

log = createlog()
log.increment()
log.increment()
print("current count no: %s" % str(log.count))
log.decrement()
log.close()
print("current count no: %s"% str(log.count))
