from secedgar import filings
from datetime import date
import streamlit as st

from sec_edgar_api import EdgarClient

# Specify user-agent string to pass to SEC to identify
# requests for rate-limiting purposes
edgar = EdgarClient(user_agent="Rad lab production <Anson>@<aragond.tech>")

# Get submissions for Apple with the additional paginated files
# appended to the recent filings to prevent the need for extra
# manual pagination handling
#filin = edgar.get_submissions(cik="320193") 
filin = edgar.get_submissions(cik="0001959228")
#create a dataframe from the filin
df = pd.DataFrame(filin)
#display the dataframe
st.write(df)

