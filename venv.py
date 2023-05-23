import subprocess, sys
cmd = ["virtualenv", "--python", "python2"] + sys.argv[1:]
subprocess.call(cmd)
