from Apriori import apriori
from AssociationRules import association_rules_average_confidence, association_rules_lift, association_rules_conviction


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


def evaluate_recommendations(test_data, user_items, rules, top_n=5):
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    for user, true_items in test_data.items():
        # Assuming user_items is a dictionary with user IDs as keys and their associated items as values
        input_items = user_items[user]
        # Get recommendations for the user
        recommended_items = set(recommend_items(input_items, rules, top_n=top_n))
        true_items = set(true_items)
        true_positives += len(recommended_items.intersection(true_items))
        false_positives += len(recommended_items - true_items)
        false_negatives += len(true_items - recommended_items)
    # Calculate precision, recall, and F1 score
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return precision, recall, f1_score


def test_recommendations():
    input_items = {"A", "B", "E"}
    transactions = [
        {'C', 'A', 'B'},
        {'C', 'A', 'D', 'E'},
        {'C', 'A', 'B'},
        {'A', 'D', 'B'},
        {'C', 'A', 'E'},
        {'C', 'A', 'D'},
        {'A', 'B'},
        {'C', 'B', 'D', 'E'},
        {'C', 'B'},
        {'B', 'E'},
        {'A', 'B'},
    ]
    min_support = 0.2
    min_confidence = 0.5
    min_lift = 1.0

    frequent_itemsets, itemsets_by_length = apriori(transactions, min_support)

    rules = association_rules_average_confidence(transactions, frequent_itemsets, min_confidence)
    recommended_items = recommend_items(input_items, rules)
    print("Recommended items (confidence):", recommended_items)

    rules = association_rules_lift(transactions, frequent_itemsets, min_lift)
    recommended_items = recommend_items(input_items, rules)
    print("Recommended items (lift)      :", recommended_items)

    rules = association_rules_conviction(transactions, frequent_itemsets)
    recommended_items = recommend_items(input_items, rules)
    print("Recommended items (conviction):", recommended_items)


if __name__ == "__main__":
    test_recommendations()