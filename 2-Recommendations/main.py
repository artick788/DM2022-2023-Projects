import Apriori as AP1
import AprioriFix as AP2
from utils import *
from CompareAssociationRules import plot_support, plot_confidence, plot_lift

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
    print("=====================confidence===================")
    rules = AP1.association_rules_average_confidence(transactions, MIN_SUPPORT, MIN_CONFIDENCE)
    print_rules(rules)
    print("========================Lift======================")
    rules = AP1.association_rules_lift(transactions, MIN_SUPPORT, MIN_LIFT)
    print_rules(rules)
    print("=====================conviction===================")
    rules = AP1.association_rules_conviction(transactions, MIN_SUPPORT)
    print_rules(rules)

    plot_support(transactions)
    plot_confidence(transactions)
    plot_lift(transactions)



if __name__ == "__main__":
    main()