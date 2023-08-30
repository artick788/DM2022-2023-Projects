from Apriori import association_rules
from AprioriOptimized import association_rules as association_rules_optimized
from time import time, time_ns
from Transactions import transactions, transactions_1, transactions_2

if __name__ == "__main__":
    # Example usage

    min_support = 0.3
    min_confidence = 0.7
    start = time()
    rules = association_rules(transactions_2, min_support, min_confidence)
    end = time()
    print(f"Time elapsed for Apriori: {end - start:.6f}")
    for antecedent, consequent, support, confidence in rules:
        print(f"{antecedent} => {consequent} (support={support:.2f}, confidence={confidence:.2f})")

    start = time_ns()
    rules = association_rules_optimized(transactions_2, min_support, min_confidence)
    end = time_ns()
    print(f"Time elapsed for AprioriOptimized: {end - start:.6f}")
    for antecedent, consequent, support, confidence in rules:
        print(f"{antecedent} => {consequent} (support={support:.2f}, confidence={confidence:.2f})")