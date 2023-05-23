from itertools import chain, combinations, filterfalse


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def join_set(itemsets, k):
    return set(
        [itemset1.union(itemset2) for itemset1 in itemsets for itemset2 in itemsets if len(itemset1.union(itemset2)) == k]
    )


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
        itemsets = join_set(itemsets, k)
    frequent_itemsets = set(chain(*itemsets_by_length))
    return frequent_itemsets, itemsets_by_length


def association_rules_average_confidence(transactions, min_support=0.3, min_confidence=0.7):
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


def association_rules_lift(transactions, min_support=0.3, min_lift=1.0):
    frequent_itemsets, itemsets_by_length = apriori(transactions, min_support)
    rules = []
    for itemset in frequent_itemsets:
        for subset in filterfalse(lambda x: not x, powerset(itemset)):
            antecedent = frozenset(subset)
            consequent = itemset - antecedent
            support_antecedent = len([t for t in transactions if antecedent.issubset(t)]) / len(transactions)
            support_consequent = len([t for t in transactions if consequent.issubset(t)]) / len(transactions)
            support_antecedent_consequent = len([t for t in transactions if antecedent.union(consequent).issubset(t)]) / len(transactions)
            lift = support_antecedent_consequent / (support_antecedent * support_consequent)

            if lift > min_lift:
                rules.append((antecedent, consequent, support_antecedent_consequent, lift))
    return rules


def association_rules_conviction(transactions, min_support=0.3):
    frequent_itemsets, itemsets_by_length = apriori(transactions, min_support)
    rules = []
    for itemset in frequent_itemsets:
        for subset in filterfalse(lambda x: not x, powerset(itemset)):
            antecedent = frozenset(subset)
            consequent = itemset - antecedent
            support_antecedent = len([t for t in transactions if antecedent.issubset(t)]) / len(transactions)
            support_consequent = len([t for t in transactions if consequent.issubset(t)]) / len(transactions)
            support_antecedent_consequent = len([t for t in transactions if antecedent.union(consequent).issubset(t)]) / len(transactions)
            confidence = support_antecedent_consequent / support_antecedent

            if confidence != 1:
                conviction = (1 - support_consequent) / (1 - confidence)
            else:
                conviction = float('inf')

            rules.append((antecedent, consequent, support_antecedent_consequent, conviction))
    return rules

