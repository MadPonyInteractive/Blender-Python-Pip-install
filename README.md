# Install any python package/module into Blender

This is an alternative solution to the original forked repo: 
https://github.com/luckychris/install_blender_python_modules

This is a usefull python function that can be called to install or uninstall pip packages directly into blender python's libraries.

## Usage

Let's say your addon needs "scipy" to function faster, then in your __init__.py file you can use:
```python
install_pip_package("scipy")
```

Or if you then choose to not use the package anymore you can use:
```python
uninstall_pip_package("scipy")
```

## Contribute

This should work in any Operating System, I tested it on Windows and it was forked from a user that tested it on MacOs but if it does not work on your system please open an issue so that I can update it and make it useful for all.
