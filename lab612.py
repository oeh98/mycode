#serparate file, import into usopen 

from netmiko import ConnectHandler

 def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):


     try:
         config_file= open(config, "r")

         config_file.read()
