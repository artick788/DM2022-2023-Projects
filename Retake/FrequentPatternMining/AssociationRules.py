from itertools import chain, combinations, filterfalse
from Apriori import powerset, apriori
from AprioriOptimized import apriori as apriori_optimized
from NDI import read_ndi


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


def association_rules_ext(transactions, min_support, min_confidence, use_optimized=False):
    if use_optimized:
        frequent_itemsets, itemsets_by_length = apriori_optimized(transactions, min_support)
    else:
        frequent_itemsets, itemsets_by_length = apriori(transactions, min_support)

    rules = []
    for itemset in frequent_itemsets:
        for subset in filterfalse(lambda x: not x, powerset(itemset)):
            antecedent = frozenset(subset)
            consequent = itemset - antecedent
            support_antecedent = len([t for t in transactions if antecedent.issubset(t)]) / len(transactions)
            support_itemset = len([t for t in transactions if itemset.issubset(t)]) / len(transactions)
            confidence = support_itemset / support_antecedent
            lift = support_itemset / (support_antecedent * len(transactions))
            if confidence == 1:  # Handle division by zero for conviction
                conviction = float('inf')  # Set conviction to infinity
            else:
                conviction = (1 - support_itemset) / (1 - confidence)
            leverage = support_itemset - (support_antecedent * len(transactions))
            jaccard_similarity = len(antecedent.intersection(consequent)) / len(antecedent.union(consequent))

            if confidence >= min_confidence and len(consequent) > 0:
                rules.append((antecedent, consequent, support_itemset, confidence, lift, conviction, leverage,
                              jaccard_similarity))
    return rules


def association_rules_ndi(transactions, min_support, min_confidence, file_name):
    frequent_itemsets, itemsets_by_length = read_ndi(file_name)

    rules = []
    for itemset in frequent_itemsets:
        for subset in filterfalse(lambda x: not x, powerset(itemset)):
            antecedent = frozenset(subset)
            consequent = itemset - antecedent
            support_antecedent = len([t for t in transactions if antecedent.issubset(t)]) / len(transactions)
            support_itemset = len([t for t in transactions if itemset.issubset(t)]) / len(transactions)
            confidence = support_itemset / support_antecedent
            lift = support_itemset / (support_antecedent * len(transactions))
            if confidence == 1:  # Handle division by zero for conviction
                conviction = float('inf')  # Set conviction to infinity
            else:
                conviction = (1 - support_itemset) / (1 - confidence)
            leverage = support_itemset - (support_antecedent * len(transactions))
            jaccard_similarity = len(antecedent.intersection(consequent)) / len(antecedent.union(consequent))

            if confidence >= min_confidence and len(consequent) > 0:
                rules.append((antecedent, consequent, support_itemset, confidence, lift, conviction, leverage,
                              jaccard_similarity))
    return rules