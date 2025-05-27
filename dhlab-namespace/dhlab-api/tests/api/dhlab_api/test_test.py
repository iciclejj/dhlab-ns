import pytest

import dhlab.api.dhlab_api as api

@pytest.fixture(scope="module")
def api_fn():
    return api.collocation

