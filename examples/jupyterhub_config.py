# Sample ConfigurationS
c.JupyterHub.spawner_class = "cloudsshspawner.cloudsshspawner.CloudSSHSpawner"

# The remote host to spawn notebooks on
c.CloudSSHSpawner.remote_hosts = ["cori19-224.nersc.gov"]
c.CloudSSHSpawner.remote_port = "2222"
c.CloudSSHSpawner.ssh_command = "ssh"

# The system path for the remote SSH session. Must have the jupyter-singleuser and python executables
c.CloudSSHSpawner.path = "/global/common/cori/software/python/3.5-anaconda/bin:/global/common/cori/das/jupyterhub/:/usr/common/usg/bin:/usr/bin:/bin:/usr/bin/X11:/usr/games:/usr/lib/mit/bin:/usr/lib/mit/sbin"

# The command to return an unused port on the target system. See scripts/get_port.py for an example
c.CloudSSHSpawner.remote_port_command = (
    "/usr/bin/python /global/common/cori/das/jupyterhub/get_port.py"
)
