import streamlit as st
import pandas as pd
##########################################################################################

GPC=pd.read_csv("Nvidia Graphics Cards.csv")
GPC.reset_index(drop=True, inplace=True)
#GPC=GPC.sort_values('Released Year')
NvidiaorAMD=['Both NVIDIA and AMD','NVIDIA','AMD']
database_url="https://www.techpowerup.com/gpu-specs/"

#########################################################################################
st.write("""
         # GRAPHICS CARD LIST FILTER
         """)
st.text('         The purpose of this application is to let user choose the specification they')
st.text('require from a graphics card either for their graphics intensive jobs, researchs')
st.text('or gaming in general.')
st.image("https://www.gpumag.com/wp-content/uploads/2020/05/AMD-and-NVIDIA-GPUs.jpg")
st.caption("Image above shown two different brands of Graphics Cards. From left to right are NVIDIA's Geforce Series and AMD's Radeon Series.")
st.text('         It simple to use, just move the sliders in the sidebar and the graphics card list')
st.text(' will be filtered.')
st.text('Note: Only recent popular graphics cards from year 2010 are listed in this table!')

##########################################################################################    

st.sidebar.write('Move the sliders to filter the list:')

type_GPC = st.sidebar.selectbox('Select NVIDIA and/or AMD:', NvidiaorAMD, 0)

memory = st.sidebar.slider('Select Lowest Memory Size (in Gb):', 1,24,1)
    
gpu=st.sidebar.slider('Select lowest GPU Clock (in MHz):', 675,2321,675)
      
memory_c=st.sidebar.slider('Select Lowest Memory Clock (in MHz)', 900,2248, 900)
     
shaders=st.sidebar.slider('Select Lowest Shaders:', 192,10496,192)

#########################################################################################

if type_GPC=='NVIDIA':
         GPC = GPC[GPC['Product Name'].str.contains('GeForce')]
elif type_GPC=='AMD':
         GPC = GPC[GPC['Product Name'].str.contains('Radeon')]
else:
         GPC = GPC

GPC = GPC[GPC['Memory (Gb)'] >= memory] 

GPC = GPC[GPC['GPU clock (MHz)'] >= gpu] 

GPC = GPC[GPC['Memory clock (MHz)'] >= memory_c] 

GPC = GPC[GPC['Shaders'] >= shaders] 


########################################################################################

if len(GPC.index)==0:
         st.error('No Graphics Cards Found')
else:
         st.dataframe(GPC)

st.markdown('Database Source ---> [TechPowerUp: GPU Specs Database](%s)' % database_url)

#########################################################################################
