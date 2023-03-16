from .generator import *
import numpy as np
from pathlib import Path

def normal_npz(mu, sigma, size):
    num, dims = size
    keys = generate_normal(mu, sigma, size)
    ids = get_ids(keys)
    path = f'./data/{dims}-dims-normal-{num}.npz'
    output = Path(path)
    output.parent.mkdir(exist_ok=True, parents=True)
    output.touch(exist_ok=True)
    np.savez(path, keys=keys, ids=ids)


def uniform_npz(low, high, size):
    num, dims = size
    keys = generate_uniform(low, high, size)
    ids = get_ids(keys)
    path = f'./data/{dims}-dims-uniform-{num}.npz'
    output = Path(path)
    output.parent.mkdir(exist_ok=True, parents=True)
    output.touch(exist_ok=True)
    np.savez(path, keys=keys, ids=ids)


def beta_npz(a, b, size):
    num, dims = size
    keys = generate_beta(a, b, size)
    ids = get_ids(keys)
    path = f'./data/{dims}-dims-beta-{num}.npz'
    output = Path(path)
    output.parent.mkdir(exist_ok=True, parents=True)
    output.touch(exist_ok=True)
    np.savez(path, keys=keys, ids=ids)


def exponential_npz(scale, size):
    num, dims = size
    keys = generate_exponential(scale, size)
    ids = get_ids(keys)
    path = f'./data/{dims}-dims-exponential-{num}.npz'
    output = Path(path)
    output.parent.mkdir(exist_ok=True, parents=True)
    output.touch(exist_ok=True)
    np.savez(path, keys=keys, ids=ids)


def lognormal_npz(mean, sigma, size):
    num, dims = size
    keys = generate_lognormal(mean, sigma, size)
    ids = get_ids(keys)
    path = f'./data/{dims}-dims-lognormal-{num}.npz'
    output = Path(path)
    output.parent.mkdir(exist_ok=True, parents=True)
    output.touch(exist_ok=True)
    np.savez(path, keys=keys, ids=ids)


def chisquare_npz(df, size):
    num, dims = size
    keys = generate_chisquare(df, size)
    ids = get_ids(keys)
    path = f'./data/{dims}-dims-chisquare-{num}.npz'
    output = Path(path)
    output.parent.mkdir(exist_ok=True, parents=True)
    output.touch(exist_ok=True)
    np.savez(path, keys=keys, ids=ids)