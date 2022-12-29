# stqdm
[![Tests](https://github.com/Wirg/st-compat/actions/workflows/tests.yml/badge.svg)](https://github.com/Wirg/st-compat/actions/workflows/tests.yml)
[![CodeQL](https://github.com/Wirg/st-compat/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Wirg/st-compat/actions/workflows/codeql-analysis.yml)

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
