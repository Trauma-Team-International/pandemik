## HofstedePlus.py

# initiate the scoring
hp = HofstedePlus()

# set default weights (this makes sense only for test)
hp.set_weights()

# set randomess
hp.get_score()

# compute the score
hp.get_score()

# set custom weights and get new result
hp.set_weights(weight_uncertainty_avoidance=.2)
hp.get_score()

# set randomness factor and get new result
hp.set_randomness(factor=.03)
hp.get_score()
