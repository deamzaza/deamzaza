import streamlit as st
import datetime
from utils import trainer

st.set_page_config(page_title="Trading Bot RL Dashboard", layout="wide")

def main():
    st.title("📈 AI Trading Bot Dashboard")
    
    st.sidebar.header("⚙️ Settings")
    trading_pair = st.sidebar.text_input("Trading Pair", "BTCUSDT")
    start_date = st.sidebar.date_input("Start Date", datetime.date(2021, 1, 1))
    end_date = st.sidebar.date_input("End Date", datetime.date.today())
    mode = st.sidebar.selectbox("Mode", ["Backtest", "Live Trade"])

    st.markdown("---")
    
    if st.button("🚀 Run Bot"):
        st.success(f"Running in {mode} mode for {trading_pair} from {start_date} to {end_date}")

        # Demo training result
        with st.spinner("Training AI..."):
            reward = trainer.train(trading_pair, start_date, end_date, mode)
            st.metric(label="📈 Total Reward", value=f"{reward:.2f}")

        st.line_chart([1, 1.5, 2.2, 1.7, 2.9])  # Placeholder chart

if __name__ == "__main__":
    main()
