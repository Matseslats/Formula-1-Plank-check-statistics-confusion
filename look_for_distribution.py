import random

# distribution to look for
distribution = [5, 5, 2, 2, 2, 2, 1, 1, 0, 0]
exaxt = False
sims = 0
while True:
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
    sims += 1

    match = False
    if exaxt:
        match = checks == distribution
    else:
        # Only match 2x5 checks and 20 checks
        match = (checks[0] == 5 and checks[1] == 5 and checks[8] == 0 and checks[9] == 0)

    if match:
        print(f"Getting the exact distribution took {sims} simulations")
        exit()