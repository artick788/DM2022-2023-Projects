from itertools import combinations


def generate_candidates(frequent_itemsets, k):
    candidates = set()
    for itemset1 in frequent_itemsets:
        for itemset2 in frequent_itemsets:
            union_set = itemset1.union(itemset2)
            if len(union_set) == k:
                candidates.add(union_set)
    return candidates


def prune_candidates(candidates, frequent_itemsets):
    pruned_candidates = set()
    for candidate in candidates:
        subsets = combinations(candidate, len(candidate) - 1)
        if all(subset in frequent_itemsets for subset in subsets):
            pruned_candidates.add(candidate)
    return pruned_candidates


def apriori(transactions, min_support):
    itemsets = [frozenset([item]) for transaction in transactions for item in transaction]
    frequent_itemsets = []
    min_support_count = len(transactions) * min_support

    while itemsets:
        item_counts = {}
        candidates = generate_candidates(itemsets, len(itemsets[0]) + 1)
        pruned_candidates = prune_candidates(candidates, itemsets)

        for transaction in transactions:
            for candidate in pruned_candidates:
                if candidate.issubset(transaction):
                    item_counts[candidate] = item_counts.get(candidate, 0) + 1

        frequent_itemsets.extend([itemset for itemset, count in item_counts.items() if count >= min_support_count])
        itemsets = list(frequent_itemsets)

    return frequent_itemsets