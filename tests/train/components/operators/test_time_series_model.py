# coding: utf-8


from train.components.operators import RNN


class TestRnn:
    def test_init(self):
        model = RNN(256, 13)

        assert isinstance(model, RNN)
