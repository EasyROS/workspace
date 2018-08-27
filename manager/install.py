import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def clone(service, dir='src/sycu', remote='https://github.com/'):
    os.system('cd ' + dir + ' && git clone ' + remote + service + '.git')


def run():
    logging.info('Install')
    logging.warning('It will be clean and install, please make sure it is safe ?')
    safe = raw_input('(y/n)')
    print(safe)
    if safe == 'y':
        os.system('rm -rf src')
        os.system('mkdir src')
        os.system('mkdir src/sycu')

        clone('EasyROS/ROServer')
        clone('EasyROS/shellservice')
        clone('EasyROS/webservice')


def exe(arg):
    logging.info('Install')
    os.system('echo ' + arg)
