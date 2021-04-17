# Author: Cesaire Tchoudjuen
# Main program that will be ran by user
# Program that:
# (1) outputs a summary of each variable to a single text file
# (2) saves a histogram of each variable to png files
# (3) outputs a scatter plot of each pair of variables

# IMPORT USED LIBRARIES
import subprocess 
import IrisFlowersPlot

# The subprocess library allows to spawn new processes. In this program it fetches and executes external scripts
subprocess.call("IrisFlowersPlot.py", shell=True)