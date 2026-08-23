import os
import subprocess
import nicegui
from pathlib import Path


def build():
    # 1. Dynamically locate the NiceGUI installation folder
    nicegui_dir = Path(nicegui.__file__).parent

    # 2. OS-aware separator for the --add-data flag
    # PyInstaller uses ';' on Windows and ':' on Linux/macOS
    separator = ';' if os.name == 'nt' else ':'
    add_data_flag = f"{nicegui_dir}{separator}nicegui"

    # 3. Construct the PyInstaller command
    command = [
        "pyinstaller",
        "--onefile",
        "--windowed",  # Hides the black console window
        "--name", "SpectroApp",  # Name of the generated .exe
        "--add-data", add_data_flag,
        "--collect-all", "matplotlib",
        "--clean",  # Clears previous build cache
        "-y",  # Overwrites existing output without prompting
        "main.py"
    ]

    print(f"Running build command:\n{' '.join(command)}\n")

    # 4. Execute the command
    try:
        subprocess.run(command, check=True)
        print("\n✅ Build successful! Check the 'dist' folder for SpectroApp.exe")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed with exit code {e.returncode}")


if __name__ == "__main__":
    build()