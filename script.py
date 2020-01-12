def main():
    prob_a1 = float(input("What is the probability of A1? "))
    prob_a2 = 1 - prob_a1

    prob_b_a1 = float(input("What is the probability of B given A1? "))
    prob_b_a2 = 1 - prob_b_a1

    prob_a1_b = (prob_a1 * prob_b_a1) / ((prob_a1 * prob_b_a1) + (prob_a2 * prob_b_a2))
    print(prob_a1_b)

main()