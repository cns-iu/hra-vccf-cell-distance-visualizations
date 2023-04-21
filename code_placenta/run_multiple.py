
# import os

# for i in range(1,2):
#     os.system("python3 vccf_visualizations.py " + str(i))

import os
import sys

# # Define a list of arguments to pass to the script
# args_list = ["arg1", "arg2", "arg3"]

# Iterate over the arguments list and execute the script with each argument
for arg in range(1,210):
    os.system(f"python3 vccf_visualizations.py {arg}")


# Images 8, 58, 92, 151, 174, 195, 196, 203 have no enthothelial cells

# Interesting images 70, 38, 204