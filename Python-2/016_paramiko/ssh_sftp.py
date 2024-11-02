import paramiko


hostname = '13.235.23.207'
username = 'ubuntu'
key_filepath = '/home/nitesh/Documents/Documents_personal/ansible/vault/aws-ansible.pem'

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=hostname, username=username, key_filename=key_filepath)
    print("Connected with server")

    try:
        # upload file to remote server
        # ftp_client = ssh.open_sftp()
        # ftp_client.put('ssh_connect.py','ssh_connect.py')
        # print("file uploaded")
        # ftp_client.close()

        # Download file from remote server
        ftp_client = ssh.open_sftp()
        ftp_client.get('ssh_connect_remote.py','ssh_connect_remote.py')
        print("File downloaded")
        ftp_client.close()

    except Exception as e:
        print(f"Failed FTP ",{e})

except paramiko.AuthenticationException:
    print("Authentication failure")

finally:
    ssh.close()