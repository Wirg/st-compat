import streamlit as st
from packaging import version

st_version = version.parse(st.__version__)
min_supported_version = version.parse("0.65")

if st_version < min_supported_version:
    raise ModuleNotFoundError(f"Not supporting streamlit version below {min_supported_version}, found: {st_version}")
