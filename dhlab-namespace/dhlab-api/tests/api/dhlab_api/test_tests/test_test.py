import pytest

import dhlab.api.dhlab_api as api

@pytest.fixture(autouse=True)
def api_fn():
    return api.collocation

