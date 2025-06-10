import pytest

import dhlab_ns.api.dhlab_api as api

@pytest.fixture(autouse=True)
def api_fn():
    return api.collocation

