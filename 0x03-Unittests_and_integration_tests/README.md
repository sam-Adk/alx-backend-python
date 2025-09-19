0x03. Unittests and Integration Tests
📌 Description

This project focuses on writing unit tests and integration tests in Python.
You will learn how to:

Test functions and classes using the unittest module.

Use parameterized tests for efficiency.

Mock external calls (e.g., HTTP requests) with unittest.mock.patch.

Implement memoization tests.

Differentiate between unit tests (isolated tests) and integration tests (testing interactions between components).

📂 Project Structure
0x03-Unittests_and_integration_tests/
│── client.py               # GithubOrgClient class implementation
│── utils.py                # Helper functions (get_json, access_nested_map, memoize, etc.)
│── fixtures.py             # Example payloads for integration testing
│── test_utils.py           # Unit tests for utils.py
│── test_client.py          # Unit & integration tests for client.py
└── README.md               # Project documentation

⚙️ Requirements

Python 3.7+

unittest (built-in)

parameterized

requests

Install dependencies:

pip install requests parameterized

🧪 Running Tests

Run all tests with:

python3 -m unittest discover -v


Run a specific test file:

python3 -m unittest -v test_utils.py
python3 -m unittest -v test_client.py

📝 Tasks Overview
test_utils.py

Parameterize a unit test – Test access_nested_map.

Mock HTTP calls – Test get_json with patched requests.get.

Memoization – Test the @memoize decorator.

test_client.py

Patch as decorators – Test GithubOrgClient.org.

Mocking a property – Test _public_repos_url.

More patching – Test public_repos.

Parameterize – Test has_license.

Integration tests with fixtures – Test public_repos using mocked requests.get.

Integration tests (with filters) – Test public_repos with license filtering.

📊 Example Test Results
python3 -m unittest -v test_client.py


Output:

test_org_0_google ... ok
test_org_1_abc ... ok
test_public_repos ... ok
test_has_license_0 ... ok
test_has_license_1 ... ok
test_public_repos_url ... ok
test_public_repos_with_license ... ok
----------------------------------------------------------------------
Ran 7 tests in 0.015s

OK

🎯 Learning Objectives

Understand test-driven development (TDD).

Write effective unit tests and integration tests.

Learn how to mock I/O and HTTP calls.

Apply parameterization to reduce redundancy in tests.
