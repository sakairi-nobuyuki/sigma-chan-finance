# coding: utf-8


from train.components import SigmaChanRNN


class TestRnn:
    def test_init(self):
        model = SigmaChanRNN(256, 13)

        assert isinstance(model, SigmaChanRNN)
