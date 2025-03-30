import os
from colorama import init, Fore, Style
import time
import stat
from tqdm import tqdm

dir = "repos"

for dirpath, dirnames, filenames in tqdm(os.walk(dir)):
    for f in filenames:
        full_path = os.path.join(dirpath, f)

        if full_path.endswith(".py"):
            pass
        else:
            if dir in full_path:
                try:
                    os.chmod(full_path, stat.S_IWRITE)  # Ensure file is writable
                    os.remove(full_path)
                except PermissionError as e:
                    print(f"Permission Error: {e}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(Fore.YELLOW + Style.BRIGHT + f"SOMETHING IS WRONG")
                time.sleep(60)
    