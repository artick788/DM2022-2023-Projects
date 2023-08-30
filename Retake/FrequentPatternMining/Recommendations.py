from Apriori import association_rules, association_rules_ext


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


def recommend_items_ext(input_items, rules, ranking_method='confidence', top_n=5):
    # the rules are sorted by confidence, lift, conviction, leverage, jaccard_similarity, this map is used to get the
    # index of the ranking method in the tuple, stupid but it works
    ranking_index = {'confidence': 0, 'lift': 1, 'conviction': 2, 'leverage': 3, 'jaccard_similarity': 4}

    recommendations = {}
    for antecedent, consequent, support, confidence, lift, conviction, leverage, jaccard_similarity in rules:
        if antecedent.issubset(input_items) and not consequent.issubset(input_items):
            for item in consequent:
                if item not in input_items:
                    if item not in recommendations:
                        recommendations[item] = []
                    ranking_value = (confidence, lift, conviction, leverage, jaccard_similarity)[
                        ranking_index[ranking_method]]
                    recommendations[item].append((ranking_value, support))

    recommendations = {
        item: (sum(ranking for ranking, _ in item_rules) / len(item_rules),
               sum(sup for _, sup in item_rules) / len(item_rules))
        for item, item_rules in recommendations.items()
    }
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: (-x[1][0], -x[1][1]))
    return [item for item, _ in sorted_recommendations[:top_n]]


if __name__ == '__main__':
    input_items = {"A", "B"}
    transactions = [
        {"A", "B", "C"},
        {"A", "B"},
        {"A", "C"},
        {"A"},
        {"B", "C"},
        {"B"},
        {"C"},
    ]
    min_support = 0.1
    min_confidence = 0.3
    rules = association_rules_ext(transactions, min_support, min_confidence)
    recommended_items = recommend_items_ext(input_items, rules, 'jaccard_similarity', top_n=5)
    print("Recommended items:", recommended_items)