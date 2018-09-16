import docker

class Executor(object):
    
    def __init__(self,container_name):
    
        self.client = docker.from_env()
        self.container_name = container_name

    def validate_code(self,code):
    
        return True 

    def execute(self,code):
        cmd = 'python -c """{0}"""'
        try:
            result = self.client.containers.run(self.container_name, cmd.format(code), True,True)
            return result
        except Exception as e:
            return self.format_error(e)

    def format_bytes(self,unformatted_result):
        return unformatted_result

    def format_error(self,unformatted_err):
            output = str(unformatted_err)[-140:]
        
#loop2 = "for i in range(0,10):print('my name is {}'.format(i));"
def example(code):
    executor = Executor("continuumio/anaconda3")
    result = executor.execute(code)
    pretty_result = executor.format_bytes(result)
    print(pretty_result)


if __name__ == '__main__':
    loop = "for i in range(0,10):print('my name is {}'.format(i));"
    bad_code = "for i in range(0,10):prinsdt('my name is {}'.format(i));"
    example(loop)
