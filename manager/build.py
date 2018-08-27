import os


def run(arg):
    print 'Build'
    os.system('echo ' + arg)


def exe(arg1, arg2):
    print 'Build'
    os.system('echo ' + arg1 + ' ' + arg2)
