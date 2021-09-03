import streamlit as st
import pickle
import numpy as np
import pandas as pd
import pydeck as pdk
import scikit-learn
from PIL import Image




page = st.sidebar.selectbox(
'Select a Page',('Home','Crash-Map','Make a prediction!')
)

if page == 'Crash-Map':
    df = pd.read_csv('./Clean_dataframe/clean_df.csv')
    df = df[['latitude','longitude']]
    st.map(df,zoom=11,use_container_width=True)
    st.write("Red color depicts different crashes in Tempe, Arizona from 2012 to 2021")

if page == 'Home':
    st.title('What is Vision Zero?')
    image_1 = Image.open('st_images/vision_zero.jpeg')
    st.image(image_1)
    st.write("Vision Zero is a multi-national road traffic safety project that aims to achieve a highway system with no fatalities or serious injuries involving road traffic. It started in Sweden and was approved by their parliament in October 1997. A core principle of the vision is that 'Life and health can never be exchanged for other benefits within the society' rather than the more conventional comparison between costs and benefits, where a monetary value is placed on life and health, and then that value is used to decide how much money to spend on a road network towards the benefit of decreasing risk. Vision Zero was introduced in 1995. It has been variously adopted in different countries or smaller jurisdictions, although its description varies significantly. The countermeasures implemented in Vision Zero continue to be education, enforcement and engineering, applied since the 1930s.")
    st.write("Vision Zero is based on an underlying ethical principle that 'it can never be ethically acceptable that people are killed or seriously injured when moving within the road transport system.' As an ethics-based approach, Vision Zero functions to guide strategy selection and not to set particular goals or targets. In most road transport systems, road users bear complete responsibility for safety. Vision Zero changes this relationship by emphasizing that responsibility is shared by transportation system designers and road users.")
    st.write("")
    st.write("")

    st.title('The Arizona Department of Transportation (A-DOT)')
    st.image('https://pbs.twimg.com/media/DkhA_PSU0AAO8f6.jpg')
    st.write("The Arizona Department of Transportation (ADOT, pronounced 'A-Dot') is an Arizona state government agency charged with facilitating mobility within the state. In addition to managing the state's highway system, the agency is also involved with public transportation and municipal airports. The department was created in 1974 when the state merged the Arizona Highway Department with the Arizona Department of Aeronautics.")
    st.write("")
    st.write("")

    st.title('Preventing Insurance Fraud:')
    st.image('https://cdn.images.express.co.uk/img/dynamic/24/590x/car-insurance-fraud-personal-injury-1335709.jpg?r=1600179606146',caption = 'Car insurance UK: Fraudsters target personal injury payouts in latest motoring scam | Express.co.uk')
    st.write("Personal injury-related insurance fraud is typically defined as any act intended to cause an insurance company to compensate you for an injury that is nonexistent, exaggerated, or unrelated to any accident covered by the policy. Common examples include faking or exaggerating the nature and extent of injuries after an accident, or planning or staging a theft, arson incident, or car accident.")



    st.write("")
    st.write("")
    st.title('Sources:')
    st.write("1. https://en.wikipedia.org/wiki/Vision_Zero")
    st.write("2. https://en.wikipedia.org/wiki/Arizona_Department_of_Transportation")
    st.write("3. https://www.alllaw.com/articles/nolo/personal-injury/claim-fraud.html")
    st.write("4. Data collected from https://catalog.data.gov/dataset/1-08-crash-data-report-detail")

if page == 'Make a prediction!':
    st.title('Predicting if a crash involves an injury or not')
    features = ['Injury_Severity','AlcoholUse_Drv1','AlcoholUse_Drv2','Age_Drv1','DrugUse_Drv1','Head_On','Left_Turn',
            'Other','Rear_End','Same_Direction','Not_Clear_Weather','Not_Dry_Surface']

    #1
    st.write('1. Enter the age of first driver (Driver 1) involved in the crash:')
    Age_Drv1 = st.text_input(label = 'Range from 0 to 110',  value = 0,key='1')
    #2
    st.write('2. Enter if drug was a contributing factor in the crash or not (Driver 1)')
    DrugUse_Drv1 = st.text_input(label = 'Enter 0 for no and 1 for yes',  value = 0,key='2')
    #3
    st.write('3. Enter if alcohol was a contributing factor in the crash or not (Driver 1)')
    AlcoholUse_Drv1 = st.text_input(label = 'Enter 0 for no and 1 for yes',  value = 0,key='3')
    #4
    st.write('4. Enter if alcohol was a contributing factor in the crash or not (Driver 2)')
    AlcoholUse_Drv2 = st.text_input(label = 'Enter 0 for no and 1 for yes',  value = 0,key='4')
    #5
    st.write('5. Choose a Collision manner:')
    manner = st.radio("Please choose from one of these 5 different collision manners:", ('Head_On', 'Left_Turn','Rear_End', 'Same_Direction', 'Other'))
    if manner == 'Head_On':
        Head_On        = 1
        Left_Turn      = 0
        Rear_End       = 0
        Same_Direction = 0
        Other          = 0

    if manner == 'Left_Turn':
        Head_On        = 0
        Left_Turn      = 1
        Rear_End       = 0
        Same_Direction = 0
        Other          = 0

    if manner == 'Rear_End':
        Head_On        = 0
        Left_Turn      = 0
        Rear_End       = 1
        Same_Direction = 0
        Other          = 0

    if manner == 'Same_Direction':
        Head_On        = 0
        Left_Turn      = 0
        Rear_End       = 0
        Same_Direction = 1
        Other          = 0

    if manner == 'Other':
        Head_On        = 0
        Left_Turn      = 0
        Rear_End       = 0
        Same_Direction = 0
        Other          = 1

    #6
    st.write('6. Enter if the weather was clear on the time of crash or not')
    Not_Clear_Weather = st.text_input(label = 'Enter 0 for clear weather and 1 for not clear weather',  value = 0,key='5')

    #7
    st.write('7. Enter if the road surface was dry or not')
    Not_Dry_Surface = st.text_input(label = 'Enter 0 for dry surface and 1 for not dry surface',  value = 0,key='6')

    #8
    st.write('8. Enter level of injury severity')
    Injury_Severity = st.text_input(label = 'Enter 1 for serious injury and 0 for otherwise',  value = 0,key='7')

    #For this portion I took help from project 4's streamlit app
    click = st.button('Predict')
    if click:
        with open('Best_model_Ada_Boosting.pkl', mode = 'rb') as pickle_in:
            pipe = pickle.load(pickle_in)
            input_val = [Injury_Severity,AlcoholUse_Drv1,AlcoholUse_Drv2,Age_Drv1,DrugUse_Drv1,Head_On,Left_Turn,
            Other,Rear_End,Same_Direction,Not_Clear_Weather,Not_Dry_Surface]
            input_val = np.reshape(input_val,(1,-1))
            predict = pipe.predict(input_val)

            dict = {0:'no injuries',
            1:'one or more injuries'}
            st.write(f'The model predicts that this crash will have {dict[predict[0]]}.')
