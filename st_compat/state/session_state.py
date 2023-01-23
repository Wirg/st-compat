# pylint: disable=no-name-in-module,import-error,import-outside-toplevel

from packaging import version

from st_compat.version import st_version

if st_version >= version.parse("0.84.0"):
    from streamlit import session_state
else:
    from .streamlit_1_12_session_state.session_state_proxy import SessionStateProxy

    session_state = SessionStateProxy()

__all__ = ["session_state"]
