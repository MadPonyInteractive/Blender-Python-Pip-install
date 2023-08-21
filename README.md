# Install any python package/module into Blender

This is an alternative solution to the original forked repo: 
https://github.com/luckychris/install_blender_python_modules

This are usefull python functions that can be used to install or uninstall pip packages directly into blender  
extending blender python libraries.

## Usage
If using "import" like the examples bellow, add blender_pip.py to the same location where your __init__.py addon file is.

In case your addon is a single file, you can simply copy the code in blender_pip.py and paste it in your __init__.py file.
 
Let's say your addon needs "scipy" to function faster, then in your __init__.py file you can use:
```python
from blender_pip import install_pip_package

install_pip_package("scipy")
```

Or if you then choose to not use the package anymore you can use:
```python
from blender_pip import uninstall_pip_package

uninstall_pip_package("scipy")
```

Alternatively you can use the original function instead of the partials:
```python
from blender_pip import pip_package

# install
pip_package("scipy")

# uninstall
pip_package("scipy", install=False)

```


## Contribute

This should work in any Operating System, I tested it on Windows and it was forked from a user who tested it on MacOs but if it does not work on your system please open an issue so that I can update it and make it useful for anyone.
