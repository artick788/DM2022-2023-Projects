import timeit
import Apriori as AP
import AprioriOptimized as APO
from AssociationRules import *
from utils import print_rules
import matplotlib.pyplot as plt
import DatasetGenerator as DG

MIN_SUPPORT = 0.2
MIN_CONFIDENCE = 0.2


def profiler():
    transactions = DG.generate_transactions()
    result: dict = {}
    print("=====================Apriori===================")
    begin = timeit.default_timer()
    frequent_itemsets, itemsets_by_length = AP.apriori(transactions, MIN_SUPPORT)
    rules = association_rules_average_confidence(transactions, frequent_itemsets, MIN_CONFIDENCE)
    end = timeit.default_timer()
    print_rules(rules)
    print("Normal apriori took: ", end - begin)
    result["apriori"] = end - begin

    print("=====================Apriori Optimized===================")
    begin = timeit.default_timer()
    frequent_itemsets, itemsets_by_length = APO.apriori_optimized(transactions, MIN_SUPPORT)
    rules = association_rules_average_confidence(transactions, frequent_itemsets, MIN_CONFIDENCE)
    end =timeit.default_timer()
    print_rules(rules)
    print("Optimized apriori took: ", end - begin)
    result["apriori_optimized"] = end - begin
    return result


if __name__ == "__main__":
    plt.figure()
    plt.title("Apriori vs Apriori Optimized")
    max_runs = 50
    runs = range(1, max_runs + 1)
    times_apriori = []
    times_apriori_optimized = []

    for i in range(max_runs):
        result = profiler()
        times_apriori.append(result["apriori"])
        times_apriori_optimized.append(result["apriori_optimized"])

    plt.plot(runs, times_apriori, label="Apriori")
    plt.plot(runs, times_apriori_optimized, label="Apriori Optimized")
    plt.xlabel("Run")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()
    avg_apriori = sum(times_apriori) / len(times_apriori)
    avg_apriori_optimized = sum(times_apriori_optimized) / len(times_apriori_optimized)
    print("Average time for apriori: ", avg_apriori)
    print("Average time for apriori optimized: ", avg_apriori_optimized)
