import logging

logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p', level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


