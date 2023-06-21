import pandas as pd


read_file = pd.read_excel (" C:\Users\User\OneDrive\Desktop\python\Copy of sonar data.csv")


read_file.to_csv ("sonar.csv",
				index = None,
				header=True)

df = pd.DataFrame(pd.read_csv("sonar.csv"))

df
