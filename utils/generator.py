import numpy as np

def  generate_uniform(low, high, size):
    data = np.random.uniform(low, high, size)
    return np.unique(data)

def generate_normal(mu, sigma, size):
    data = np.random.normal(mu, sigma, size)
    return np.unique(data)

def generate_beta(a,b ,size):
    data = np.random.beta(a, b, size)
    return np.unique(data)


def  generate_exponential(scale, size):
    data = np.random.exponential(scale, size)
    return np.unique(data)

def generate_lognormal(mean, sigma, size):
    data = np.random.lognormal(mean, sigma, size)
    return np.unique(data)

def generate_chisquare(df, size):
    data = np.random.chisquare(df, size)
    return np.unique(data)

def get_ids(data):
    return np.array(range(data.shape[0])).reshape(data.shape[0], 1) +1 

def add_ids(data):
    ids = np.array(range(data.shape[0])).reshape(data.shape[0], 1) +1 
    return np.hstack((data,ids))