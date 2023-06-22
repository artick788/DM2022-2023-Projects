import threading


class Dataset:
    def __init__(self, transaction_file, itemset_file):
        self.itemsets: [frozenset] = []
        self.transactions: [frozenset] = []

        t1 = threading.Thread(target=self.read_transactions, args=(transaction_file,))
        t2 = threading.Thread(target=self.read_itemsets, args=(itemset_file,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()


    def read_transactions(self, transaction_file):
        with open(transaction_file, "r") as f:
            for line in f:
                self.transactions.append(frozenset(line.split(" ")))

    def read_itemsets(self, itemsets_file):
        with open(itemsets_file, "r") as f:
            for line in f:
                numbers = []
                for number in line.split():
                    if number.startswith('(') or number.startswith('['):
                        break
                    numbers.append(number)
                self.itemsets.append(frozenset(numbers))