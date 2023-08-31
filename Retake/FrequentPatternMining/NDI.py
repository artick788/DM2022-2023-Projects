import os


SUPPORTS = [10, 20, 30, 40, 50, 60, 70, 100, 200]


def generate_ndi(ndi_type: str = 'bf', support: int = 10):
    os.system(
        f'ndi\\cmake-build-release\\{ndi_type}.exe data/retail_small.dat {support} 3 data/{ndi_type}_{support}.dat'
    )


def read_ndi(file_name: str):
    with open(file_name, 'r') as f:
        lines = f.readlines()[1:]

    ls_of_freq_itemsets = [set(line.split(" (")[0].split()) for line in lines]

    new_ls_of_freq_itemsets = []
    for freq_itemset in ls_of_freq_itemsets:
        new_ls_of_freq_itemsets.append(
            frozenset([item for item in freq_itemset]))

    itemsets_by_length = dict()
    for itemset in new_ls_of_freq_itemsets:
        if len(itemset) not in itemsets_by_length:
            itemsets_by_length[len(itemset)] = set()
        itemsets_by_length[len(itemset)].add(itemset)

    return new_ls_of_freq_itemsets, list(itemsets_by_length.values())


if __name__ == '__main__':
    for ndi in ['bf', 'df']:
        for support in SUPPORTS:
            print(f'Generating {ndi}_{support}.dat')
            generate_ndi(ndi, support)