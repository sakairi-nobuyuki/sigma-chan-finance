# coding: utf-8

from train.components.operators import TimeSeriesTrain
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
from torch.utils.data import DataLoader

import numpy as np


class TrainRnn(TimeSeriesTrain):
    def __init__(self) -> None:
        super().__init__()