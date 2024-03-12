#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static
import 
import getpass
from fabric import *
from fabric import connection, config

# password = getpass.getpass("Enter your password: ")

config = Config(overrides={'sudo': {'password' : putty}})
conn = Connection("52.3.220.80", user="ubuntu", config=config)

conn.run("sudo mkdir -p data")
conn.run("cd data")
conn.run("sudo mkdir -p web_static")
conn.run("cd web_static")
conn.run("sudo mkdir -p releases")
conn.run("cd web_static")
conn.run("sudo mkdir -p shared")
conn.run("cd web_static")
conn.run("cd releases")
conn.run("sudo mkdir -p test")
conn.run("cd test")
conn.run("echo <h1>my enginx</h1> > index.html)



