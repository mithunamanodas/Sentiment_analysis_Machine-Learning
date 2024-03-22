from flask import Flask, render_template, request, redirect, url_for, session
import jsonpickle
#from flask import Flask, jsonify, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.externals import joblib
import sklearn.externals
import joblib

import mysql.connector
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import warnings
warnings.filterwarnings('ignore')
app=Flask(__name__)
Swagger(app)

app.secret_key=os.urandom(24)



conn = mysql.connector.connect(host="localhost",user="root",password="",database="pythonlogin")
cusrsor = conn.cursor()

#newData = pd.read_csv(r'C:\other\latest\Imdb-Sentiment-Analysis-Flask\IMDB_Dataset.csv')
mnb = pickle.load(open('Naive_Bayes_model_imdb.pkl','rb'))
countVect = pickle.load(open('countVect_imdb.pkl','rb'))



@app.route("/comments",methods=['POST','GET'])
def comments():
    #deatails = ''
    print('cities')
    set=False
    if session:
       return render_template("comments.html",set=set)
    else:
       return  redirect('/')

@app.route("/goto",methods=['POST','GET'])
def goto():
    #deatails = ''
    set=True
   # Import necessary libraries
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    from textblob import TextBlob

    # Download required NLTK data
    #nltk.download('vader_lexicon',halt_on_error=False)
    #import nltk
    #dler = nltk.downloader.Downloader()
    #dler._update_index()
    #dler._status_cache['panlex_lite'] = 'installed' # Trick the index to treat panlex_lite as it's already installed.
    #dler.download('vader_lexicon')
    #nltk.downloader.download('vader_lexicon')

    # Define a function to perform sentiment analysis using VADER
    
    # Define a function to perform sentiment analysis using TextBlob
    def analyze_sentiment_textblob(comment):
        blob = TextBlob(comment)
        if blob.sentiment.polarity > 0:
            return 'Positive'
        elif blob.sentiment.polarity < 0:
            return 'Negative'
        else:
            return 'Neutral'

    # Example comment to test sentiment analysis
    comment = request.form.get('comment')

    # Perform sentiment analysis using VADER
    #sentiment_vader = analyze_sentiment_vader(comment)
    #print(f"Sentiment (VADER): {sentiment_vader}")

    # Perform sentiment analysis using TextBlob
    sentiment_textblob = analyze_sentiment_textblob(comment)
    print(f"Sentiment (TextBlob): {sentiment_textblob}")

    c= comment
    s = sentiment_textblob

    cusrsor.execute("""INSERT INTO  `sentiment` (`id`,`comment`,`sentiment`) VALUES (NULL,'{}','{}') """.format(c,s))
    conn.commit()
    if session:
        return render_template("comments.html",set=set,comment=comment,senti=sentiment_textblob)
    else:
        return redirect("/")

@app.route("/savecsv",methods=['POST','GET'])
def savecsv():
    set=False
    query = "SELECT comment,sentiment FROM sentiment"
    cursor = conn.cursor()
    cursor.execute(query)
    #print(cursor.execute(query))
    myallData = cursor.fetchall()

    all_user_name = []
    all_tweets = []
    for  text,user_name in myallData:
        all_user_name.append(user_name)
        all_tweets.append(text)
    print(all_user_name)
    #we need to store this data to CSV
    dic = {'review':all_tweets,'sentiment' : all_user_name}
    df = pd.DataFrame (dic)
    df_csv = df.to_csv('E:\mainproject\Imdb-Sentiment-Analysis-Flask\Comments\Comments.csv')
    folder_path = r'E:\mainproject\Imdb-Sentiment-Analysis-Flask\Comments'
    os.system(f'start {folder_path}')
    #deatails = ''
    print('cities')
    if session:
      return render_template("comments.html",set=set)
    else:
      return redirect("/")


@app.route('/login_validation', methods =['POST'])
def login_validation():
    user = request.form.get('username')
    password = request.form.get('password')
    cusrsor.execute("""SELECT * FROM `accounts` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """.format(user,password))
    users =cusrsor.fetchall()
    #print(users)
    msg = ''
    if len(users)>0:
        session['user_id']=users[0][0]
        return redirect('/')
    else:
        msg = 'You have entered an invalid username or password'
        return render_template('login.html',msg = msg)

@app.route('/add_users', methods =['POST'])
def add_users(): 
    name = request.form.get('uname')
    email = request.form.get('uemail')
    psw = request.form.get('upsw')
    cusrsor.execute("""INSERT INTO  `accounts` (`id`,`username`,`password`,`email`) VALUES (NULL,'{}','{}','{}') """.format(name,psw,email))
    conn.commit()

    cusrsor.execute("""SELECT * FROM `accounts` WHERE `email` LIKE '{}'  """.format(email))
    myuser = cusrsor.fetchall()
    session['user_id']=myuser[0][0]
    return redirect('/')

@app.route('/login')
def login():
    if session:
        return render_template('index.html')
    else:
        return render_template('login.html')

    
@app.route("/register")
def register():
    if session:
        return render_template('index.html')
    else:
        #return redirect('/login')
        return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('user_id')
    return redirect("/")


@app.route('/imdb-home')
def home():
    if session:
      return render_template('imdbhome.html')
    else:
      return redirect("/")

@app.route('/imdb-home-view')
def home2():
    folder_path = r'E:\mainproject\Imdb-Sentiment-Analysis-Flask\DataSet'
    os.system(f'start {folder_path}')
    if session:
       return render_template('imdbhome.html')
    else:
       return redirect("/")

@app.route('/senti')
def senti():
    if session:
      return render_template('senti.html')
    else:
      return redirect("/")

@app.route('/about')
def about():
    if session:
        return render_template('about.html')
    else:
        return redirect("/")

@app.route('/')
def indexx():
    
    return render_template('index.html')
    

@app.route('/index')
def index():
    if session:
        return render_template('index.html')
    else:
        return redirect("/")

@app.route('/ytube',methods=['POST','GET'])
def ytube():
    if request.method == 'POST':
        
        Com = request.form['Com']
        new = []
        
        def scrapper(condition):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(Com)
            driver.execute_script('window.scrollTo(1, 500);')
            #now wait let load the comments
            time.sleep(7)
            #scroll window from x-cordinaate 0 to y-cordinate-3000
            driver.execute_script('window.scrollTo(1, 3000);')
            comment_div=driver.find_element("xpath",'//*[@id="contents"]')
            #this is a list
            comments=comment_div.find_elements("xpath",'//*[@id="content-text"]')
            #create list of comments
            comments_list = []
            #create list to store score of comments
            comment_score = []
            print("Comments : ")
            for comment in comments:
                print("\n",comment.text)
                comments_list.append(comment.text)
                #calculate score of that comment
                comment_score.append(analyze(comment.text))
                #create a dictionary with all the values
            data = {'Comment':comments_list,'Sentiment':comment_score}
            df = pd.DataFrame(data, columns=['Comment','Sentiment'])
            new={'data':df,'percent':totalSentiment(df)}
            
            
            return new

        def analyze(comment):

            #analyzing the data
                sid_obj = SentimentIntensityAnalyzer()
    
        # polarity_scores method of SentimentIntensityAnalyzer
        # object gives a sentiment dictionary.
        # which contains pos, neg, neu, and compound scores.
                score = sid_obj.polarity_scores(comment)

                #score = SentimentIntensityAnalyzer().polarity_scores(comment)
                
                if score['compound'] >= 0.05 :
                    sentiment = "Positive"
                elif score['compound'] <= - 0.05 :
                    sentiment = "Negative"
                else:
                    sentiment = "Neutral"
                
                return sentiment
        def totalSentiment(df):
            #calculate the percentage of sentiments
            sentiment_list = df.loc[:,'Sentiment']
            count_Positive = 0
            count_Neutral = 0
            count_Negative = 0
            count = 0
            for sentiment in sentiment_list:
                if(sentiment == 'Positive'):
                    count_Positive +=1
                elif(sentiment == 'Negative'):
                    count_Negative +=1
                else:
                    count_Neutral +=1
                count+=1
                
            if(count != 0):
                print("\nPositivity percentage : ",(count_Positive/count)*100)
                print("\nNegativity percentage: ",(count_Negative/count)*100)
                print("\nNeutrality percentage: ", (count_Neutral/count)*100)
                data = {'positive':((count_Positive/count)*100),'negative':((count_Negative/count)*100),'neutral':((count_Neutral/count)*100)}
                return data
            else:
                print("Issue with scrapping. Please try again!")
                data=[]
                return data
        
        Array = scrapper('no')
        customUrl=Com.replace("watch?v=", "embed/")
        if session:
            return render_template('ytube.html',data1=scrapper('no'),URL =Com,cUrl=customUrl, tables=[Array['data'].to_html()], titles=[''])
        else:
            return redirect("/")
""" @app.route("/table")
def table():
    import csv
    filename = 'IMDB_Dataset.csv'
    data = pd.read_csv(filename, header=0)
    stocklist = list(data.values)
    return render_template('table.html', stocklist=stocklist) """

    

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        Reviews = request.form['Reviews']
        data = [Reviews]
        #print(countVect)
        vect = countVect.transform(data).toarray()
        my_prediction = mnb.predict(vect)
    if session:
        return render_template('result1.html',prediction = my_prediction, getData=Reviews)
    else:
        return redirect("/")
@app.route('/youtub',methods=['POST','GET'])
def youtub():
    
    if request.method == 'POST':
        
        Com = request.form['Com']
        data = [Com]
        #print(countVect)
        #vect = countVect.transform(data).toarray()
        #my_prediction = mnb.predict(vect)
    if session:
        return render_template('youtube.html', getData=Com)
    else:
        return redirect("/")

@app.route('/youtube',methods=['POST','GET'])
def youtube():
    if session:
        return render_template('youtube.html')
    else:
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
    
