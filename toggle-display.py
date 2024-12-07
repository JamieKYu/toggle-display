# BUILD command: pyinstaller --onefile --noconsole toggle-display.py

import os
import subprocess

# The string to check in the command output
IS_MIRRORED_STRING = "CE290F63-3CCF-429B-8F17-F13EAC9DC49C+37D8832A-2D66-02CA-B9F7-8F30A301B230"
DISPLAY_EXTEND_COMMAND_STRING = (
    'displayplacer "id:37D8832A-2D66-02CA-B9F7-8F30A301B230 res:1512x982 hz:120 color_depth:8 enabled:true scaling:on origin:(0,0) degree:0" "id:CE290F63-3CCF-429B-8F17-F13EAC9DC49C res:2560x1440 hz:120 color_depth:8 enabled:true scaling:on origin:(-230,-1440) degree:0"'
)
DISPLAY_MIRROR_COMMAND_STRING = (
    'displayplacer "id:CE290F63-3CCF-429B-8F17-F13EAC9DC49C+37D8832A-2D66-02CA-B9F7-8F30A301B230 res:1920x1080 hz:144 color_depth:8 enabled:true scaling:on origin:(0,0) degree:0"'
)

try:
    # Run the 'displayplacer list' command and capture its output
    result = subprocess.run(
        ["displayplacer", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Check if the string is in the output
    if IS_MIRRORED_STRING in result.stdout:
        print("Stop mirroring...")
        command = DISPLAY_EXTEND_COMMAND_STRING
    else:
        print("Mirroring display...")
        command = DISPLAY_MIRROR_COMMAND_STRING

    result = subprocess.run(
        command,
        shell=True,  # Use shell=True to allow the string command to run in the shell
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Ensure output is a string
    )

    # Print the command's standard output and standard error
    if result.returncode == 0:
        print("Command executed successfully:")
        print(result.stdout)
    else:
        print("Error while executing the command:")
        print(result.stderr)

except FileNotFoundError:
    print("Error: The 'displayplacer' command is not installed or not found in PATH.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

os._exit(0)
