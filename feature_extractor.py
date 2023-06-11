import pandas as pd
from typing import Tuple
"Base interface for feature extractor"

class FeatureExtractor:

    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def get_max_length(self) -> int:
        return self.data.Length.max()

    def get_min_length(self) -> int:
        return self.data.Length.min()

    def get_avg_length(self) -> int:
        return self.data.Length.mean()

    def is_data_msg(self):
        self.data["is_data_msg"] = 0
        self.data.loc[
            self.data["Info"].str.lower().str.startswith("data"),
            "is_data_msg"] = 1
        
    def time_diff(self):
        self.data["time_diff"] = self.data.Time.diff()

    def is_dio_msg(self):
        dio_msg = "RPL Control (DODAG Information Object)"
        self.data["is_dio_msg"] = 0
        self.data.loc[
            self.data["Info"]== dio_msg,
            "is_dio_msg"] = 1

    def is_dao_msg(self):
        dao_msg = "RPL Control (Destination Advertisement Object)"
        self.data["is_dao_msg"] = 0
        self.data.loc[
            self.data["Info"]==dao_msg,
            "is_dao_msg"] = 1

    def is_dis_msg(self):
        dis_msg = "RPL Control (DODAG Information Solicitation)"
        self.data["is_dis_msg"] = 0
        self.data.loc[
            self.data["Info"]==dis_msg,
            "is_dis_msg"] = 1

    def get_num_msgs(self) -> int:
        self.is_data_msg()
        return self.data.is_data_msg.sum()

    def get_max_delta(self) -> float:
        return self.data.time_diff.max()

    def get_min_delta(self) -> float:
        return self.data.time_diff.min()

    def get_avg_delta(self) -> float:
        return self.data.time_diff.mean()

    def get_num_dio(self) -> int:
        self.is_dio_msg()
        return self.data.is_dio_msg.sum()

    def get_num_dis(self) -> int:
        self.is_dis_msg()
        return self.data.is_dis_msg.sum()

    def get_num_dao(self) -> int:
        self.is_dao_msg()
        return self.data.is_dao_msg.sum()

    def get_dio_delta(self) -> Tuple[float, float, float]:
        dio_data = self.data[self.data.is_dio_msg==1]
        dio_data["dio_delta"] = dio_data.Time.diff()
        return (dio_data.dio_delta.max(),
                dio_data.dio_delta.min(),
                dio_data.dio_delta.mean())

    def get_dis_delta(self) -> Tuple[float, float, float]:
        dis_data = self.data[self.data.is_dis_msg==1]
        dis_data["dis_delta"] = dis_data.Time.diff()
        return (dis_data.dis_delta.max(),
                dis_data.dis_delta.min(),
                dis_data.dis_delta.mean())

    def get_dao_delta(self) -> Tuple[float, float, float]:
        dao_data = self.data[self.data.is_dao_msg==1]
        dao_data["dao_delta"] = dao_data.Time.diff()
        return (dao_data.dao_delta.max(),
                dao_data.dao_delta.min(),
                dao_data.dao_delta.mean())
