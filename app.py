from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import pickle

# load the model from disk
filename = 'nlp_model.pkl'
classifierNB = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
#	df= pd.read_csv("spam.csv", encoding="latin-1")
#	df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
#	# Features and Labels
#	df['label'] = df['class'].map({'ham': 0, 'spam': 1})
#	X = df['message']
#	y = df['label']
#	
#	# Extract Feature With CountVectorizer
#	cv = CountVectorizer()
#	X = cv.fit_transform(X) # Fit the Data
#    
#    pickle.dump(cv, open('tranform.pkl', 'wb'))
#    
#    
#	from sklearn.model_selection import train_test_split
#	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#	#Naive Bayes Classifier
#	from sklearn.naive_bayes import MultinomialNB
#
#	classifierNB = MultinomialNB()
#	classifierNB.fit(X_train,y_train)
#	classifierNB.score(X_test,y_test)
#    filename = 'nlp_model.pkl'
#    pickle.dump(classifierNB, open(filename, 'wb'))
    
	#Alternative Usage of Saved Model
	# joblib.dump(classifierNB, 'NB_spam_model.pkl')
	# NB_spam_model = open('NB_spam_model.pkl','rb')
	# classifierNB = joblib.load(NB_spam_model)

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = classifierNB.predict(vect)
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)