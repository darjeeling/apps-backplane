import pytest


@pytest.mark.django_db
def test_default():
    assert 1 == 1
