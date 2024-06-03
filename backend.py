import subprocess
import os

# initialize pyinstaller to build python executable

def build_executable(script_path=False, onefile=True, windowed=True, icon=False, output_name=False):
    # Navigate to the directory containing the script
    script_path = os.path.abspath(script_path)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)

    instructions = ['pyinstaller']

    if onefile:
        instructions.append('--onefile')
    if windowed:
        instructions.append('--windowed')
    else:
        instructions.append('--console')
    if icon:
        instructions.append(f'--icon={icon}')
    if output_name:
        instructions.append(f'--name={output_name}')
    
    instructions.append(os.path.basename(script_path))
    
    # Run PyInstaller command
    subprocess.call(instructions)
    