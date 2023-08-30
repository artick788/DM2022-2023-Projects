from Apriori import association_rules
from AprioriOptimized import association_rules as association_rules_optimized
from time import time, time_ns
from Transactions import transactions, transactions_1, transactions_2


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

if __name__ == "__main__":
    task_1()