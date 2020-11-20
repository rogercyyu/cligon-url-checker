import pytest
import responses
import requests
import argparse

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


@pytest.fixture
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-j",
        "--json",
        action="store_true",
    )
    parser.add_argument("--good", action="store_true")
    parser.add_argument("--bad", action="store_true")
    return parser


def custom_response(link, status_code):
    """ Setting up mock network response """
    responses.add(responses.HEAD, link, status=status_code)
    resp_code = requests.head(link, timeout=2.5).status_code
    assert resp_code == status_code


@pytest.mark.parametrize(
    "url, status_code, expected_result",
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
def test_status_codes(url_checker, url, status_code, expected_result):
    custom_response(url, status_code)
    result = url_checker.get_url_status_code(url, 2.5)
    assert result.get_status_code() == status_code
    assert result.get_result_name() == expected_result


@responses.activate
def test_urls_thread(url_checker):
    urls = ["http://www.test.com"]
    status_code = 404
    custom_response(urls[0], status_code)
    result = url_checker.check_urls_thread(urls, 2.5)
    assert result[0].get_status_code() == status_code
    assert result[0].get_result_name() == "BAD"


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


@responses.activate
def test_bad_color(url_checker):
    url = "http://www.test.com"
    custom_response(url, 404)
    result = url_checker.get_url_status_code(url, 2.5)
    assert result.color() == "\033[31m"


@responses.activate
def test_status_output_json(url_checker, create_parser):
    parser = create_parser
    parsed = parser.parse_args(["--json"])
    url = "http://www.test.com"
    custom_response(url, 404)
    result = url_checker.get_url_status_code(url, 2.5)

    assert result.output(parsed) == '{ "url": "http://www.test.com", "status": "404" }'


@responses.activate
def test_status_output(url_checker, create_parser):
    answer_str = "\x1b[31mBAD    \x1b[0m -> \x1b[31mhttp://www.test.com\x1b[0m"
    parser = create_parser
    parsed = parser.parse_args()
    url = "http://www.test.com"
    custom_response(url, 404)
    result = url_checker.get_url_status_code(url, 2.5)

    assert result.output(parsed) == answer_str


@responses.activate
def test_output_urls_and_status(url_checker, create_parser, capsys):
    answer_str = "\x1b[32mGOOD   \x1b[0m -> \x1b[32mhttp://www.test.com\x1b[0m\n"
    parser = create_parser
    parsed = parser.parse_args(["--good"])
    # Create custom UrlStatus object
    url_status_list = []
    url_status = UrlStatus("http://www.test.com", "GOOD", 200)
    url_status_list.append(url_status)
    # Actual test
    url_checker.output_urls_and_status(url_status_list, parsed)
    captured = capsys.readouterr()

    assert captured.out == answer_str
