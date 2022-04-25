from src.ses_send import SESSend


class TestSESMail:
    def test_sesmail(self):
        x = SESSend()
        assert isinstance(x, object)
