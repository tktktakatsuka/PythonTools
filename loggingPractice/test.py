import logging
import logging.config

logging.config.fileConfig('logging.conf' , encoding='UTF-8')

# create logger
logger = logging.getLogger('root')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')