from ftplib import FTP


def download_file(ftp_obj, directory=None, file=None):
    if directory != ftp_obj.pwd():
        ftp_obj.cwd(directory)
    with open(file, 'wb') as fd:
        ftp_obj.retrbinary(f'RETR {file}', fd.write)


def download_files(ftp_obj, directory=None):
    if directory != ftp_obj.pwd():
        ftp_obj.cwd(directory)
    files = ftp_obj.nlst()
    for file in files:
        with open(file, 'wb') as fd:
            ftp_obj.retrbinary('RETR ' + file, fd.write)


def upload_file(ftp_obj, directory=None, path=None):
    if directory != ftp_obj.pwd():
        ftp_obj.cwd(directory)

    with open(path, 'rb') as fd:
        ftp_obj.storbinary('STOR ' + path, fd, 1024)


if __name__ == '__main__':
    with FTP('192.168.0.107') as ftp:
        auth = ftp.login(user='ftpuser', passwd='ftpuser')
        print(auth)

        # List directory content 01_ftp.dir()
        print(ftp.retrlines('LIST'))

        # Change working directory
        ftp.cwd('..')
        print(ftp.retrlines('LIST'))

        # Download one file
        download_file(ftp, directory='/home/ftpuser', file='01_ftp.txt')

        # Download several files
        download_files(ftp, directory='/home/ftpuser')

        # Upload file
        upload_file(ftp, directory='/home/ftpuser', path='config.yml')
