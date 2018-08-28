import os


def run():
    print 'Build'
    os.system('catkin build --force-color --profile release')


def exe(arg):
    print 'Build'
    os.system('echo ' + arg)
