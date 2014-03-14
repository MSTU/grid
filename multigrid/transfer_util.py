from ftplib import FTP
import os
from conf import config


def need_transfer(filename):
	return not os.path.exists(filename)

def do_file_transfer(address, directory, filename):
	cur_dir = os.getcwd()
	if not os.path.exists(directory):
		os.makedirs(directory)
	os.chdir(directory)

	ftp = FTP()

	if need_transfer(filename):
		ftp.connect(address, config.FTP_PORT)
		ftp.login(config.FTP_LOGIN, config.FTP_PASSWORD)

		localfile = open(filename, 'w+')
		ftp.retrbinary('RETR ' + filename, localfile.write)

		#TODO need error handling
		localfile.close()
		ftp.quit()

	# change to parent directory
	os.chdir(cur_dir)