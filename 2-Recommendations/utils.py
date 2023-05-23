def print_rules(rules):
    for i in rules:
        antecedent = i["antecedent"]
        consequent = i["consequent"]
        formatted_string = f"{antecedent} => {consequent} "
        if "support" in i:
            support = i["support"]
            formatted_string += f"(support={support:.2f}"
        if "confidence" in i:
            confidence = i["confidence"]
            formatted_string += f", confidence={confidence:.2f}"
        if "lift" in i:
            lift = i["lift"]
            formatted_string += f", lift={lift:.2f}"
        if "conviction" in i:
            conviction = i["conviction"]
            formatted_string += f", conviction={conviction:.2f}"
        print(formatted_string)


def get_support_item(transactions) -> dict:
    support_count = {}
    for transaction in transactions:
        for item in transaction:
            if item not in support_count:
                support_count[item] = 0
            support_count[item] += 1
    n_transactions = len(transactions)
    return {item: support / n_transactions for item, support in support_count.items()}
