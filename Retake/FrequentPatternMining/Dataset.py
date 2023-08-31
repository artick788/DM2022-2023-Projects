import numpy as np
import random

VALIDATE_RATIO = 0.2


class Dataset:
    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            self.dataset = [set(line.strip().split()) for line in file.readlines()]


    def split_dataset(self):
        train_size = int(len(self.dataset) * (1 - VALIDATE_RATIO))
        train_data = self.dataset[:train_size]

        np.random.seed(0)

        # create the test dataset
        # get the last element of each of the test dataset elements
        user_items = dict()
        user_item_indices = [0 for _ in range(len(self.dataset[train_size:]))]
        for i, test_el in enumerate(self.dataset[train_size:]):
            if len(test_el) > 1:
                item_index = np.random.randint(0, len(test_el))
                user_item_indices[i] = item_index
                user_items[i] = sorted(list(test_el))[item_index]

        # remove the last element of each of the test dataset elements
        test_data = dict()
        for i, test_el in enumerate(self.dataset[train_size:]):
            if len(test_el) > 1:
                test_data[i] = test_el - set(
                    sorted(list(test_el))[user_item_indices[i]])

        return train_data, test_data, user_items

