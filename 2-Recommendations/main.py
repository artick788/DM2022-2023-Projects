import Apriori as AP1
import AprioriFix as AP2
import AprioriPruning as AP3
from utils import *
from AssociationRules import *

MIN_SUPPORT = 0.3
MIN_CONFIDENCE = 0.7
MIN_LIFT = 1.0


def main():
    transactions = [
        {"A", "B", "C"},
        {"A", "B"},
        {"A", "C", "B"},
        {"A", "B"},
        {"B", "C"},
        {"B"},
        {"C"},
    ]
    print("======================Support=====================")
    support = get_support_item(transactions)
    print(support)
    print("=====================Apriori===================")
    frequent_itemsets, itemsets_by_length = AP1.apriori(transactions, MIN_SUPPORT)
    rules = association_rules_average_confidence(transactions, frequent_itemsets, MIN_CONFIDENCE)
    print_rules(rules)
    print("=================AprioriPruning================")
    frequent_itemsets, itemsets_by_length = AP3.apriori(transactions, MIN_SUPPORT)
    rules = association_rules_average_confidence(transactions, frequent_itemsets, MIN_CONFIDENCE)
    print_rules(rules)

if __name__ == "__main__":
    main()