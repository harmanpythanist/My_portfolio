import streamlit as st
import pandas as pd

def display_text_shape(text, text_color='white', background_color=None, size=14, border_radius=0):
    st.write(
        f'<span style="color: {text_color}; background-color: {background_color}; padding: 5px; font-size: {size}px; border-radius: {border_radius}px;">{text}</span>',
        unsafe_allow_html=True)


def colored_subheader(text, color='white'):
    st.markdown(f'<h3 style="color: {color};">{text}</h3>', unsafe_allow_html=True)


def display_underline(text, underline=False, color="white", size=14, bold=False):
    styles = f'color: {color}; text-decoration: {"underline" if underline else "none"};'
    styles += f'font-size: {size}px; font-weight: {"bold" if bold else "normal"};'
    styled_text = f'<span style="{styles}">{text}</span>'
    st.markdown(styled_text, unsafe_allow_html=True)

st.subheader("Harman Abdul Waheed")
display_underline('Data Scientist', size=15, bold=True)
st.write('Pythonista, passionate about NLP, data science and training AI model.')
st.write('---')
a, b, c, d, e, f = st.tabs(['General', 'Projects', 'Experience', 'Softwares', 'Skills' , 'Workspaces'])

with a:
    st.write('I am Harman, residential of Pakistan, living in the city Lahore. As a young skillfull person(atleast I think I have skills) I am hopefull to have a great impact in the field of Artificial Intelligence.')
    st.write("---")
    st.markdown('Bio data: ')
    data = pd.DataFrame({'Data':['Name', 'Country living in', 'Age', 'Email', 'Contact number', 'Moto'], 'Answers':['Harman', 'Pakistan', '19', 'harmanwaheed@gmail.com', '+923329555307', 'Consistency']})
    data = pd.DataFrame({'Data':['Name', 'Country living in', 'Age', 'Email', 'Contact number', 'Moto'], 'Answers':['Harman', 'Pakistan', '19', 'harmanwaheed@gmail.com', '+923329555307', 'Consistency']})
    st.table(data)

with b:
    display_underline('1 - Restaurants feedback sentiment analysis – NLP with python', size=18, bold=True, color='black')
    display_underline('Using the machine learning and natural language techniques in python I have built a model that could predict whether the feedback is positive on negative. I have achieved accuaracy of 83.25% on that model, which is pretty impressive', size=16, color='black')
    display_underline('For this project I have used these modules in python: ', size=16, underline=True)
    display_underline('TfidfVectorizer, CountVectorizer, LogisticRegression, and machine learning techniques including accuracy, split method, Stop word etc.', bold=True)
    display_underline("See my sentiment analysis model on github: ", size=16)
    st.write('[feedbacks predictions model](https://github.com/harmanpythanist/Sentiment_analysis_movie_reviews)')

    st.write('---')
    display_underline('2 - Cats and Dogs classification - Convolutional Neural network', size=18, bold=True, color='yellow')
    display_underline('Using AI techniques to let the computer understand whether image is of cat or a dog is very interesting and complex as well. I have used convolutional neural network for this purpose which perform efficient on very large data(number of pixels in images)', size=16)
    display_underline('Used techniques: ', size=16, underline=True)
    display_underline('Tensorflow, keras, Sequential, Conv2d, optimizers, fully connected layers, and other techniques related to neural networks', bold=True)
    display_underline("See my website which can classify images based on this project: ", size=16)
    st.write('[Dogs-cats Classification app](https://https://neuralnetwok.streamlit.app/)')
    st.write('---')
    display_underline('3 - Movies Recommendation system - ML with python', size=18, bold=True, color='yellow')
    display_underline("I have used nlp and ai related stuff to make this model suggest you a movie based on any other movie. It will extract your movie's overview from the IMDB reviews and find a movie with similar overview for you. This project included high math calculations and techniques to reach a overview of same taste", size=16)
    display_underline('Used techniques: ', size=16, underline=True)
    display_underline('Machine learning algorithms and for converting text data into numerics, tfidf vectorizer and count vectorizer is used. For calculating the overviews similarity, Cosine similarity and linear kernel (from sklear) is used', bold=True)
    display_underline("See my movies recomemndation system sources on github: ", size=16)
    st.write('[feedbacks predictions model](https://github.com/harmanpythanist/Movies_recommendation_system)')
    st.write('---')
    display_underline('4 - Selfmade Chatbot - NLP, ML', size=18, bold=True, color='yellow')
    display_underline('After making a model that could suggest you movie based on a movie you already liked (upper project), I thought to make it more robust by converting it into a chatbot.', size=16)
    display_underline('that chatbot will talk to you in a way a human would and suggest you a movie. The new thing is chatbot. It uses some artificial techniques and some rule based commands', size=16)
    display_underline('Used techniques: ', size=16, underline=True)
    display_underline("Spacy(i wide library for nlp), re, CountVectorizer, sklearn, textblob and many other techniques to find patterns in the user's text to provide him with an appropriate response", bold=True)
    display_underline('See the code online in my repository: ', size=16)
    st.write("[Movies suggestions chatbot](https://github.com/harmanpythanist/chatbot_movies_python)")
    st.write('---')
    display_underline('5 - Website for my college students - Purely Python', size=18, bold=True, color='yellow')
    display_underline("I have made a website for my college and that website is connected with a database to store the data. I have added options to sign up, login, add random note, gossip to the home page of website and also one option to add confession. Furthermore, there is teachers data visible in the website and in the position of principal its my picture(with a note that I am not principal)", size=16)
    display_underline('Used tools:', size=16, underline=True)
    display_underline('Streamlit, database, processing with dataframes, some css tools to make forms(to submit data) looks better, Some data science techniques to fetch data data from databse to add it on the website, Ballons celebrations and animations from lottie files to make website more appealing', bold=True)
    display_underline("Have a look at that website, you will absolutely enjoy!")
    st.write("[Fazaia-Inter-College-network](https://fazaia-inter-college-network.streamlit.app/)")

    st.write('---')
    display_underline('These were some of the major work of mine, you can view further projects on my github', size=20, bold=True, underline=True, color='yellow')
    st.write("[Github account](https://github.com/harmanpythanist)")

with d:
    display_underline('Languages, technical, and other softwares are shown along with rating from 5', size=16, bold=True)
    df = pd.DataFrame({"Software":['Python', 'SQL', 'Spreadsheets','Anaconda',  'CSS', 'Javascripts', 'Bliss', 'Zoiper', 'Slack', 'Filmora', 'Azure machine learning'], 'Rating': [4.7, 4.0, 4.7, 4.5 ,3.5,3.0,4.2,4.0,4.0, 4.0, 4.3]})
    st.table(df)

with e:
    display_underline('Technical skills', size=16, bold=True)
    st.write('- :green[Deep Neural networks ---    4.9]')
    st.write('- :green[Artificial neural networks ---    4.7]')
    st.write('- :green[Web development    --- 4.5]')
    st.write('- :green[Natural language processing  ---  4.5]')
    st.write('- :green[Machine learning algotihms  ---   4.8]')
    st.write('- :green[Error handling   --- 4.8]')
    st.write('- :green[Stats   ---  4.6]')
    st.write('- :green[Data visualization ---    4.9]')
    st.write('- :green[Convolutional neural networks ---    4.7]')
    st.write('- :green[Softwares Engineering ---     4.5]')
    display_underline('Soft skills', bold=True, size=17)
    st.write('- :green[Leading ---5.0]')
    st.write('- :green[Consistency    ---5.0]')
    st.write('- :green[Task completion     ---4.9]')
    st.write('- :green[Punctuality   ---    4.9]')
    st.write('- :green[Hard working  ---      5.0]')
    st.write('- :green[Critical thinking ---     5.0]')
    st.write('- :green[Adaptablity    ---  5.0]')
    st.write('- :green[Learning  ---   5.0]')
    st.write('- :green[Freindly  ---   4.5]')
    st.write('- :green[Collaboration ---        4.9]')

with c:
    display_underline('Python Instructor', color='yellow', size=18, underline=True)
    st.write(':green[I take online classes of students from different origins including Pakistan and UAE and help them to elevate their understanding in ML including Linear models and Keras.]')


with f:
    st.write('Check out my progress in workspaces online: ')
    st.write('[Github](https://github.com/harmanpythanist)')
    st.write('[Datacamp](https://www.datacamp.com/portfolio/harmanwaheed)')
    st.write('[Linkedin](https://www.linkedin.com/in/harman-waheed-84004b255/)')
