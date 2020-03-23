import getpass
import paramiko


def login(hostname, username, password, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname, port, username, password)
    return ssh


if __name__ == '__main__':
    hostname = "10.172.161.10"
    username = r"ls\0qianmaye"
    password = getpass.getpass()
    ssh = login(hostname, username, password)
    stdin, stdout, stderr = ssh.exec_command("show run")
    for line in stdout.readlines():
        print(line)
