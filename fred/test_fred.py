import pytest

from furl import furl
from hypothesis import given, assume
from hypothesis.strategies import text

from fred.service.fred import FredWrapper
# Tests for the Fred Wrapper


@given(text())
def test_FredWrapper__build_url_normal(endpoint):
    assume(not endpoint.startswith('/'))
    assert furl(f'https://api.stlouisfed.org/fred/{endpoint}').url ==  \
        FredWrapper(api_key='test')._build_url(endpoint)


@pytest.mark.parametrize('endpoint', [
    ('/'), ('/laksdjflaksd'), ('/k/l/'),
    ])
def test_FredWrapper__build_url_valueerror(endpoint):
    with pytest.raises(ValueError):
        FredWrapper(api_key='test')._build_url(endpoint)
