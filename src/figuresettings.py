#!/usr/bin/python

# Hannah Johlas, 2019
# Revised Kirby Heck, 2023

import matplotlib

# Plot formatting
matplotlib.rcParams['savefig.format']     = 'png'                               # image file type (pdf, png)
matplotlib.rcParams['savefig.dpi']        = 300                                 # figure resolution (makes a little better .png)
matplotlib.rcParams['savefig.pad_inches'] = 0.10                                # remove extra whitespace
matplotlib.rcParams['savefig.bbox']       = 'tight'                           # remove extra whitespace = 'tight'
matplotlib.rcParams['lines.linewidth']    = 1.
matplotlib.rcParams['legend.handlelength']  = 1.5
matplotlib.rcParams['axes.linewidth'] = 0.5 # set the value globally
matplotlib.rcParams['xtick.major.width'] = 0.5
matplotlib.rcParams['ytick.major.width'] = 0.5
