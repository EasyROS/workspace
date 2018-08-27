import os


def run(arg):
    print 'Test'
    os.system('echo ' + arg)


def exe(arg1, arg2):
    print 'Test'
    os.system('echo ' + arg1 + ' ' + arg2)
