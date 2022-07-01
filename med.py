# %%
import streamlit as st
from PIL import Image

# %%
#creatng the dict list of the medicine and disease
disease_list={'vomiting':'Aprepitant','head pain':'Aspirin','headpain':'Aspirin',
             'headache':'Aspirin','dizzy':'meclizine or dimenhydrinate (Dramamine)',
             'stomach pain':'Clidinium','stomachache':'Clidinium',
              'dizziness':'meclizine or dimenhydrinate (Dramamine)',
             'diabetes':'Metaformin','cold':'Montemac-L or Solvin-cold','loose motion':'O2 or Loperamide',
             'loosemotion':'O2 or Loperamide','body pain':'Solvin-cold',
              'bodypain':'Solvin-cold','muscle pain':'Solvin-cold or naproxen',
             'burn':'burnol cream or naproxen sodium (Aleve) or acetaminophen','cut':'Silver Nitrate Gel','muscle cramps':'Solvin-cold',
             'fever':'Ibuprofen','cough and fever':'Ibuprofen','musclecramps':'Solvin-cold or naproxen',
             'cough':'Grilinctus or Benadryl','periodscramp':'Meftal Spas',
             'periods cramp':'Meftal Spas','allergy':'Cetirizine or Loratadine',
             'diarrhea':'Loperamide or O2','anxiety':'Nexito Plus',
             'conjunctivitis':'ophthalmic antibiotic eyedrops or ointments such as Bleph (sulfacetamide sodium)'}

# %%
#creating a function to rerun the app 
def med_names():
    st.header('WELCOME TO MEDICINE OH MED!')
    #using image to display it in the web app using pillow lib
    image_link = ("http://www.trbimg.com/img-58c1ff36/turbine/sd-me-military-drugs-20170309")
    st.image(image_link,width=800)
    #displaying info what this website is all about
    st.text("This website is all about encountering common disease which we face in our \nday to day life. This website is specially for people who do not have much \nunderstanding about medicine.\nSo in case of emergency they can use this app to get prescribed") 
    st.markdown('We are happy to help you!')
    #taking input from the user
    client_input=st.text_input('You Are Suffering From ?').lower()
    if client_input in disease_list.keys():       
        med_name=disease_list.get(client_input)
        button=st.button('Search your medicine') 
        if button:
            #if the button is true the go and get the data 
            st.subheader('Medicine prescribe for you')
            st.subheader(med_name)
            st.balloons()
    else:
        button=st.button('Search your medicine') 
        if button:
            #if the button is true the go and get the data         
            st.subheader('Sorry not in our records Try Another') 
med_names() 

# %%


# %%
