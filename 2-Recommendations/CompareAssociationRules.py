import Apriori as AP1
import matplotlib.pyplot as plt

MIN_SUPPORT = 0.3
MIN_CONFIDENCE = 0.7
MIN_LIFT = 1.0


def plot_support(transactions):
    supports: [float] = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.45, 0.5]
    rules_avg_confidences: [int] = []
    rules_lifts: [int] = []
    rules_convictions: [int] = []
    for support in supports:
        r1 = AP1.association_rules_average_confidence(transactions, support, MIN_CONFIDENCE)
        r2 = AP1.association_rules_lift(transactions, support, MIN_LIFT)
        r3 = AP1.association_rules_conviction(transactions, support)
        rules_avg_confidences.append(len(r1))
        rules_lifts.append(len(r2))
        rules_convictions.append(len(r3))

    plt.title("Support vs Number of rules")
    plt.plot(supports, rules_avg_confidences, label="Average Confidence")
    plt.plot(supports, rules_lifts, label="Lift")
    plt.plot(supports, rules_convictions, label="Conviction")
    plt.xlabel("Support")
    plt.ylabel("Number of rules")
    plt.legend()
    plt.show()


def plot_confidence(transactions):
    confidences: [float] = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
    rules_avg_confidences: [int] = []

    for confidence in confidences:
        r1 = AP1.association_rules_average_confidence(transactions, MIN_SUPPORT, confidence)
        rules_avg_confidences.append(len(r1))

    plt.title("Confidence vs Number of rules")
    plt.plot(confidences, rules_avg_confidences, label="Average Confidence")
    plt.xlabel("Confidence")
    plt.ylabel("Number of rules")
    plt.legend()
    plt.show()
