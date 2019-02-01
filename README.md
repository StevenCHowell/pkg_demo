# Python Packaging Notes

[Python Packaging Documentation](https://python-packaging.readthedocs.io/en/latest/minimal.html)





To reload a module, use `importlib.reload`.

```python
>>> import mod
a = [100, 200, 300]

>>> import mod

>>> import importlib
>>> importlib.reload(mod)
a = [100, 200, 300]
```
