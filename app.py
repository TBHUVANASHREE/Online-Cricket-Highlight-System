import streamlit as st
import json
import time

st.set_page_config(layout="wide")
st.title("🏏 AI Cricket Highlight Dashboard")

placeholder = st.empty()

def format_event(event):
    if event == "SIX":
        return "🔥 SIX!"
    elif event == "FOUR":
        return "✨ FOUR!"
    elif event == "WICKET":
        return "🚨 WICKET!"
    return event


while True:
    try:
        with open("highlights.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    # ✅ SORT PROPERLY
    data = sorted(data, key=lambda x: (x["over"], x["ball"]))

    with placeholder.container():
        st.subheader("🎬 Live Highlights")

        if len(data) == 0:
            st.info("No highlights yet...")

        for h in reversed(data[-10:]):
            st.markdown(f"""
            **{h['batsman']}**  
            {format_event(h['event'])}  
            Over {h['over']}.{h['ball']}  
            ⭐ Score: {h['score']} | Excitement: {h['excitement']}
            """)

    time.sleep(1)