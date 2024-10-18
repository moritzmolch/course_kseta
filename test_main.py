import numpy as np
import pytest
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_DIR)

from main import load_data, plot

TEST_DATA = os.path.join(PROJECT_DIR, "data.csv")


def test_load_data():
    data = load_data(TEST_DATA)
    assert data.shape[0] == 200
    assert data.shape[1] == 2


def test_plot():
    output_path = "test_plot.png"
    if os.path.exists(output_path):
        os.remove(output_path)
    data = np.random.normal(size=(80, 2))
    plot(data, output_path)
    assert os.path.exists(output_path)
