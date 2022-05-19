import os
import subprocess


class GoToPython:
    def __init__(self, command):
        splited_command = command.split()
        exec_path = self.__module_exec_path(splited_command[0])  # Send Module name to module_exec_path
        self.command = exec_path + " ".join(splited_command[1:]) # Create valid format of command
    

    def run(self):
        return subprocess.run(self.command, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
        

    def __get_go_path(self):
        if os.environ.get('GOPATH'):
            return os.environ['GOPATH'] + "/bin/"  #GOPATH
        else:
            exit("GOPATH not found")


    def __module_exec_path(self, module_name):
        module_path = self.__get_go_path() + module_name
        if os.path.exists(module_path):
            return module_path + " "
        else:
            exit(f'Module \"{module_name}\" not found in GO installed modules (\"{module_path}\")')