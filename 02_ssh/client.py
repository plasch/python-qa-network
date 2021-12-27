import paramiko
import os


HOST = "192.168.0.107"
# Add 02_ssh key of client to authorized_keys

with paramiko.SSHClient() as client:
    # Load host key from ~/.02_ssh/known_hosts
    # client.load_host_keys(filename=os.path.expanduser("~/.02_ssh/known_hosts"))

    # Add missing host key to the local HostKeys object
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Login using password
    client.connect(HOST, username="agr",
                   password=f'{os.getenv("SSH_PASSWD")}', port=22)

    # Login using public key
    client.connect(HOST, username="agr", port=22)

    stdin, stdout, stderr = client.exec_command("ls -la")
    # stdin, stdout, stderr = client.exec_command("touch file.py")
    print(stdout.read().decode("utf-8"))

    # Interactive shell example
    # 02_ssh = client.invoke_shell()
    # 02_ssh.send("ip address\n")
    # print(02_ssh.recv(3000).decode("utf-8"))

    # sftp = client.open_sftp()

    # Download via 02_ssh
    # sftp.get("/home/agr/02_ssh.txt", "02_ssh.txt")

    # Upload via 02_ssh
    # sftp.put("config.yml", "/home/agr/config.yml")
