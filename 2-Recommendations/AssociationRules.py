from itertools import chain, combinations, filterfalse


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def association_rules_average_confidence(transactions, frequent_itemsets, min_confidence=0.7):
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


def association_rules_lift(transactions, frequent_itemsets, min_lift=1.0):
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


def association_rules_conviction(transactions, frequent_itemsets):
    rules = []
    for itemset in frequent_itemsets:
        for subset in filterfalse(lambda x: not x, powerset(itemset)):
            antecedent = frozenset(subset)
            consequent = itemset - antecedent
            support_antecedent = len([t for t in transactions if antecedent.issubset(t)]) / len(transactions)
            support_consequent = len([t for t in transactions if consequent.issubset(t)]) / len(transactions)
            support_antecedent_consequent = len([t for t in transactions if antecedent.union(consequent).issubset(t)]) / len(transactions)
            confidence = support_antecedent_consequent / support_antecedent

            if confidence > 1:
                conviction = (1 - support_consequent) / (1 - confidence)
            elif confidence == 1:
                conviction = float('inf')
            else:
                continue

            rules.append((antecedent, consequent, support_antecedent_consequent, conviction))
    return rules