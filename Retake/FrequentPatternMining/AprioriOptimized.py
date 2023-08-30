from itertools import chain, combinations, filterfalse
from time import time, time_ns


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def join_set(itemsets, k):
    return set(
        [itemset1.union(itemset2) for itemset1 in itemsets for itemset2 in itemsets if len(itemset1.union(itemset2)) == k]
    )


def improved_join_set(itemsets, k):
    new_itemsets = set()

    for itemset1 in itemsets:
        for itemset2 in itemsets:
            candidate = itemset1.union(itemset2)
            if len(candidate) == k:
                continue
            else:
                too_little_itemset = False
                for item in candidate:
                    subset = candidate - frozenset([item])
                    if subset not in itemsets:
                        too_little_itemset = True
                        break

                if not too_little_itemset:
                    new_itemsets.add(candidate)

    return new_itemsets

def itemsets_support(transactions, itemsets, min_support):
    support_count = {itemset: 0 for itemset in itemsets}
    for transaction in transactions:
        for itemset in itemsets:
            if itemset.issubset(transaction):
                support_count[itemset] += 1
    n_transactions = len(transactions)
    return {itemset: support / n_transactions for itemset, support in support_count.items() if support / n_transactions >= min_support}


def apriori(transactions, min_support):
    items = set(chain(*transactions))
    itemsets = [frozenset([item]) for item in items]
    itemsets_by_length = [set()]
    k = 1
    while itemsets:
        support_count = itemsets_support(transactions, itemsets, min_support)
        itemsets_by_length.append(set(support_count.keys()))
        k += 1
        itemsets = improved_join_set(itemsets, k)
    frequent_itemsets = set(chain(*itemsets_by_length))
    return frequent_itemsets, itemsets_by_length


def association_rules(transactions, min_support, min_confidence):
    frequent_itemsets, itemsets_by_length = apriori(transactions, min_support)
    rules = []
    for itemset in frequent_itemsets:
        for subset in filterfalse(lambda x: not x, powerset(itemset)):
            antecedent = frozenset(subset)
            consequent = itemset - antecedent
            support_antecedent = len([t for t in transactions if antecedent.issubset(t)]) / len(transactions)
            support_itemset = len([t for t in transactions if itemset.issubset(t)]) / len(transactions)
            confidence = support_itemset / support_antecedent
            if confidence >= min_confidence:
                rules.append((antecedent, consequent, support_itemset, confidence))
    return rules


if __name__ == "__main__":
    # Example usage
    transactions = [
{'D', 'H', 'B', 'J', 'I'} ,
{'J', 'F', 'A'} ,
{'A', 'G', 'E', 'J'} ,
{'B', 'A', 'H', 'J'} ,
{'B', 'J', 'G'} ,
{'F'} ,
{'J'} ,
{'I', 'E'} ,
{'F'} ,
{'C', 'D'} ,
{'A', 'G', 'D'} ,
{'H', 'F', 'A'} ,
{'A', 'I', 'C'} ,
{'A', 'I', 'G', 'C'} ,
{'B', 'J', 'I', 'G'} ,
{'C'} ,
{'B', 'A', 'E', 'F'} ,
{'G', 'C', 'F'} ,
{'J', 'I', 'E'} ,
{'H', 'I'} ,
{'H', 'I', 'J'} ,
{'A', 'D'} ,
{'H', 'D'} ,
{'A', 'C', 'E', 'F'} ,
{'H', 'C', 'A'} ,
{'B', 'H', 'I', 'C'} ,
{'B', 'A', 'F'} ,
{'H', 'E'} ,
{'B', 'H', 'G', 'F'} ,
{'H', 'J', 'G', 'A'} ,
{'E'} ,
{'D'} ,
{'H', 'G', 'J'} ,
{'G', 'H', 'C', 'B', 'I'} ,
{'E', 'D', 'A', 'C', 'B'} ,
{'I'} ,
{'H', 'E'} ,
{'H', 'G'} ,
{'A', 'I', 'G'} ,
{'A'} ,
{'B', 'J', 'C', 'F'} ,
{'C'} ,
{'A', 'J'} ,
{'F', 'H', 'C', 'B', 'J'} ,
{'I'} ,
{'B', 'I', 'C'} ,
{'H', 'G', 'J'} ,
{'C'} ,
{'A', 'G', 'F', 'D'} ,
{'A', 'I', 'F'} ,
{'A', 'I', 'G', 'C'} ,
{'G', 'E', 'A', 'C', 'B'} ,
{'A', 'I', 'J'} ,
{'A', 'D'} ,
{'G', 'E', 'C', 'B', 'J'} ,
{'E'} ,
{'J', 'C', 'E', 'F'} ,
{'I', 'G'} ,
{'A'} ,
{'H', 'G', 'E'} ,
{'B', 'E'} ,
{'B', 'J', 'G'} ,
{'H', 'G'} ,
{'H'} ,
{'I'} ,
{'A', 'G', 'D'} ,
{'B'} ,
{'H'} ,
{'I', 'G'} ,
{'A', 'J', 'F', 'H'} ,
{'A', 'D', 'F'} ,
{'B', 'J', 'E'} ,
{'H', 'E'} ,
{'B'} ,
{'B'} ,
{'E', 'C', 'D'} ,
{'E'} ,
{'A'} ,
{'J', 'G'} ,
{'H'} ,
{'J', 'E', 'G', 'D'} ,
{'I', 'D', 'F'} ,
{'B', 'F'} ,
{'B'} ,
{'I', 'C', 'D'} ,
{'J', 'F', 'D'} ,
{'F', 'A', 'B', 'J', 'I'} ,
{'H', 'D', 'A'} ,
{'B', 'I'} ,
{'A', 'C', 'E', 'F'} ,
{'G', 'C'} ,
{'A', 'G'} ,
{'H', 'I'} ,
{'J', 'I', 'F'} ,
{'G'} ,
{'H'} ,
{'B', 'C', 'F'} ,
{'H'} ,
{'B', 'C'} ,
{'E', 'A', 'H', 'C', 'I'} ,
]
    min_support = 0.3
    min_confidence = 0.7
    start = time_ns()
    rules = association_rules(transactions, min_support, min_confidence)
    end = time_ns()
    print(f"Time elapsed: {end - start:.6f}")
    for antecedent, consequent, support, confidence in rules:
        print(f"{antecedent} => {consequent} (support={support:.2f}, confidence={confidence:.2f})")