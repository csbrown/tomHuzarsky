from scipy.stats import norm

# Somebody claims that their product has a click-through rate of 2%
#hypothetical = norm(loc = 0.02, scale = 0.001)

# We test that by taking a sample
our_sample_mean = 0.01
our_sample_std_dev = 0.007
our_sample_size = 100
std_dev_for_sampling_distribution_of_the_mean = our_sample_std_dev / math.sqrt(our_sample_size - 1)

hypothetical = norm(loc = 0.02, scale = std_dev_for_sampling_distribution_of_the_mean)

# t-distribution looks a whole lot like the normal distribution.... We should be using it instead.

print hypothetical.cdf(our_sample_mean)


# Fancy formula for our std dev to use
# std_dev_for_sampling_distribution_of_the_mean = our_sample_std_dev / sqrt(n - 1)  JUST FOR HYPOTHESIS TEST ON A MEAN




