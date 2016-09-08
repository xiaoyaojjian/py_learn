import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', 2206, 'root', 'root')
stdin, stdout, stderr = ssh.exec_command('df -h')
print(stdout.read())
ssh.close()