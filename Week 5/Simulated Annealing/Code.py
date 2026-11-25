import math
import random

# Objective function
def objective(x):
    return x * x + 4 * math.sin(5 * x)

# Simulated Annealing Algorithm
def simulated_annealing():
    current = random.uniform(-5, 5)
    temperature = 100
    cooling_rate = 0.8
    step = 1

    print("Initial Solution:", round(current, 4))
    print("Initial Cost:", round(objective(current), 4))
    print("\nSteps:\n")

    while temperature > 1:

        new = current + random.uniform(-1, 1)
        change = objective(new) - objective(current)

        if change < 0:
            current = new
            decision = "Accepted (Better solution)"
        elif random.random() < math.exp(-change / temperature):
            current = new
            decision = "Accepted (Probability)"
        else:
            decision = "Rejected"

        print("Step:", step)
        print("Temperature:", round(temperature, 4))
        print("New Solution:", round(new, 4))
        print("New Cost:", round(objective(new), 4))
        print("Decision:", decision)
        print("Current Solution:", round(current, 4))
        print("--------------------------------")

        temperature *= cooling_rate
        step += 1

    print("\nFinal Solution:", round(current, 4))
    print("Minimum Cost:", round(objective(current), 4))


# Run the algorithm
simulated_annealing()
