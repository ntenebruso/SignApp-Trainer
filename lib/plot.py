import os

import matplotlib
import matplotlib.pyplot as plt

from lib.util import bundle_dir, train_config

matplotlib.use('QtAgg')

NUM_EXAMPLES = 5


def plot():
    dataset_path = os.path.join(bundle_dir, train_config.get("data_dir"))
    print(dataset_path)

    labels = []
    for i in os.listdir(dataset_path):
        if os.path.isdir(os.path.join(dataset_path, i)):
            labels.append(i)
    print(labels)

    for label in labels:
        label_dir = os.path.join(dataset_path, label)
        example_filenames = os.listdir(label_dir)[:NUM_EXAMPLES]
        fig, axs = plt.subplots(1, NUM_EXAMPLES, figsize=(10, 2))
        for i in range(NUM_EXAMPLES):
            axs[i].imshow(plt.imread(os.path.join(label_dir, example_filenames[i])))
            axs[i].get_xaxis().set_visible(False)
            axs[i].get_yaxis().set_visible(False)
        fig.suptitle(f'Showing {NUM_EXAMPLES} for {label}')
    plt.show()
