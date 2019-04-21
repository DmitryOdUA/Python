import pytest


@pytest.fixture(scope='class', autouse=True)
def suite_data():
    print("\n> Suite setup")
    yield
    print("> Suite teardown")


@pytest.fixture(autouse=True)
def case_data():
    print("   > Case setup")
    yield
    print("\n   > Case teardown")
