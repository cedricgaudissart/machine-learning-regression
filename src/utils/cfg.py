# -----------------------------------------------------------------------------
# IMPORT PACKAGES
# -----------------------------------------------------------------------------

import os
from dotenv import load_dotenv
load_dotenv()


# -----------------------------------------------------------------------------
# DEFINE CLASS
# -----------------------------------------------------------------------------

class Config():
    def __init__(self):
        # Paths
        self.train_data_path = os.getenv("TRAIN_DATA_PATH")
        self.test_data_path = os.getenv("TEST_DATA_PATH")
        self.data_profiling_dashboard_path = (
            os.getenv("DATA_PROFILING_DASHBOARD_PATH")
        )
        
        # Model Parameters
        self.imputation_strategy = "iterative"
        self.outlier_detection_method = "isolation_forest"
        
        # Feature Engineering
        self.create_interactions = True
        self.create_ratios = True
        
        # Normalization
        self.normalization_method = "minmax"

