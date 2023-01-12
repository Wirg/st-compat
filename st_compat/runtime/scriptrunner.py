from packaging import version

from st_compat.version import st_version


if st_version >= version.parse("1.12.0"):
    from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx, SCRIPT_RUN_CONTEXT_ATTR_NAME
elif st_version >= version.parse("1.8.0"):
    from streamlit.scriptrunner.script_run_context import get_script_run_ctx, SCRIPT_RUN_CONTEXT_ATTR_NAME
elif st_version >= version.parse("1.4.0"):
    from streamlit.script_run_context import get_script_run_ctx, SCRIPT_RUN_CONTEXT_ATTR_NAME
elif st_version >= version.parse("0.65"):
    from streamlit.report_thread import get_report_ctx as get_script_run_ctx, REPORT_CONTEXT_ATTR_NAME as SCRIPT_RUN_CONTEXT_ATTR_NAME
else:
    from streamlit.ReportThread import get_report_ctx as get_script_run_ctx, REPORT_CONTEXT_ATTR_NAME as SCRIPT_RUN_CONTEXT_ATTR_NAME

