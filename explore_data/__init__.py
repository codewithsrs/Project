import os, sys

module1_path = os.path.abspath(os.path.join('..', 'getfiles')) # .. goes up one directory
module2_path = os.path.abspath(os.path.join('..', 'explore_data'))
sys.path.append([module1_path,module2_path])
