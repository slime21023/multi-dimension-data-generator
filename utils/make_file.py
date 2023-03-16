from .generator import *
import numpy as np
from pathlib import Path



def normal_npz(mu, sigma, size):
    num, dims = size
    keys = generate_normal(mu, sigma, size)
    ids = get_ids(keys)
    path = f'{dims}-dims-normal-{num}.npz'
    Path(path).touch(exist_ok=True)
    np.savez(path, keys=keys, ids=ids)
