"""
Class for IQ Data
CSV formats

Xaratustrah Aug-2015

"""

import numpy as np
import time, os
from iqbase import IQBase


class CSVData(IQBase):
    def read(self, nframes=10, lframes=1024, sframes=1):
        self.lframes = lframes
        self.nframes = nframes

        x = np.genfromtxt(self.filename, dtype=np.float32)
        self.fs = x[0, 0]
        self.center = x[0, 1]
        all_data = x[1:, :]
        all_data = all_data.view(np.complex64)[:, 0]
        self.number_samples = len(all_data)
        self.nframes_tot = int(self.number_samples / lframes)
        self.date_time = time.ctime(os.path.getctime(self.filename))

        total_n_bytes = nframes * lframes
        start_n_bytes = (sframes - 1) * lframes

        self.data_array = all_data[start_n_bytes:start_n_bytes + total_n_bytes]
