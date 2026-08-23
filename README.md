# cbk-spectrometer
A repository containing code to modernize CBK spectrometer. 

## Building the Executable

This project includes a Python-based build script that automatically handles PyInstaller configuration, missing Matplotlib dependencies, and cross-platform web asset paths for NiceGUI.

### Prerequisites
Make sure you have [uv](https://github.com/astral-sh/uv) installed to manage dependencies and the virtual environment.

### Build Locally
To compile the standalone Windows executable, run the following command from the project root:

```bash
cd src/spectroscope
uv run python build.py
```