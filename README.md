# st-compat
[![Tests](https://github.com/Wirg/st-compat/actions/workflows/tests.yml/badge.svg)](https://github.com/Wirg/st-compat/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/Wirg/st-compat/branch/main/graph/badge.svg?token=DSA23TOBWV)](https://codecov.io/github/Wirg/st-compat)
[![CodeQL](https://github.com/Wirg/st-compat/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Wirg/st-compat/actions/workflows/codeql-analysis.yml)
[![Downloads](https://static.pepy.tech/personalized-badge/st-compat?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads/month)](https://pepy.tech/project/st-compat)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/st-compat)
![pypi version](https://img.shields.io/pypi/v/st-compat)

`st-compat` is the simplest way to handle compatibility between streamlit versions when building utils and modules for the community!

## How to install

```sh
pip install st-compat
```

## How to use

```python
from st_compat import get_script_run_ctx

ctx = get_script_run_ctx()
```
