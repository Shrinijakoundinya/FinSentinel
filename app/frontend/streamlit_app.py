import streamlit as st
import re

st.set_page_config(page_title='FinSentinel — Demo', layout='centered')
st.title('FinSentinel — AI Investor Safety Net (Demo)')
st.markdown('Paste a suspicious investment message below and click Analyze. This is a prototype: no real PII should be used.')

EXAMPLE_MESSAGES = [
    "Guaranteed 200% returns in 7 days! Buy XYZ now 🚀",
    "This insider tip will multiply your money. Call +91-XXXXXXXXXX",
    "Mutual fund NAV update: ABC Fund - please read the factsheet before investing.",
    "IPO allotment confirmed. Check your demat. No worries."
]

def classify_message(msg: str):
    # Simple heuristic classifier (MVP)
    score = 0
    rationale = []
    text = msg.lower()
    keywords_scam = ['guaranteed', 'guarantee', 'no risk', 'zero risk', 'get rich', 'multibagger', '2x', '200%', 'insider', 'call', 'contact', 'buy now', 'urgent', 'only today', 'exclusive']
    for kw in keywords_scam:
        if kw in text:
            score += 2
            rationale.append(f'Found suspicious keyword: "{kw}"')
    # urgency patterns
    if re.search(r'\b(buy now|act now|limited time|only today|urgent)\b', text):
        score += 2
        rationale.append('Urgent call-to-action detected')
    # numeric promises
    if re.search(r'\b(\d{2,3}%|\d+x|\d+x)\b', text):
        score += 2
        rationale.append('Unrealistic returns / percent promise')
    # contact-sharing (phone, payment links)
    if re.search(r'\+?\d{6,}|upi|paytm|phone|contact', text):
        score += 1
        rationale.append('Contact/payment info present — suspicious')
    # short-circuit decision
    if score >= 5:
        verdict = '⚠️ High Risk — Likely Scam'
    elif score >= 3:
        verdict = '⚠️ Medium Risk — Review Carefully'
    else:
        verdict = '✅ Low Risk / Likely Safe'
    return verdict, rationale

st.subheader('Paste message to analyze')
user_msg = st.text_area('Message', value=EXAMPLE_MESSAGES[0], height=120)

if st.button('Analyze'):
    verdict, rationale = classify_message(user_msg)
    st.markdown(f'### Result: {verdict}')
    st.markdown('**Rationale (highlights):**')
    for r in rationale:
        st.write('- ' + r)
    st.info('Disclaimer: This prototype is for demonstration only. Not financial advice.')

st.markdown('---')
st.subheader('Example messages')
for m in EXAMPLE_MESSAGES:
    st.write('- ' + m)
