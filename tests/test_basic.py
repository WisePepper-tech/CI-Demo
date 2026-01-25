from app.brokeme import summary


def test_summary():
    assert summary(2, 3) == 5  # nosec B101
