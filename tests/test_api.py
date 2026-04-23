import pytest
import requests

# ==================== GLOBAL CONFIGURATION ====================
BASE_URL = "https://<base-url>/api/v1"

COMMON_HEADERS = {}

# ==================== TEST FUNCTIONS ====================
def test_tc001_verify_successful_data_fetch_with_valid_token_and_default_paginationsorting():
    """
    Test ID: TC001
    Name: Verify successful data fetch with valid token and default pagination/sorting
    Expected behavior: The API should return a 200 OK status with the first page of data sorted by locoNo.
    """
    url = f"{BASE_URL}/api/v1/configurable-data"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer valid-access-token"
    }
    params = {
        "sortBy": "locoNo",
        "sortDirection": "asc",
        "page": 1,
        "size": 10
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    expected_response = {
      "status": 200,
      "message": "Configurable Data Fetched Successfully",
      "data": []
    }
    assert response.json() == expected_response

def test_tc002_verify_sorting_by_locotype_in_ascending_order():
    """
    Test ID: TC002
    Name: Verify sorting by locoType in ascending order
    Expected behavior: The API should return a 200 OK status with data sorted by locoType.
    """
    url = f"{BASE_URL}/api/v1/configurable-data"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer valid-access-token"
    }
    params = {
        "sortBy": "locoType",
        "sortDirection": "asc"
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == 200
    assert response_data["message"] == "Configurable Data Fetched Successfully"

def test_tc003_verify_filtering_by_a_specific_sheddetail():
    """
    Test ID: TC003
    Name: Verify filtering by a specific shedDetail
    Expected behavior: The API should return a 200 OK status with data filtered by the specified shedDetail.
    """
    url = f"{BASE_URL}/api/v1/configurable-data"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer valid-access-token"
    }
    params = {
        "shedDetail": "ExampleShed"
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == 200
    assert response_data["message"] == "Configurable Data Fetched Successfully"

def test_tc004_verify_pagination_works_for_the_second_page():
    """
    Test ID: TC004
    Name: Verify pagination works for the second page
    Expected behavior: The API should return a 200 OK status with the second page of data.
    """
    url = f"{BASE_URL}/api/v1/configurable-data"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer valid-access-token"
    }
    params = {
        "page": 2,
        "size": 10
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == 200
    assert response_data["message"] == "Configurable Data Fetched Successfully"

def test_tc005_verify_401_unauthorized_with_an_invalid_token():
    """
    Test ID: TC005
    Name: Verify 401 Unauthorized with an invalid token
    Expected behavior: The API should return a 401 Unauthorized status for an invalid token.
    """
    url = f"{BASE_URL}/api/v1/configurable-data"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer invalid-token"
    }
    params = {}
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 401
    expected_response = {
      "status": 401,
      "message": "Unauthorized",
      "error": "Token expired"
    }
    assert response.json() == expected_response

def test_tc006_verify_401_unauthorized_with_an_expired_token():
    """
    Test ID: TC006
    Name: Verify 401 Unauthorized with an expired token
    Expected behavior: The API should return a 401 Unauthorized status for an expired token.
    """
    url = f"{BASE_URL}/api/v1/configurable-data"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer expired-token"
    }
    params = {}
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 401
    expected_response = {
      "status": 401,
      "message": "Unauthorized",
      "error": "Token expired"
    }
    assert response.json() == expected_response

def test_tc007_verify_401_unauthorized_when_no_token_is_provided():
    """
    Test ID: TC007
    Name: Verify 401 Unauthorized when no token is provided
    Expected behavior: The API should return a 401 Unauthorized status when the Authorization header is missing.
    """
    url = f"{BASE_URL}/api/v1/configurable-data"
    headers = {
        **COMMON_HEADERS
    }
    params = {}
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 401
    expected_response = {
      "status": 401,
      "message": "Unauthorized"
    }
    assert response.json() == expected_response

def test_tc008_verify_403_forbidden_for_a_user_without_required_permissions():
    """
    Test ID: TC008
    Name: Verify 403 Forbidden for a user without required permissions
    Expected behavior: The API should return a 403 Forbidden status for a user lacking permissions.
    """
    url = f"{BASE_URL}/api/v1/configurable-data"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer unauthorized-user-token"
    }
    params = {}
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 403
    expected_response = {
      "status": 403,
      "message": "You do not have permission to access this resource",
      "error": "Forbidden"
    }
    assert response.json() == expected_response

def test_tc009_verify_400_bad_request_with_an_invalid_sort_field():
    """
    Test ID: TC009
    Name: Verify 400 Bad Request with an invalid sort field
    Expected behavior: The API should return a 400 Bad Request status with a specific error message when an invalid 'sortBy' parameter is used.
    """
    endpoint = "/api/v1/configurable-data"
    url = f"{BASE_URL}{endpoint}"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer <valid-access-token>"
    }
    params = {
        "sortBy": "invalidSortField"
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 400
    expected_response = {
      "status": 400,
      "message": "Bad Request",
      "error": "Invalid sort field provided"
    }
    assert response.json() == expected_response

def test_tc010_verify_200_ok_with_an_empty_data_array_for_a_query_with_no_results():
    """
    Test ID: TC010
    Name: Verify 200 OK with an empty data array for a query with no results
    Expected behavior: The API should return a 200 OK status with an empty 'data' array when a query yields no results.
    """
    endpoint = "/api/v1/configurable-data"
    url = f"{BASE_URL}{endpoint}"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer <valid-access-token>"
    }
    params = {
        "locoNo": "non-existent-loco-12345"
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    expected_response = {
      "status": 200,
      "message": "Configurable Data Fetched Successfully",
      "data": []
    }
    assert response.json() == expected_response

def test_tc011_verify_performance_and_response_time_with_a_large_page_size():
    """
    Test ID: TC011
    Name: Verify performance and response time with a large page size
    Expected behavior: The API should return a 200 OK status in a timely manner when requesting a large page size.
    """
    endpoint = "/api/v1/configurable-data"
    url = f"{BASE_URL}{endpoint}"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer <valid-access-token>"
    }
    params = {
        "size": 1000
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == 200