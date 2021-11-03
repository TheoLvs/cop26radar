import streamlit as st
import datetime



# st.image("https://www.transformative-mobility.org/assets/site/events/COP26.PNG")
st.image("https://www.lifewatch.eu/wp-content/uploads/2021/06/UN-Climate-Change-Conference.jpg")



#----------------------------------------------------------------------------------------------------------------------
# SIDEBAR
#----------------------------------------------------------------------------------------------------------------------


st.sidebar.image("./img/logo_cop2.png",width = 150)
st.sidebar.write("""
# COP26 Radar
The purpose of the COP26 radar is to **analyze reactions to official conference announcements** and public perception on social networks.

In particular, we will **analyze the emotions** and try to **quantify the greenwashing**. 

The analysis is done using NLP (Natural Language Processing) techniques. 
""")

st.sidebar.write("""##### Table of contents
1. [How to use](#how-to-use)
2. [Highlights](#highlights)
3. [Data Analysis](#data-analysis)
4. [Topics](#topics)
5. [Emotions & reactions](#emotions-reactions)
""")


st.sidebar.write("""
## Author

Work done by [Théo Alves Da Costa](https://www.linkedin.com/in/th%C3%A9o-alves-da-costa-09397a82/).
Head of AI for Sustainability at [Ekimetrics](https://ekimetrics.com/) & Co-Lead for the NGO [Data For Good](https://dataforgood.fr/).

I am present at the COP26 from the 4th to the 12th, if you want to meet in person. 

- Code for the platform is open sourced on [Github](https://github.com/TheoLvs/cop26radar)
- Contact by mail [here](mailto:theo.alvesdacosta@ekimetrics.com)

## Methodology
For developers - analysis are done on Twitter data using Python, Flashtext, Hugging Face pretrained Transformers models from Cardiff University, BERTopic, langdetect, VADER.
*Work in progress - Detailed methodology article and open source code soon available* 

## AI Carbon Footprint
Artificial intelligence can consume a lot of energy, so special attention was paid to reduce the carbon footprint of the analyses: no cloud platform was used - performed on a simple laptop, the computing is done asynchronously to avoid multiplying requests and live calculations.

Moreover, the carbon footprint was measured with the [CodeCarbon](https://github.com/mlco2/codecarbon) tool developed by the MILA University.
""")


#----------------------------------------------------------------------------------------------------------------------
# USAGE
#----------------------------------------------------------------------------------------------------------------------



st.write("## How to use")
st.write("Select below the day you want to analyse")
analysis_day = st.selectbox('Which day of the conference',
    ('Day 1','Day 2')
)
st.write("*For now analyses are done live every day, a summarization of all analyses will be done at the end of the conference*")



st.write("## Highlights")


st.write("## Data Analysis")
st.info("WIP")
col1, col2, col3 = st.columns(3)
col1.metric("# of tweets", "70 °F", "1.2 °F")
col2.metric("# of likes", "70 °F", "1.2 °F")
col3.metric("Temperature", "70 °F", "1.2 °F")

st.write("Evolution of tweets")
st.write("Hashtags")
st.write("Languages")


st.write("### Top tweets")
st.info("WIP")


st.write("## Topics")
st.info("WIP")

st.write("## Emotions & reactions")
st.info("WIP")