import Apriori as AP1
import AprioriFix as AP2
import AprioriPruning as AP3
from utils import *
from AssociationRules import *

MIN_SUPPORT = 0.3
MIN_CONFIDENCE = 0.5
MIN_LIFT = 1.0


def main():
    transactions = [
        {"A", "B", "C"},
        {"A", "B"},
        {"A", "C", },
        {"A", },
        {"B", "C"},
        {"B"},
        {"C"},
    ]
    transactions = [
        {1, 3, 4},
        {2, 3, 5},
        {1, 2, 3, 5},
        {2, 5},
        {1, 3, 5},
    ]
    print("======================Support=====================")
    support = get_support_item(transactions)
    print(support)
    print("=====================Apriori===================")
    frequent_itemsets, itemsets_by_length = AP1.apriori(transactions, MIN_SUPPORT)
    rules = association_rules_average_confidence(transactions, frequent_itemsets, MIN_CONFIDENCE)
    print_rules(rules)
    # print("=================AprioriPruning================")
    # frequent_itemsets, itemsets_by_length = AP1.apriori(transactions, MIN_SUPPORT)
    # rules = association_rules_average_confidence(transactions, frequent_itemsets, MIN_CONFIDENCE)
    # print_rules(rules)


if __name__ == "__main__":
    main()