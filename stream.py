from secedgar import filings
from datetime import date
import streamlit as st
daily_filings = filings(start_date=date(2021, 6, 30),
                        user_agent="Anson Parker (ansondparker@gmail.com)")
daily_urls = daily_filings.get_urls()


from sec_edgar_api import EdgarClient

# Specify user-agent string to pass to SEC to identify
# requests for rate-limiting purposes
edgar = EdgarClient(user_agent="Rad lab production <Anson>@<aragond.tech>")

# Get submissions for Apple with the additional paginated files
# appended to the recent filings to prevent the need for extra
# manual pagination handling
edgar.get_submissions(cik="320193")

st.write(daily_urls)

st.write(edgar)
