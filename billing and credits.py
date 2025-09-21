import streamlit as st

st.set_page_config(page_title="Billing & Credits")

st.title("Billing & Credits")
st.write("💳 Here you can show credits balance, usage history, and invoices.")

# Example: credit balance
st.metric("Credits Remaining", "1,250", "-50 since last week")

# Example: usage breakdown
st.bar_chart({"Usage": [200, 180, 220, 150, 100]})
