import numpy as np

def generate_normal(mu, sigma, size):
    return np.random.normal(mu, sigma, size)

def  generate_uniform(low, high, size):
    return np.random.uniform(low, high, size)

def generate_beta(a,b ,size):
    return np.random.beta(a, b, size)

def  generate_exponential(scale, size):
    return np.random.exponential(scale, size)

def generate_lognormal(mean, sigma, size):
    return np.random.lognormal(mean, sigma, size)

def generate_chisquare(df, size):
    return np.random.chisquare(df, size)

def get_ids(data):
    return np.array(range(data.shape[0])).reshape(data.shape[0], 1) +1 

def add_ids(data):
    ids = np.array(range(data.shape[0])).reshape(data.shape[0], 1) +1 
    return np.hstack((data,ids))