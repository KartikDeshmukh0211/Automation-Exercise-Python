import os
import time

def is_file_downloaded(download_dir, filename_contains=None, timeout=10):
    for _ in range(timeout):
        files = os.listdir(download_dir)

        for file in files:
            if filename_contains:
                if filename_contains.lower() in file.lower():
                    return True
            else:
                return True

        time.sleep(1)

    return False