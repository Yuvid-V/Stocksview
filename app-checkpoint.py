import streamlit as st
import analysis.analysis_one as analysis_one
import analysis.analysis_multiple as analysis_multiple
import forecasting.forecasting as forecasting
import forecasting.advance_forecasting as advance_forecasting
import pandas as pd
import guide

st.set_page_config(layout="wide")

ticker_list = pd.read_csv("scrapping_ticker/Ticker_list.csv")


section = st.sidebar.radio(
    "**Select Section:**", 
    options=["📊 Stock Analysis","🔮 Stock Forecasting","📈 Expert Details"])
#st.sidebar.divider()

ticker= ticker_list['Ticker'].values
ticker_map = {ticker: ticker + '.JK' for ticker in ticker}
display_names = list(ticker_map.keys())

selected_display_name = st.sidebar.selectbox('Select Stock Symbol', options=display_names , index=1)
stock_symbol = ticker_map[selected_display_name]




if section == "📊 Stock Analysis" : 

    tab1, tab2 = st.tabs(["Single Stock Analysis", "Multiple Stock Analysis"])

    with tab1 :

        analysis_one.Analysis_stock_data(stock_symbol=stock_symbol)
    
    with tab2 : 
         
      selected_display_names = st.sidebar.multiselect('Select Stock Symbols', options=display_names , max_selections=4 , default=display_names[:2])

      selected_symbols = [ticker_map[name] for name in selected_display_names]

      analysis_multiple.multiply_alalysis(selected_symbols)

elif section == "🔮 Stock Forecasting":

    tab1 , tab2 = st.tabs(["Forecast" , "Documentation"])

    with tab1 : 
        forecasting.Forecasting(stock_symbol = stock_symbol)
    with tab2 : 
        guide.Forecast()


elif section == '⚙️ Customize LSTM Parameters':
    advance_forecasting.Forecasting(stock=stock_symbol)
elif section == '📈 Expert Details' :

    st.title(":green[Expert Deails]")
    st.image("experts/1.jpg", caption="Expert 1")
    st.text("Teaching Stock Trading/Future & Options trading / Forex Trading / Crypto trading is an art which many ")
    st.text("mentors lack. I teach my students from zero level to advance level each and every concept and also provide")
    st.text("practical demonstration of my teachings in live market sessions,which boost their confidence as they know the market concepts")
    st.text("9785685478")
    st.image("experts/2.jpg", caption="Expert 2")
    st.text("I've worked as a professional investing and trading mentor for more than")
    st.text("2000+ students in the past 4 years. Apart from that I'm involved in")
    st.text("individual mentoring of students lately where I conduct a 1-2 month program")
    st.text("8759687548")
    st.image("experts/3.jpg", caption="Expert 3")
    st.text("I am an Analyst/Trader/Trainer with a Master's degree in Economics &")
    st.text("more than 20 years of experience in the Global Financial Markets with")
    st.text("some of the leading organizations in India and the UAE. My role has")
    st.text("9632145875")
else : 
    st.title(":red[select section]")








