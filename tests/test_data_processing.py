import pytest
import pandas as pd
import numpy as np

class TestDataValidation:
    """Tests to verify data is clean and valid"""
    
    def test_dataset_loads(self):
        """Test that we can load a dataset"""
        df = pd.DataFrame({
            'order_id': [1, 2, 3],
            'order_value': [100.50, 200.75, 150.25],
            'delivery_days': [5, 10, 7]
        })
        
        assert len(df) == 3, "Dataset should have 3 rows"
        assert df.shape[1] == 3, "Dataset should have 3 columns"
    
    def test_no_negative_values(self):
        """Order values should never be negative"""
        df = pd.DataFrame({
            'order_value': [100, 200, 300]
        })
        
        assert (df['order_value'] > 0).all(), "Order values must be positive"
    
    def test_numeric_columns(self):
        """Numeric columns should be numbers, not text"""
        df = pd.DataFrame({
            'order_value': [100, 200, 300],
            'delivery_days': [5, 10, 7]
        })
        
        assert df['order_value'].dtype in [np.float64, np.int64]
        assert df['delivery_days'].dtype in [np.float64, np.int64]
