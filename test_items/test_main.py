import pytest

from src.url_checker import UrlChecker
from src.url_status import UrlStatus


@pytest.fixture
def url_checker():
    """ Returns an empty UrlChecker object """
    return UrlChecker()


@pytest.fixture
def url_status():
    """ Returns an empty UrlStatus object """
    return UrlStatus("", "", "")


def test_status_code_200(url_checker):
    result = url_checker.get_url_status_code("https://www.google.ca/", 2.5)
    assert result.get_status_code() == 200


def test_status_code_unknown(url_checker):
    result = url_checker.get_url_status_code("", 2.5)
    assert result.get_result_name() == "UNKNOWN"


def test_html_tags(url_checker):
    result = url_checker.remove_html_tags("<a>unchanged<a/>")
    assert result == "unchanged"


def test_status_code_store(url_status):
    result = url_status.get_status_code()
    assert result == ""


def test_file(url_checker):
    with pytest.raises(FileNotFoundError):
        url_checker.parse_urls_from_file("thisFileDoesNotExist")
