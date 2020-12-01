import src.cligon as cl
import pytest

path = "tests/test_cases.html"


def _args(**override):
    args = {
        "filename": path,
        "json": False,
        "all": False,
        "good": False,
        "bad": False,
    }
    args.update(override)
    return args


@pytest.mark.parametrize(
    "argv, result",
    [
        ([path, "-j"], _args(json=True)),
        ([path, "--all"], _args(all=True)),
        ([path, "--bad"], _args(bad=True)),
        ([path, "--good"], _args(good=True)),
    ],
)
def test_process_arguments(argv, result):
    assert vars(cl.process_arguments(argv)) == result
