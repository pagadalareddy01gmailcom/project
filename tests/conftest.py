import pytest
import pandas as pd
import numpy as np

@pytest.fixture
def sample_dataset():
    """Sample dataset for testing"""
    return pd.DataFrame({
        'order_id': [1, 2, 3, 4, 5],
        'order_value': [100, 150, 200, 250, 300],
        'delivery_days': [5, 7, 10, 12, 15],
        'customer_rating': [4.5, 4.0, 5.0, 3.5, 4.8]
    })

@pytest.fixture
def random_seed():
    """Set reproducible random seed"""
    np.random.seed(42)
    return 42
