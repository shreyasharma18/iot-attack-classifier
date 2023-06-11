import os
from os.path import join, isfile, split
import sys
import json
import argparse
import logging
import pandas as pd
from typing import List
from feature_extractor import (FeatureExtractorPCAP,
                               FeatureExtractorLog)
from data import DataFields
from dataclasses import asdict

class DataLoader:

    def __init__(self, csv_path) -> None:
        # path to csv files
        self.csv_path = csv_path
        self.log_dir = "/home/sheron/Desktop/iot-attack-classifier/Dataset/Small Network/Log Files/"

    def _filter_readable_files(self, files) -> List[str]:
        readable_files = [f for f in files \
                if isfile(join(self.csv_path, f))]
        return readable_files

    def _filter_csv_files(files) -> List[str]:
        csv_files = [f for f in files if f.endswith('.csv')]
        return csv_files

    def _fetch_data_src(self) -> List[str]:
        # fetch all files and return relevant
        # csv files
        files = os.listdir(self.csv_path)
        readable_files = self._filter_readable_files(files)
        csv_files = self._filter_csv_files(readable_files)
        return [join(self.csv_path, f) for f in csv_files]
    
    def extract_features(self, df: pd.DataFrame) -> pd.DataFrame:
        fe = FeatureExtractorPCAP(df)
        fe.is_data_msg()
        fe.is_dio_msg()
        fe.is_dis_msg()
        fe.is_dao_msg()
        fe.time_diff()
        dio_deltas = fe.get_dio_delta()
        dao_deltas = fe.get_dao_delta()
        dis_deltas = fe.get_dis_delta()

        fe_log = FeatureExtractorLog(self.log_path)
        drop_counter = fe_log.load_log_file()
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
            dao_deltas[2],
            drop_counter["collision_drops"],
            drop_counter["neigh_alloc_drops"],
            drop_counter["queue_drops"],
            drop_counter["packetn_drops"]
        )
        return asdict(data)        

    def preprocess_data(self) -> pd.DataFrame:
        csv_files = self._fetch_data_src()
        df = pd.DataFrame()
        for csv_file in csv_files:
            self.log_path = join(self.log_dir, split(csv_file)[1][:-4] + ".testlog")
            df = pd.read_csv(csv_file)
            rec = self.extract_features(df)
            df = df.append(rec, 
                           ignore_index=True)
        return df




    