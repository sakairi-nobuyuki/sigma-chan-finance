# coding: utf-8

import torch



class SigmaChanRNN(torch.nn.Module):
    def __init__(self, input_size: int, hidden_layer_units: int) -> None:
        super().__init__()
        self.network = torch.nn.RNN(1, hidden_layer_units, batch_first=True)
        #self.network = torch.nn.RNN(input_size, hidden_layer_units, batch_first=True)
        self.fc = torch.nn.Linear(hidden_layer_units, 1)

    def forward(self, x) -> torch.nn.Linear:
        y, h = self.network(x, None)
        return self.fc(y[:, -1, :])
