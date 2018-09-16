import docker
import re
from threading import Timer
from threading import Thread

def run_stopper(container,timeout):
    r = Timer(timeout, kill_container, (container,))
    r.start()

def kill_container(container):
    container.stop()

class Executor(object):
    
    def __init__(self,container_name):
    
        self.client = docker.from_env()
        self.container_name = container_name
        self.TIMEOUT = 10

    def sanitize_code(self,code):
        return code 

    def execute(self,code,timeout = None):
        
        code = self.sanitize_code(code)
        
        if code is None:
            return None

        cmd = 'python -c """{0}"""'

        container = None

        try:

            container = self.client.containers.run(self.container_name, 
                command = cmd.format(code), 
                stdout = True,
                stderr =True,
                pids_limit = 15,
                privileged = False,
                tty = True,
                detach = True)

            full_output = ''
            
            if timeout is not None and timeout is True:
                thread = Thread(target = run_stopper, args = (container,self.TIMEOUT,))
                thread.start()

            for line in container.logs(stream=True):
                full_output +=line.decode('utf8')
            return re.escape(full_output)

        except Exception as e:

            if container is not None:
                container.stop()
            return self.format_error(e)

    def execute_async(self,code,callback,timeout = None):
        pass
        
    def format_error(self,unformatted_err):
        return str(unformatted_err)[-140:].decode("utf-8") 
    

#loop2 = "for i in range(0,10):print('my name is {}'.format(i));"
def example(code):
    executor = Executor("continuumio/anaconda3")
    result = executor.execute(code,timeout = True)
    print(result)

    
if __name__ == '__main__':
    loop = "for i in range(0,10):print('my name is {}'.format(i));print('...');"
    bad_code = "for i in range(0,10):prinsdt('my name is {}'.format(i));"
    sleep_ = "import time;print('Start : %s' % time.ctime());time.sleep(3);print('End : %s' % time.ctime());"
    example(loop)
