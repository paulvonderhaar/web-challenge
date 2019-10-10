import pandas as pd


def main():
	df = pd.read_csv('cities.csv')
	df.to_html('data.html')




main()