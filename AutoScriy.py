import subprocess

def runCMD(Command):
    '''
    Command: stdin command

    This function is for System Autoamtion.
    Input System Command and return object
    '''
    result = subprocess.run(Command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
    print(f'success:{Command}' if result.returncode == 0 else f'error:{Command}' )
    return(result)

