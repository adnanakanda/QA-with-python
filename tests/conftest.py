import pytest



@pytest.hookimpl
def pytest_report_teststatus(report,config):
    if report.when == "call":
        if report.outcome == "failed":
            return "Test Fail", "F", "Test Failed"
        elif report.outcome == "passed":
            return "Test pass", "P", "Test Passed"


def test_something():
    assert 1 + 1 == 2


"""following example, the pytest_report_teststatus hook is used to customize tests. 
If the test name is prefixed with api this test must be skipped."""

def pytest_collection_modifyitems(session, config, items):
    skip_api_marker = pytest.mark.skip(reason="This is not a UI test, this is an API test")

    for item in items:
        if "api" in item.name:
            item.add_marker(skip_api_marker)

def test_api():
    assert 1 + 1 == 2



# more example on hooks
# Hook that is called before each test function
def pytest_runtest_setup(item):
    print(f"Setting up for test: {item.name}")

# Hook that is called after each test function
def pytest_runtest_teardown(item, nextitem):
    print(f"Tearing down after test: {item.name}")

# A simple test function
def test_example():
    assert True

# Another simple test function
def test_another_example():
    assert 1 + 1 == 2

