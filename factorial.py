# import logging
# logging.basicConfig(level=logging.DEBUG, format= ' %(asctime)s - %(levelname)s - %(message)s')
# 
# logging.debug('Start of program')
# 
# def factorial(num):
#     logging.debug('Start of factorial(' + str(num) + ')')
#     total = 1
#     for i in range(1, num + 1):
#         total = total * i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total) + '.')
#     logging.debug('End of factorial(' + str(num) + ')')
#     print(total)
#     
# print(factorial(3))
# logging.debug('End of program')

# import logging
# logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
# 
# logging.debug('This is a basic debugging message containing small details used to diagnose problems.')
# logging.info('This is general information about what the program is currently doing or has done. Used to confirm its working.')
# logging.warning('WARNING! There''s a potential issue with the code. It is still working but might not continue to do so in the future.')
# logging.error('Error! Error! Something happened and the program failed to do something')
# logging.critical('Critical error! Critical error! Program has crashed or is about to!')

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
