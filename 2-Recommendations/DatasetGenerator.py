import random


def generate_transactions(items=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], num_transactions=100, max_items_per_transaction=5) -> [set]:
    transactions: [set] = []

    for _ in range(num_transactions):
        transaction = set()
        for _ in range(random.randint(3, max_items_per_transaction)):
            transaction.add(random.choice(items))
        transactions.append(transaction)

    return transactions


if __name__ == "__main__":
    transactions = generate_transactions(["A", "B", "C", "D", "E",], 20, 4)
    with open("transactions.py", "w") as f:
        f.write("transactions = [\n")
        for t in transactions:
            f.write("    " + str(t) + ",\n")
            print(t)
        f.write("]\n")