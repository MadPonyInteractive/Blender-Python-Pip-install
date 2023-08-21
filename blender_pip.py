from functools import partial


def pip_package(pkg, install=True):
    """
    ### Installs/Uninstalls python packages into Blender

    Install Example:
        pip_package("scipy")

    Uninstall Example:
        pip_package("scipy", install=False)
    """
    import subprocess
    import sys
    import os
    import platform
    import bpy

    # Determine the platform and adapt the python binary path accordingly
    if platform.system() == "Windows":
        python_exe = os.path.join(sys.prefix, "bin", "python.exe")
    elif platform.system() == "Darwin":  # MacOS
        if hasattr(bpy.app, "binary_path_python"):
            # 2.92 and older
            path = bpy.app.binary_path_python  # type: ignore
        else:
            # 2.93 and later
            import sys

            path = sys.executable
        python_exe = os.path.abspath(path)
    elif platform.system() == "Linux":
        python_exe = os.path.join(sys.prefix, "sys.prefix/bin", "python")
    else:
        print(
            "Sorry, still not implemented for ",
            os.name,
            " - ",
            platform.system(),
        )
        return

    if not install:
        # uninstall package
        subprocess.check_call([python_exe, "-m", "pip", "uninstall", pkg])
        return

    try:
        subprocess.check_call([python_exe, "import ", pkg])
    except:
        # upgrade pip
        subprocess.check_call([python_exe, "-m", "ensurepip"])
        subprocess.check_call(
            [python_exe, "-m", "pip", "install", "--upgrade", "pip"]
        )

        # install required packages
        subprocess.check_call([python_exe, "-m", "pip", "install", pkg])


install_pip_package = partial(pip_package, install=True)
"""Installs a pip package into Blender's python bin"""

uninstall_pip_package = partial(pip_package, install=False)
"""Uninstalls a pip package from Blender's python bin.
Note: This is mainly useful for development purposes as you will need
to confirm the uninstallation of the package in the terminal."""
