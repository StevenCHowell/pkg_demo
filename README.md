# Python Packaging Notes

[Python Packaging Documentation](https://python-packaging.readthedocs.io/en/latest/minimal.html)

The structure of the file should follow the patern

```
repo_dir/
    package_dir/
        __init__.py
        some_code.py
    setup.py
```

To install this package in edit mode, run the command

```bash
pip install -e path/to/repo_dir
```

Note, to reload a module after making changes, use `importlib.reload`.

```python
>>> import mod
a = [100, 200, 300]

>>> import mod

>>> import importlib
>>> importlib.reload(mod)
a = [100, 200, 300]
```
