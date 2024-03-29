from itertools import chain, combinations, filterfalse
from time import time, time_ns


def powerset(iterable):
    # generate a powerset of the iterable
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def join_set_prune(itemsets, k):
    new_itemsets = set()

    for itemset1 in itemsets:
        for itemset2 in itemsets:
            candidate = itemset1.union(itemset2)
            if len(candidate) != k:
                continue
            else:
                pruned_much = False
                for item in candidate:
                    subset = candidate - frozenset([item])
                    if subset not in itemsets:
                        pruned_much = True
                        break

                if not pruned_much:
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
    # perform the apriori algorithm
    items = set(chain(*transactions))
    itemsets = [frozenset([item]) for item in items]
    itemsets_by_length = [set()]
    k = 1
    while itemsets:
        # get candidates with minimum support
        support_count = itemsets_support(transactions, itemsets, min_support)
        itemsets_by_length.append(set(support_count.keys()))
        itemsets = list(support_count.keys())
        k += 1

        itemsets = join_set_prune(itemsets, k)

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
