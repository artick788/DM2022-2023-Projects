def print_rules(rules):
    for antecedent, consequent, support, confidence in rules:
        print(f"{antecedent} => {consequent} (support={support:.2f}, confidence={confidence:.2f})")


def get_support_item(transactions) -> dict:
    support_count = {}
    for transaction in transactions:
        for item in transaction:
            if item not in support_count:
                support_count[item] = 0
            support_count[item] += 1
    n_transactions = len(transactions)
    return {item: support / n_transactions for item, support in support_count.items()}
