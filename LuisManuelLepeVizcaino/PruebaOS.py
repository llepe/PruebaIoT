import os
print(os.name)

from pathlib import Path
IS_RPI = Path("/etc/rpi-issue").exists()


print(IS_RPI)