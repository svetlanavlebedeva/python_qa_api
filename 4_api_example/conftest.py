import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://run.mocky.io/v3/f545c75d-4a62-450d-b9fd-bfeb9ae0a583",
                     help="Url for test API mock")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
