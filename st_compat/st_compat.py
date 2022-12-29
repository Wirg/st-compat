import streamlit as st
from packaging import version


st_version = version.parse(st.__version__)

if st_version >= version.parse("1.12.0"):
    from streamlit.runtime.scriptrunner import get_script_run_ctx
elif st_version >= version.parse("1.8.0"):
    from streamlit.scriptrunner.script_run_context import get_script_run_ctx
elif st_version >= version.parse("1.4.0"):
    from streamlit.script_run_context import get_script_run_ctx
elif st_version >= version.parse("0.65"):
    from streamlit.report_thread import get_report_ctx as get_script_run_ctx
else:
    from streamlit.ReportThread import get_report_ctx as get_script_run_ctx
