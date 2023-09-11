import subprocess 
git_command1 = "git checkout main" 
git_command2 = "git branch develop" 
git_command3 = "git checkout develop" 
try: 
    result = subprocess.check_output(git_command1, shell=True, stderr=subprocess.STDOUT, universal_newlines=True) 
    result2 = subprocess.check_output(git_command2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True) 
    result3 = subprocess.check_output(git_command3, shell=True, stderr=subprocess.STDOUT, universal_newlines=True) 
except subprocess.CalledProcessError as e:
    print(f"Error executing Git command: {e.returncode}\n{e.output}") 