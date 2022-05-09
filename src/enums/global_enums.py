from enum import Enum
import pytest

class GlobalErrorMessaged(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'Number of items is not equal excepted'

# @pytest.mark.parametrize('status', [
#     'ACTIVE',
#     'BANNED',
#     'DELETED',
#     'INCTIVE',
# ])