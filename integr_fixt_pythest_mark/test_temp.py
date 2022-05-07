import sys

import pytest


@pytest.mark.skip(reason="Баг в продукте - <ссылка>")
def test_one():
    pass


minversion = pytest.mark.skipif(
    sys.version_info < (3, 10), reason="at least mymodule-1.1 required"
)

@minversion
def test_python36_and_greater():
    pass


@pytest.mark.xfail(sys.platform == "Win32", reason="Ошибка в системной библиотеке")
def test_not_for_windows():
    pass


@pytest.mark.xfail(raises=RuntimeError)
def test_x_status_runtime_only():
    pass

@pytest.mark.xfail
def test_flaky():
    pass

