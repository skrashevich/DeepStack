import wget
import shutil
import os
from concurrent.futures import ThreadPoolExecutor


def download(url, name):
    print(f"Downloading {url}\n")
    zip_name = f"{name}.zip"
    wget.download(url, zip_name)

    print(f"\nExtracting {zip_name}\n")

    shutil.unpack_archive(zip_name, name)
    os.remove(zip_name)
    print(f"\nDone unpacking {name}")


urls_and_names = [
    ("https://deepquest.sfo2.digitaloceanspaces.com/deepstack/shared-files/sharedfiles.zip", "sharedfiles"),
    ("https://deepquest.sfo2.digitaloceanspaces.com/deepstack/shared-files/interpreter.zip", "interpreter"),
    ("https://deepquest.sfo2.digitaloceanspaces.com/deepstack/shared-files/redis.zip", "redis"),
    ("https://deepquest.sfo2.digitaloceanspaces.com/deepstack/windows_packages_cpu.zip", "windows_packages_cpu"),
    ("https://deepquest.sfo2.digitaloceanspaces.com/deepstack/windows_packages_gpu.zip", "windows_packages_gpu"),
    ("https://deepquest.sfo2.digitaloceanspaces.com/deepstack/shared-files/windows_setup.zip", "windows_setup")
]

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(download, url, name) for url, name in urls_and_names]

    for future in futures:
        future.result()
