import pytest
#from selenium.webdriver.common.by import By

#example of fixture
# Define a simple fixture with function scope (default)
@pytest.fixture
def sample_fixture():
    # Setup code before yield
    print("Setup: Starting the test")
    yield 42  # This value will be passed to the test function

    # Teardown code after yield
    print("Teardown: Ending the test")

# Use the fixture in a test function
def test_example(sample_fixture):
    # The fixture's return value is available in the test
    assert sample_fixture == 42
    print("Test: Running test_example with fixture value", sample_fixture)

# Another test function using the same fixture
def test_another_example(sample_fixture):
    # The fixture will be set up and torn down again for this test
    assert sample_fixture == 42
    print("Test: Running test_another_example with fixture value", sample_fixture)



# Working with the fixture scope
# Function scope: runs once per test function
@pytest.fixture(scope="function")
def func_scope():
    print("\nRunning function scope fixture")
    yield
    print("Tearing down function scope fixture")

# Class scope: runs once per test class
@pytest.fixture(scope="class")
def class_scope():
    print("\nRunning class scope fixture")
    yield
    print("Tearing down class scope fixture")

# Module scope: runs once per module
@pytest.fixture(scope="module")
def module_scope():
    print("\nRunning module scope fixture")
    yield
    print("Tearing down module scope fixture")

# Session scope: runs once per session
@pytest.fixture(scope="session")
def session_scope():
    print("\nRunning session scope fixture")
    yield
    print("Tearing down session scope fixture")

def test_1(func_scope):
    print("Executing test_1")


@pytest.mark.usefixtures("class_scope")
class TestClass:
    def test_3(self):
        print("Executing test_3 within a class")

    def test_4(self):
        print("Executing test_4 within a class")

def test_5(module_scope):
    print("Executing test_5 in a module")

def test_6(session_scope):
    print("Executing test_6 in a session")



# Define an autouse fixture with module scope
@pytest.fixture(autouse=True, scope="module")
def setup_and_teardown():
    # Setup code before yield
    print("Setup: Module-wide setup code runs before any tests")
    yield
    # Teardown code after yield
    print("Teardown: Module-wide teardown code runs after all tests")

def test_one():
    # This test will automatically use the autouse fixture
    print("Test: Running test_one")

def test_two():
    # This test will also automatically use the autouse fixture
    print("Test: Running test_two")
