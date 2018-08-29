import os


def run(arg):
    print 'Build'
    os.system('catkin clean --yes --profile release')


def exe(arg):
    print 'Build'
    os.system('catkin build --yes --profile release ' + arg)
