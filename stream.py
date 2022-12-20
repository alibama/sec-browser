from secedgar import filings
from datetime import date

daily_filings = filings(start_date=date(2021, 6, 30),
                        user_agent="Anson Parker (ansondparker@gmail.com)")
daily_urls = daily_filings.get_urls()

st.write(daily_urls)
