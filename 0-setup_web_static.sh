!#/usr/bin/env python3
"""a Bash script that sets up your web servers for the deployment of web_static"""
from fabric.api import *
from datetime import datetime
import os
def do_pack():

	local("sudo mkdir -p versions")
	t = datetime.now()
	t_str = t.strftime('%Y%m%d%H%M%S')

	local(f'sudo tar -cvzf versions/web_static_{t_str}.tgz web_static')

	f_path = f"versions/web_static_{t_str}.tgz"
	f_size = os.path.getsize(f_path)
	if f_path = True
		print(f'web_static packed: {f_path} -> {f_size)Bytes')
	else:
		return f_path

