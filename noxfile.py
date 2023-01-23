from typing import List

import nox
import nox_poetry

LATEST = "@latest"


def with_python_versions(python_versions: List[str], st_version: str):
    return [(python_version, st_version) for python_version in python_versions]


PYTHON_ST_TQDM_VERSIONS = (
    with_python_versions(["3.7", "3.8", "3.9"], "==0.65.*")
    + with_python_versions(["3.7", "3.8", "3.9"], "==1.2.*")
    + with_python_versions(["3.7", "3.8", "3.9"], "==1.3.*")
    + with_python_versions(["3.7", "3.8", "3.9"], "==1.4.*")
    + with_python_versions(["3.8", "3.9", "3.10"], "==1.8.*")
    + with_python_versions(["3.9", "3.10"], LATEST)
)


@nox_poetry.session
@nox.parametrize(["python", "streamlit_version"], PYTHON_ST_TQDM_VERSIONS)
def tests(session: nox_poetry.Session, streamlit_version):
    dependencies_to_install_with_pip: List[str] = [
        name if version == LATEST else name + version for name, version in [("streamlit", streamlit_version)]
    ]

    session.install("pytest", "pytest-cov", ".")
    session.run("pip", "install", "-U", *dependencies_to_install_with_pip)
    session.run("pytest", "--cov=st_compat", "--cov-report=xml:codecov.xml")


@nox_poetry.session(python=None)
def isort(session: nox.Session):
    session.install("isort")
    session.run("isort", ".", "--check")


@nox_poetry.session(python=None)
def black(session: nox.Session):
    session.install("black")
    session.run("black", ".", "--check")


@nox_poetry.session(python=None)
def lint(session: nox.Session):
    session.install("pylint", "nox", "nox_poetry", "tqdm", "streamlit")
    session.run("pylint", "st_compat", "tests", "noxfile.py")
