import paramiko
import time

hostname = 'ip_address'
username = 'username'
key_filepath = '<ssh-key_path>'

try: 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #trust local with remote

    ssh.connect(hostname=hostname, username=username, key_filename=key_filepath)
    print("connected with Server")

    stdin, stdout, stderr  = ssh.exec_command('free -m')
    time.sleep(5)
    print("Memory usage information: ")
    print("".join(stdout))

except  paramiko.AuthenticationException:
    print("Authentication failure.")

except paramiko.SSHException as e:
    print(f"Exception occured ",{e})

finally:
    ssh.close()
    print("SSH connection closed")
