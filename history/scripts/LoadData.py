# Load packages
import pandas as pd

# Load review data
F23url = 'https://raw.githubusercontent.com/matthew-zahn/as.180.369/main/history/input/F23CourseReviews.csv'
#F23url = 'https://raw.githubusercontent.com/llorracc/as.180.369/main/history/input/F23CourseReviews.csv'
F23df = pd.read_csv(F23url,sep=";")
print(F23df.head())

# Export as a pickle
#F23url = 'https://raw.githubusercontent.com/llorracc/as.180.369/main/history/output/F23CourseReviews.pkl'
outpath = 'F23CourseReviews.pkl'
F23df.to_pickle(outpath)

# Load example
#df = pd.read_pickle(outpath)
# EOF
