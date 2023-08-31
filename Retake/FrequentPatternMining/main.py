from AssociationRules import association_rules, association_rules_ext
from AprioriOptimized import association_rules as association_rules_optimized
from time import time, time_ns
from Transactions import transactions, transactions_1, transactions_2
from Dataset import Dataset
from EvaluateRecommendations import evaluate_recommendations, evaluate_recommendations_ext


def print_rules(rules):
    for antecedent, consequent, support, confidence in rules:
        print(f"{antecedent} => {consequent} (support={support:.2f}, confidence={confidence:.2f})")


def task_1():
    min_support = 0.3
    min_confidence = 0.7
    times_default = []
    times_optimized = []
    for i in range(10):
        start = time()
        rules = association_rules(transactions_1, min_support, min_confidence)
        end = time()
        elapsed = end - start
        times_default.append(elapsed)
        print(f"Time elapsed for Apriori: {elapsed:.6f}")
        for antecedent, consequent, support, confidence in rules:
            print(f"{antecedent} => {consequent} (support={support:.2f}, confidence={confidence:.2f})")

        start = time()
        rules = association_rules_optimized(transactions_1, min_support, min_confidence)
        end = time()
        elapsed = end - start
        times_optimized.append(elapsed)
        print(f"Time elapsed for AprioriOptimized: {end - start:.6f}")
        for antecedent, consequent, support, confidence in rules:
            print(f"{antecedent} => {consequent} (support={support:.2f}, confidence={confidence:.2f})")

    print(f"Average time for Apriori: {sum(times_default) / len(times_default):.6f}")
    print(f"Average time for AprioriOptimized: {sum(times_optimized) / len(times_optimized):.6f}")


def task_2():
    d = Dataset("data/retail_small.dat")
    train, validate, user_items = d.split_dataset()

    for min_confidence in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.5]:
        rules = association_rules_ext(train, 0.005, min_confidence, use_optimized=True)
        for ranking_method in ['confidence', 'lift', 'conviction', 'leverage', 'jaccard_similarity']:
            precision, recall, f1 = evaluate_recommendations_ext(validate, user_items, rules, ranking_method)
            print(f"min_confidence={min_confidence:.3f}, ranking_method={ranking_method}, precision={precision:.3f}, recall={recall:.3f}, f1={f1:.3f}")



if __name__ == "__main__":
    task_2()