import subprocess
import os

# initialize pyinstaller to build python executable

def build_executable(script_name=False, onefile=True, windowed=True, icon=False):
    # Navigate to the directory containing the script
    script_path = os.path.abspath(script_name)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)

    instructions = ['pyinstaller']

    if script_name:
        instructions.append(f'--name {script_name}')
    if onefile:
        instructions.append('--onefile')
    if windowed:
        instructions.append('--windowed')
    else:
        instructions.append('--console')
    if icon:
        instructions.append(f'--icon={icon}')
    
    # Run PyInstaller command
    subprocess.call(instructions)
    