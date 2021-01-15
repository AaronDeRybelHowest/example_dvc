import wget

print('retrieve data from UCI machine learning repository to local device')

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
wget.download(url)