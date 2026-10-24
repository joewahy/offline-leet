def pytest_addoption(parser):
    parser.addoption(
        "--solutions",
        action="store_true",
        help="also run test_solutions.py, which tests your own solution.py files",
    )


def pytest_ignore_collect(collection_path, config):
    """test_solutions.py is for the learner's unfinished code, so it fails on a fresh clone."""
    if collection_path.name == "test_solutions.py" and not config.getoption("--solutions"):
        return True
