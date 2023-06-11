import os
from os.path import join, isfile
import sys
import json
import argparse
import logging
import pandas as pd
from typing import List
from feature_extractor import FeatureExtractor
from data import DataFields

class DataLoader:

    def __init__(self, csv_path) -> None:
        # path to csv files
        self.path = csv_path

    @staticmethod
    def _filter_readable_files(self, files) -> List[str]:
        readable_files = [f for f in files \
                if isfile(join(self.path, f))]
        return readable_files

    @staticmethod
    def _filter_csv_files(files) -> List[str]:
        csv_files = [f for f in files if f.endswith('.csv')]
        return csv_files

    def _fetch_data_src(self) -> List[str]:
        # fetch all files and return relevant
        # csv files
        files = os.listdir(self.path)
        readable_files = self._filter_readable_files(files)
        csv_files = self._filter_csv_files(readable_files)
        return [join(self.path, f) for f in csv_files]
    
    def extract_features(self, df: pd.DataFrame) -> pd.DataFrame:
        fe = FeatureExtractor(df)
        fe.is_data_msg()
        fe.is_dio_msg()
        fe.is_dis_msg()
        fe.is_dao_msg()
        dio_deltas = fe.get_dio_delta()
        dao_deltas = fe.get_dao_delta()
        dis_deltas = fe.get_dis_delta()
        data = DataFields(
            fe.get_max_length(),
            fe.get_min_length(),
            fe.get_avg_length(),
            fe.get_num_msgs(),
            fe.get_max_delta(),
            fe.get_min_delta(),
            fe.get_avg_delta(),
            fe.get_num_dao(),
            fe.get_num_dis(),
            fe.get_num_dao(),
            dio_deltas[0],
            dio_deltas[1],
            dio_deltas[2],
            dis_deltas[0],
            dis_deltas[1],
            dis_deltas[2],
            dao_deltas[0],
            dao_deltas[1],
            dao_deltas[2]
        )
        

    def preprocess_data(self) -> pd.DataFrame:
        csv_files = self._fetch_data_src()
        for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            fe = FeatureExtractor(df)
        pass





    