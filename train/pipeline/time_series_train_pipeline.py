# coding: utf-8

from typing import Any
from train.components import TimeSeriesTrainConfig
import torch

class TimeSeriesTrainPipeline:
    def __init__(self) -> None:
        self.train_config = TimeSeriesTrainConfig()

        self.train_loader = 0.0

        ### compile model
        self.model = self.compile_model()
        self.loss_function = torch.nn.L1Loss()
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.01)


    def compile_model(self) -> Any:
        model = self.train_config.load_sigma_chan_rnn()

        return model


    def train_model(self, n_epochs: int) -> Any:
        train_loss_record = []
        for i in range(n_epochs):
            self.model.train()
            train_loss = 0.0

            for j, (x, t) in enumerate(self.train_loader):
                loss = self.loss_function(self.model(x), t.to(self.train_config.device))
                train_loss += loss.item()
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
            train_loss /= float(j+1)

            train_loss_record.append(train_loss)