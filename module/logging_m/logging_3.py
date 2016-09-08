import logging

'''
logging_m.basicConfig(filename='3a.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging_m.DEBUG)
logging_m.info('test info')
logging_m.debug('deeeee')
'''
# create shii object
shii = logging.getLogger('shiina')
shii.setLevel(logging.INFO)

# create file handler and set level to waring
shii_fh = logging.FileHandler('shii_fh.log')
shii_fh.setLevel(logging.WARNING)

# create console handler and set level to debug
shii_sh = logging.StreamHandler()
shii_sh.setLevel(logging.DEBUG)

# create formatter to shii_fh and shii_sh
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to shii_fh and shii_sh
shii_fh.setFormatter(formatter)
shii_sh.setFormatter(formatter)

# add shii_fh and shii_sh to shii
shii.addHandler(shii_fh)
shii.addHandler(shii_sh)

shii.debug('debug message')
shii.info('info message')
shii.warning('warning message')
shii.error('error message')
shii.critical('critical message')