from AssociationRules import association_rules, association_rules_ext, association_rules_ndi
from AprioriOptimized import association_rules as association_rules_optimized
from time import time, time_ns
from Transactions import transactions, transactions_1, transactions_2
from Dataset import Dataset
from EvaluateRecommendations import evaluate_recommendations, evaluate_recommendations_ext
import matplotlib.pyplot as plt
from NDI import generate_ndi, read_ndi, SUPPORTS


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

    results: dict = {
        'confidence': {
            'precision': [],
            'recall': [],
            'f1': []
        },
        'lift': {
            'precision': [],
            'recall': [],
            'f1': []
        },
        'conviction': {
            'precision': [],
            'recall': [],
            'f1': []
        },
        'leverage': {
            'precision': [],
            'recall': [],
            'f1': []
        },
        'jaccard_similarity': {
            'precision': [],
            'recall': [],
            'f1': []
        }
    }

    confidences = [0.01, 0.05, 0.1, 0.3, 0.4, 0.5, 0.6, 0.7]
    for min_confidence in confidences:
        rules = association_rules_ext(train, 0.005, min_confidence, use_optimized=True)
        for ranking_method in ['confidence', 'lift', 'conviction', 'leverage', 'jaccard_similarity']:
            precision, recall, f1 = evaluate_recommendations_ext(validate, user_items, rules, ranking_method)
            print(f"min_confidence={min_confidence:.3f}, ranking_method={ranking_method}, precision={precision:.3f}, recall={recall:.3f}, f1={f1:.3f}")
            results[ranking_method]['precision'].append(precision)
            results[ranking_method]['recall'].append(recall)
            results[ranking_method]['f1'].append(f1)

    # plot graphs
    for metric in ['precision', 'recall', 'f1']:
        plt.figure()
        plt.title(metric)
        plt.plot(confidences, results['confidence'][metric], label='confidence', marker='o')
        plt.plot(confidences, results['lift'][metric], label='lift', marker='o')
        plt.plot(confidences, results['conviction'][metric], label='conviction', marker='o')
        plt.plot(confidences, results['leverage'][metric], label='leverage', marker='o')
        plt.plot(confidences, results['jaccard_similarity'][metric], label='jaccard_similarity', marker='o')
        plt.xlabel('min_confidence')
        plt.ylabel(metric)
        plt.legend()
        plt.savefig(f"task_2_{metric}.png")
        plt.close()


def task_3():
    d = Dataset("data/retail_small.dat")
    train, validate, user_items = d.split_dataset()

    results: dict = {
        'precision': [],
        'recall': [],
        'f1': []
    }

    for min_support in SUPPORTS:
        rules = association_rules_ndi(train, min_support, 0.01, file_name=f"data/bf_{min_support}.dat")
        precision, recall, f1 = evaluate_recommendations_ext(validate, user_items, rules, 'confidence')
        print(f"min_support={min_support:.3f}, precision={precision:.3f}, recall={recall:.3f}, f1={f1:.3f}")
        results['precision'].append(precision)
        results['recall'].append(recall)
        results['f1'].append(f1)

    # plot graphs
    for metric in ['precision', 'recall', 'f1']:
        plt.figure()
        plt.title(metric)
        plt.plot(SUPPORTS, results[metric], label='avg_confidence', marker='o')
        plt.xlabel('min_support')
        plt.ylabel(metric)
        plt.legend()
        plt.savefig(f"task_3_{metric}.png")
        plt.close()



if __name__ == "__main__":
    print("=================== Task 1 ===================")
    task_1()
    print("=================== Task 2 ===================")
    task_2()
    print("=================== Task 3 ===================")
    task_3()
