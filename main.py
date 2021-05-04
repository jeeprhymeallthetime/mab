from classes import *
import numpy as np
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    c = arm_tracker(num_bands=10, n_tests=500)
    # null
    print("Test results - Random: ", np.round(c.test_results_random, 2))
    print("Test results - Binomial: ", np.round(c.test_results_binomial, 2))
    print("Actual Odds: ", np.round(c.odds, 2))
    # TODO: Build 'delta-from-truth' tracker that tracks the gap between theory and actual odds of arms
    track_state_1, track_state_2 = c.track_state()
