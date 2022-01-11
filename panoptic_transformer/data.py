from pathlib import Path
from random import choice
from PIL import Image
import numpy as np

import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torch.utils.data import random_split
from torchvision import transforms as T

class PathfinderXDataset(Dataset):
    def __init__(
        self,
        folder,
        augment = False
    ):
        super().__init__()
        metadata_files = [*Path(folder).glob(f'**/*.npy')]
        assert len(metadata_files) > 0, 'not able to find more than 1 metadata file'

        metadata_file = metadata_files[0]
        metadata = np.load(str(metadata_file))
        root_path = metadata_file.parents[1]

        self.augment = augment
        self.data = [(str(root_path / m[0] / m[1]), int(m[3])) for m in metadata]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, ind):
        path, label = self.data[ind]
        img = Image.open(path)

        img = T.Compose([
            T.RandomHorizontalFlip() if self.augment else nn.Identity(),
            T.RandomVerticalFlip() if self.augment else nn.Identity(),
            T.PILToTensor()
        ])(img)

        label = torch.tensor(label, dtype = torch.float32)

        if self.augment:
            rand_rotate = [0, 90, 180, 270]
            img = T.functional.rotate(img, choice(rand_rotate))
            rand_padding = [(0, 0, 0, 0), (1, -1, 0, 0), (-1, 1, 0, 0), (0, 0, 1, -1), (0, 0, -1, 1)]
            img = F.pad(img, choice(rand_padding))

        return img.float(), label
