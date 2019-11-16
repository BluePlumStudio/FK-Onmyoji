import sys
import time
import winsound
import inspect
import ctypes

def _asyncRaise(threadId, exctype):
    threadId = ctypes.c_long(threadId)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(threadId, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(threadId, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stopThread(thread):
    if thread.isAlive():
        _asyncRaise(thread.ident, SystemExit)

def getTimeFormatted():
    return time.strftime("[%Y-%m-%d %H:%M:%S]",time.localtime())

def printWithTime(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    print(getTimeFormatted()+":", sep=' ', end='')
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

def inputWithTimePrompt(prompt):
    return input(getTimeFormatted()+":"+prompt)