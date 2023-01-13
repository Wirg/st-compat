# pylint: disable=import-outside-toplevel
import functools
import threading
from types import SimpleNamespace
from typing import Callable
from unittest.mock import patch, sentinel


def mock_for_streamlit_context(wrapped: Callable):
    @functools.wraps(wrapped)
    def _mocked(*args, **kwargs):
        from st_compat.runtime.scriptrunner import SCRIPT_RUN_CONTEXT_ATTR_NAME

        with patch.object(
            threading,
            "current_thread",
            return_value=SimpleNamespace(**{SCRIPT_RUN_CONTEXT_ATTR_NAME: sentinel.script_run_context}),
        ):
            return wrapped(*args, **kwargs)

    return _mocked


def test_get_script_run_ctx():
    from st_compat.runtime.scriptrunner import get_script_run_ctx

    assert get_script_run_ctx() is None


@mock_for_streamlit_context
def test_get_script_run_ctx_in_thread():
    from st_compat.runtime.scriptrunner import get_script_run_ctx

    assert get_script_run_ctx() is sentinel.script_run_context
