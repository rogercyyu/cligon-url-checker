import pytest
import responses
import requests

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


def custom_response(link, status_code):
    """ Setting up mock network response """
    responses.add(responses.HEAD, link, status=status_code)
    resp_code = requests.head(link, timeout=2.5).status_code
    assert resp_code == status_code


@pytest.mark.parametrize(
    "url, expected_code, expected_result",
    [
        ("http://google.ca/", 404, "BAD"),
        ("http://google.ca/", 200, "GOOD"),
        ("http://google.ca/", 300, "UNKNOWN"),
        ("http://youtube.com", 404, "BAD"),
        ("http://testurl.com", 200, "GOOD"),
        ("http://123456.com", 300, "UNKNOWN"),
    ],
)
@responses.activate
def test_status_codes(url_checker, url, expected_code, expected_result):
    custom_response(url, expected_code)
    result = url_checker.get_url_status_code(url, 2.5)
    assert result.get_status_code() == expected_code
    assert result.get_result_name() == expected_result


@responses.activate
def test_status_code_exception(url_checker):
    with pytest.raises(requests.exceptions.MissingSchema):
        custom_response("unknown", 0)
        url_checker.get_url_status_code("unknown", 2.5)


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
