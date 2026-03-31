import pickle

def save_file(obj, filename):
    with open(filename, "wb") as f:
        pickle.dump(obj, f)

def load_file(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
