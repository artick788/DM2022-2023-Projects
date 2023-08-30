import Apriori as AP1
from utils import *
from AssociationRules import *

MIN_SUPPORT = 0.41
MIN_CONFIDENCE = 0.5
MIN_LIFT = 1.0


def test_apriori():
    transactions = [
        {'A', 'B', 'C'},
        {'A', 'B', 'C', 'D'},
        {'B', 'C', 'D', 'E'},
        {'A', 'C', 'D', 'E'},
        {'D', 'E'},
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
    test_apriori()
