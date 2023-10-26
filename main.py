import random
import matplotlib.pyplot as plt

for sim_no in range(36):
    # Initialize all car checks to 0
    checks = [0]*10

    # Do checks every race for 18 races
    for i in range(5):
        # Generate what four cars to check
        cars_to_check = random.sample(range(0, 20), 4)
        for check_this_car in cars_to_check:
            # Check them!
            checks[check_this_car//2] += 1

    checks.sort(reverse=True)

    # Generate graph and save it
    plt.bar([i+1 for i in range(10)], checks)
    plt.ylabel("Number of checks")
    plt.xlabel("Team number")
    # plt.show()
    plt.savefig(fname=f"./graphs/out_{sim_no}.png")
    # Clear it so that you can make a new one without old data
    plt.clf()
