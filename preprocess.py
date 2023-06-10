import os
from os.path import join, isfile
import sys
import json
import argparse
import logging
import pandas as pd
from typing import List, Tuple, Optional

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
    
    def preprocess_data(self) -> pd.DataFrame:
        csv_files = self._fetch_data_src()
        for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            
        pass





    