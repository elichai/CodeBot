import docker
client = docker.from_env()
#result = client.containers.run("continuumio/anaconda3", "echo hello world")
code = "print('running code')"
loop = "for i in range(0,10):\n\tprint('hello')"
loop2 = "for i in range(0,10):print('my name is {}'.format(i));"
cmd = 'python -c """{0}"""'
result = client.containers.run("continuumio/anaconda3", cmd.format(loop2), True,True)
print(result)