import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def clone(service, dir, remote='https://github.com/'):
    os.system('cd src/' + dir + ' && git clone ' + remote + service + '.git')


def run():
    logging.info('Install')
    logging.warning('It will be clean and install, please make sure it is safe ?')
    safe = raw_input('( install / clean / other type is cancel )')

    if safe == 'install' or safe == 'clean':
        if safe == 'clean':
            os.system('rm -rf src')
        os.system('mkdir src')
        os.system('mkdir src/default')

        clone('ros/catkin', ' ')
        clone('EasyROS/ROServer', 'default')
        clone('EasyROS/shellservice', 'default')
        clone('EasyROS/webservice', 'default')
        clone('EasyROS/env_public', 'default')


def exe(arg):
    logging.info('Install')
    os.system('echo ' + arg)
