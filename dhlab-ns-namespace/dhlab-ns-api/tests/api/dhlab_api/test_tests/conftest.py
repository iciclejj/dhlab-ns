from unittest.mock import MagicMock
import requests
import pytest

from dhlab.api.utils import DHLabApiError
import tests.api.utils as apitest

@pytest.mark.usefixtures("api_fn")
@pytest.fixture(scope="session", autouse=True)
@pytest.mark.parametrize("error_status_code", (404, 500, 504, 418,))
def test_error_status_codes(request, error_status_code):
    api_fn = getattr(request.module, "api_fn")
    mock_response = MagicMock(spec=requests.Response)
    mock_response.reason = "Mocked reason"
    mock_response.status_code = error_status_code
    session = apitest.mock_api_call(response=mock_response)

    with pytest.raises(DHLabApiError):
        api_fn(session=session)

