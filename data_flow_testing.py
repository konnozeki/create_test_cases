import pytest

import main as mn
import pandas as pd

data = pd.read_table("data_flow_test_cases.txt", sep=",", names=['Age', 'Height', 'Expected Output'])
array = data.to_numpy()


@pytest.mark.parametrize("test_input", array)
def test_sales(test_input):
    assert mn.sales(test_input[0], test_input[1]) == test_input[2]