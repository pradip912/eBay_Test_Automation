import os
from behave.__main__ import main as behave_main

if __name__ == "__main__":
    feature_path = os.path.join(os.path.dirname(__file__), "../features")
    behave_main(feature_path)
