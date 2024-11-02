import paramiko


hostname = 'ip_address'
username = 'username'
key_filepath = '<ssh-key_path>'

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