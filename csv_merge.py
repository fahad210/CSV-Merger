import os
import glob
import pandas as pd
#Change “csv_folder” to your desired working directory
os.chdir("csv_folder")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f, encoding = "ISO-8859-1") for f in all_filenames ])
combined_csv.to_csv( "Combined_CSV.csv", index=False, encoding='utf-8-sig')
