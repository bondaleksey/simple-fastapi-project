import os

import joblib


__all__ = ["store", "load"]


def store(data, filename="baseline", path="default"):
    if path == "default":
        path = models_path()
    filepath = os.path.join(path, filename + ".joblib")

    joblib.dump(data, filepath)


def load(filename="baseline", path="default"):
    if path == "default":
        path = models_path()
    filepath = os.path.join(path, filename + ".joblib")

    return joblib.load(filepath)


def models_path() -> str:
    script_path = os.path.abspath(__file__)
    script_dir_path = os.path.dirname(script_path)
    models_folder = os.path.join(script_dir_path, "..", "..", "..", "models")
    return models_folder
