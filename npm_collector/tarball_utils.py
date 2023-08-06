import subprocess


# returns output of npm pack
def downlaod_tar(package_name: str) -> str:
    return subprocess.getoutput("npm pack jest@latest")
