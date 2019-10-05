import pytest

from shelob.core.attribute import AttributeType


@pytest.fixture(scope="session")
def int_attribute_type():
    class IntAttribute(AttributeType):
        @classmethod
        def validate(cls, value):
            if isinstance(value, int):
                return True
            else:
                return False

    return IntAttribute

