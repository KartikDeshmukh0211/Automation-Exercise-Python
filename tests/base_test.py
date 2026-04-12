import pytest

from utils.logger import get_logger

@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    def setup_method(self, method):
        self.logger = get_logger(method.__name__)