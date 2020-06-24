# Example Python Packaging Notes

[Python.org Packaging Tutorial](https://packaging.python.org/tutorials/packaging-projects/).
[Python Packaging Documentation](https://python-packaging.readthedocs.io/en/latest/minimal.html)

The structure of the file should follow the pattern

```
repo_dir/
├── LICENSE
├── README.md
├── package_dir/
│   └── pkg_code.py
├── setup.py
└── tests/
    └── some_test.py
```

To install this package in edit mode, run the command

```bash
pip install -e path/to/repo_dir
```

Note, to reload a module after making changes, use `importlib.reload`.

```python
>>> import mod
a = [100, 200, 300]

# make some change to the `mod` source code
>>> import mod
# did not actually import because it was already loaded

>>> import importlib
>>> importlib.reload(mod)
a = [100, 200, 300]
```

This readme can be expanded using
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
in whatever way makes sense to describe the content.
