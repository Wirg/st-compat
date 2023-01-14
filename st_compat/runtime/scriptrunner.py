from packaging import version

from st_compat.version import st_version

# pylint: disable=no-name-in-module,import-error,import-outside-toplevel
if st_version >= version.parse("1.12.0"):
    from streamlit.runtime.scriptrunner.script_run_context import (
        SCRIPT_RUN_CONTEXT_ATTR_NAME,
        add_script_run_ctx,
        get_script_run_ctx,
    )
elif st_version >= version.parse("1.8.0"):
    from streamlit.scriptrunner.script_run_context import (
        SCRIPT_RUN_CONTEXT_ATTR_NAME,
        add_script_run_ctx,
        get_script_run_ctx,
    )
elif st_version >= version.parse("1.4.0"):
    from streamlit.script_run_context import (
        SCRIPT_RUN_CONTEXT_ATTR_NAME,
        add_script_run_ctx,
        get_script_run_ctx,
    )
elif st_version >= version.parse("0.65"):
    from streamlit.report_thread import (
        REPORT_CONTEXT_ATTR_NAME as SCRIPT_RUN_CONTEXT_ATTR_NAME,
    )
    from streamlit.report_thread import add_report_ctx as add_script_run_ctx
    from streamlit.report_thread import get_report_ctx as get_script_run_ctx
else:
    raise ModuleNotFoundError(f"Not supporting streamlit version before 0.65, found: {st_version}")
# pylint: enable=no-name-in-module,import-error,import-outside-toplevel

__all__ = [
    "add_script_run_ctx",
    "get_script_run_ctx",
    "SCRIPT_RUN_CONTEXT_ATTR_NAME",
]
