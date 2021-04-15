# library
# standard library
import os
from PIL import Image
import torch
import torch.nn as nn
import torch.utils.data as Data
import torchvision
import matplotlib.pyplot as plt
from torchvision import transforms
import numpy as np
import utils


class SSlayer(nn.Module):
    def __init__(self, requires_grad=False):
        super(SSlayer, self).__init__()

        cov_module = nn.Conv2d(in_channels=3, out_channels=3, kernel_size=16, stride=16, padding=0, bias=False)

        weight = utils.get_3DGauss()  # [16,16]
        weight = weight.unsqueeze(0).unsqueeze(0)  # [1,1,16,16]
        weight = torch.cat([weight, weight, weight], dim=1)  # [1,3,16,16]
        cov_module.weight = nn.Parameter(weight)
        self.conv_module = nn.Sequential(
            cov_module
        )

        if not requires_grad:
            for param in self.parameters():
                param.requires_grad = False # each kernel is fixed to gauss weight

    def forward(self, x):
        x = x.repeat(1, 1, 1, 1)
        x = self.conv_module(x)
        return x  # return x for visualization
