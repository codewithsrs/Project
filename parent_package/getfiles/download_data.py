import connect_kaggle_api as k,Download_zip as d
import sys


print("Showing the paths available to this envirnoment..")
print(sys.path)


print("Authenticating with kaggle..")
kg2 = k.kaggle_auth()

print("setting the path for download..")
download_path = r'd:\BagPricePrediction\Project\data'

kg2.download(download_path,"playground-series-s5e2")
d.extract_all_zips_in_directory(download_path)