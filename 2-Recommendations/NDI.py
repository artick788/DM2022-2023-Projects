from AssociationRules import association_rules_average_confidence, association_rules_lift, association_rules_conviction
from DataProcessor import Dataset
from AprioriOptimized import apriori_optimized


def recommend_items(input_items, rules, top_n=5):
    recommendations = {}
    for antecedent, consequent, support, confidence in rules:
        if antecedent.issubset(input_items) and not consequent.issubset(input_items):
            for item in consequent:
                if item not in input_items:
                    if item not in recommendations:
                        recommendations[item] = []
                    recommendations[item].append((confidence, support))

    recommendations = {
        item: (sum(conf for conf, _ in item_rules) / len(item_rules), sum(sup for _, sup in item_rules) / len(item_rules))
        for item, item_rules in recommendations.items()
    }
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: (-x[1][0], -x[1][1]))
    return [item for item, _ in sorted_recommendations[:top_n]]


def test_ndi():
    min_support = 0.0001
    min_confidence = 0.0001
    min_lift = 1.0

    input_items = {"365", "1150", "86"}

    ds = Dataset("NonDerivableItemsets/data/custom_retail.dat", "NonDerivableItemsets/bf_out.txt")

    rules = association_rules_average_confidence(ds.transactions, ds.itemsets, min_confidence)
    recommended_items = recommend_items(input_items, rules)
    print("Recommended items (NDI):", recommended_items)

    frequent_itemsets, itemsets_by_length = apriori_optimized(ds.transactions, min_support)
    rules = association_rules_average_confidence(ds.transactions, frequent_itemsets, min_lift)
    recommended_items = recommend_items(input_items, rules)
    print("Recommended items (Apriori):", recommended_items)


if __name__ == "__main__":
    test_ndi()