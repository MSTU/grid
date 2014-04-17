import tempfile
from contextlib import contextmanager
import os
import shutil
import subprocess

from smb.SMBConnection import SMBConnection
from nmb.NetBIOS import NetBIOS

from conf import ConfigHost


def getBIOSName(remote_smb_ip, timeout=30):
	try:
		bios = NetBIOS()
		srv_name = bios.queryIPForName(remote_smb_ip, timeout=timeout)
	except:
		print >> sys.stderr, "Looking up timeout, check remote_smb_ip again!!"
	finally:
		bios.close()
		return srv_name


def getBIOSIp(remote_smb_name, timeout=30):
	try:
		bios = NetBIOS()
		server_ip_list = bios.queryName(remote_smb_name, timeout=timeout)
	except:
		print >> sys.stderr, "Looking up timeout, check remote_smb_name again!!"
	finally:
		bios.close()
		return server_ip_list


@contextmanager
def mounted(remote_dir, local_dir):
	local_dir = os.path.abspath(local_dir)
	retcode = subprocess.call(["/sbin/mount", "-t", "smbfs", remote_dir, local_dir])
	if retcode != 0:
		raise OSError("mount operation failed")
	try:
		yield
	finally:
		retcode = subprocess.call(["/sbin/umount", local_dir])
		if retcode != 0:
			raise OSError("umount operation failed")


def path_leaf(path):
	"""
	Get filename from filepath for Windows or Linux.
	"""
	import ntpath
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

def copy_file_from(server_name, file_path):
	# set connection with smb server
	conn = SMBConnection(ConfigHost.USERNAME, ConfigHost.PASSWORD, ConfigHost.CLIENT_NAME, server_name)
	conn.connect(getBIOSIp(server_name)[0])

	#with mounted(remote_dir, local_dir):
	#	shutil.copy(file_to_be_copied, local_dir)

	try:
		filename = path_leaf(file_path)
		print filename
		#data_file = open(filename, 'w')
		data_file = tempfile.NamedTemporaryFile()

		attr, size = conn.retrieveFile(ConfigHost.SHARE_DIR, file_path, data_file)
		print size
		data_file.close()
	except Exception as e:
		print e.message
