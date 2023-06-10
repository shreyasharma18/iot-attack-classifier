import pandas as pd
"Base interface for feature extractor"

class FeatureExtractor:

    def __init__(self, data: pd.DataFrame) -> None:
        pass

    def get_max_length(self) -> int:
        pass

    def get_min_length(self) -> int:
        pass

    def get_avg_length(self) -> int:
        pass

    def get_num_msgs(self) -> int:
        pass

    def get_max_delta(self) -> int:
        pass

    def get_min_delta(self) -> int:
        pass

    def get_avg_delta(self) -> int:
        pass

    def get_num_dio(self) -> int:
        pass

    def get_num_dis(self) -> int:
        pass

    def get_num_dao(self) -> int:
        pass

