"""
Example 6x6 wind farm setup
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from floris.tools import FlorisInterface

def farm(Sx=6, Sy=6, D=126., wd_array=None, ws_array=None, rows=6, cols=6, velocity_model='Gauss'): 
    # Instantiate FLORIS using either the GCH or CC model
    if velocity_model == 'Jensen': 
        inputfile = 'jensen.yaml'
    elif velocity_model == 'Gauss': 
        inputfile = 'gch.yaml'
    else: 
        raise NotImplementedError('velocity_model must be `Jensen` or `Gauss`')
    fi = FlorisInterface(Path(__file__).parent / "inputs" / inputfile) # GCH model matched to the default "legacy_gauss" of V2

    # Define a two turbine farm
    xG, yG = np.meshgrid(np.arange(0, rows) * Sx * D, np.arange(0, cols) * Sy * D, indexing='ij')
    layout_x = xG.ravel()  # np.array([0, D*6])
    layout_y = yG.ravel()  # [0, 0]

    # Sweep wind speeds but keep wind direction fixed
    if wd_array is None: 
        wd_array = np.arange(250,291,1.)
    if ws_array is None: 
        ws_array = np.array([8])  # 8 m/s

    fi.reinitialize(layout_x=layout_x, layout_y=layout_y, wind_directions=wd_array, wind_speeds=ws_array)
    return fi


if __name__ == "__main__": 
    pass
