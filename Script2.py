# Specify the file name and open it in write mode
import subprocess
file_name = "git.py"
base_branch = input('Enter the base branch name: ')
your_branch = input('Enter your branch: ')
with open(file_name, "w") as file:
    # Write something to the file
    file.write(f'import subprocess \ngit_command1 = "git checkout {base_branch}" \ngit_command2 = "git branch {your_branch}" \ngit_command3 = "git checkout {your_branch}" \ntry: \n    result = subprocess.check_output(git_command1, shell=True, stderr=subprocess.STDOUT, universal_newlines=True) \n    result2 = subprocess.check_output(git_command2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True) \n    result3 = subprocess.check_output(git_command3, shell=True, stderr=subprocess.STDOUT, universal_newlines=True) \nexcept subprocess.CalledProcessError as e:\n'+r'    print(f"Error executing Git command: {e.returncode}\n{e.output}") ')
   
command = ["python", "git.py"]
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(result)
# File is automatically closed when exiting the "with" block
