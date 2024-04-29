import streamlit as st
import pandas as pd
import numpy as np

st.title('Invest Smart Flex Account Value Projection')

age = st.number_input('**How old are you?**', value=30, step=1, min_value=18, max_value=70)
st.write('I am ', age, " years old this year")

invest_term = st.selectbox(
    '**How long do you want to invest?**',
    ('10 Years', '15 Years', '20 Years'))

st.write('I am investing for ', invest_term)

if invest_term == '10 Years':
    payment_term = st.selectbox(
        '**How long do you want to pay?**',
        ('5 Years', '6 Years', '7 Years', '8 Years', '9 Years', '10 Years'))

elif invest_term == '15 Years':
    payment_term = st.selectbox(
        '**How long do you want to pay?**',
        ('8 Years', '9 Years', '10 Years', '11 Years', '12 Years', '13 Years', '13 Years', '14 Years', '15 Years'))

else:
    payment_term = st.selectbox(
        '**How long do you want to pay?**',
        ('9 Years', '10 Years', '11 Years', '12 Years', '13 Years', '13 Years', '14 Years', '15 Years', '16 Years', '17 Years', '18 Years', '19 Years', '20 Years'))

st.write('I am paying for ', payment_term)

yearly_invest_amount = st.number_input('**How much do you want to invest yearly?**', value=12000, step=1200, min_value=2400)
st.write('I am investing $', yearly_invest_amount, " every year")

fund = st.selectbox(
    '**What fund do you want to invest in?**',
    ('Allianz Income & Growth (Dividend Payout)', 'Fundsmith Equity Fund (Wealth Accumulation)'))
st.write('I am investing in ', fund)

if fund == 'Fundsmith Equity Fund (Wealth Accumulation)':
    roi = st.slider('**Projected fund growth %** (Past performance - Fundsmith Equity Fund: 15% | Allianz Income & Growth: 2%)', 0, 15, 15)
    st.write('Fund projected to grow at ', roi, '%')

    dividend = st.slider('**Projected fund dividend payout %** (Past performance - Fundsmith Equity Fund: 0% | Allianz Income & Growth: 8%)', 0, 10, 0)
    st.write('Fund dividend payout projected at ', dividend, '%')
else:
    roi = st.slider('**Projected fund growth %** (Past performance - Fundsmith Equity Fund: 15% | Allianz Income & Growth: 2%)', 0, 15, 2)
    st.write('Fund projected to grow at ', roi, '%')

    dividend = st.slider('**Projected fund dividend payout %** (Past performance - Fundsmith Equity Fund: 0% | Allianz Income & Growth: 8%)', 0, 10, 8)
    st.write('Fund dividend payout projected at ', dividend, '%')

st.write('')
st.write('*Disclaimer - Past performance of a particular fund is not an indication of its future performance. The projection below is based on past performance and non-guaranteed as all investment are subjected to market risks.*')

def calculate_bonus():
    if invest_term == '10 Years':
        if yearly_invest_amount < 9600:
            bonus = yearly_invest_amount * 0.15
        else:
            bonus = yearly_invest_amount * 0.3
    elif invest_term == '15 Years':
        if yearly_invest_amount < 7200:
            bonus = yearly_invest_amount * 0.25
        else:
            bonus = yearly_invest_amount * 0.5
    else:
        if yearly_invest_amount < 4800:
            bonus = yearly_invest_amount * 0.4
        else:
            bonus = yearly_invest_amount * 0.8
    return int(bonus)

st.write('')
bonus_text = '💰 First Year Start-up Bonus: $' + f'{calculate_bonus():,}'
bonus_tag = '<p style="font-family:sans-serif; font-size: 24px;">'+bonus_text+'</p>'
st.markdown(bonus_tag, unsafe_allow_html=True)

df = pd.DataFrame(columns=['Age','Deposit','Start-up Bonus','Loyalty Bonus','Account Value (After Fees)','Yearly Dividends','Monthly Dividends','Yearly Fees', 'Monthly Fees'])

if invest_term == '10 Years':

    for i in range(10):

        payment_term_int = int(payment_term.replace(' Years', ''))
        if payment_term_int <= i:
            deposit = 0
        else:
            deposit = yearly_invest_amount
        
        if i > 0:
            su_bonus = 0
        else:
            su_bonus = calculate_bonus()
        
        if i == 0:
            loyalty_bonus = 0
            total_deposit = (deposit + su_bonus)
            returns = total_deposit + (total_deposit *(roi/100))
            fees = returns * 0.02
            actual_returns = returns - fees
        else:
            if deposit != 0:
                loyalty_bonus = int(df.iloc[i-1]['Account Value (After Fees)']) * 0.002
            else:
                loyalty_bonus = 0
            total_deposit = int(df.iloc[i-1]['Account Value (After Fees)']) + deposit
            returns = total_deposit + (total_deposit *(roi/100))
            fees = returns * 0.02
            actual_returns = returns + loyalty_bonus - fees
        monthly_fees = fees/12

        yearly_dividends = actual_returns * (dividend/100)
        monthly_dividends = yearly_dividends/12

        df_temp = {'Age':age+i, 'Deposit':deposit, 'Start-up Bonus':su_bonus, 'Account Value (After Fees)': actual_returns, 'Yearly Fees':fees, 'Yearly Dividends':yearly_dividends, 'Monthly Dividends':monthly_dividends, 'Loyalty Bonus':loyalty_bonus, 'Monthly Fees':monthly_fees}
        df = df._append(df_temp, ignore_index=True)

if invest_term == '15 Years':

    for i in range(15):

        payment_term_int = int(payment_term.replace(' Years', ''))
        if payment_term_int <= i:
            deposit = 0
        else:
            deposit = yearly_invest_amount
        
        if i > 0:
            su_bonus = 0
        else:
            su_bonus = calculate_bonus()
        
        if i == 0:
            loyalty_bonus = 0
            total_deposit = (deposit + su_bonus)
            returns = total_deposit + (total_deposit *(roi/100))
            fees = returns * 0.02
            actual_returns = returns - fees
        else:
            if deposit != 0:
                loyalty_bonus = int(df.iloc[i-1]['Account Value (After Fees)']) * 0.002
            else:
                loyalty_bonus = 0
            total_deposit = int(df.iloc[i-1]['Account Value (After Fees)']) + deposit
            returns = total_deposit + (total_deposit *(roi/100))
            if i < 10:
                fees = returns * 0.02
            else:
                fees = returns * 0.016
            actual_returns = returns + loyalty_bonus - fees

        monthly_fees = fees/12

        yearly_dividends = actual_returns * (dividend/100)
        monthly_dividends = yearly_dividends/12

        df_temp = {'Age':age+i, 'Deposit':deposit, 'Start-up Bonus':su_bonus, 'Account Value (After Fees)': actual_returns, 'Yearly Fees':fees, 'Yearly Dividends':yearly_dividends, 'Monthly Dividends':monthly_dividends, 'Loyalty Bonus':loyalty_bonus, 'Monthly Fees':monthly_fees}
        df = df._append(df_temp, ignore_index=True)

if invest_term == '20 Years':

    for i in range(20):

        payment_term_int = int(payment_term.replace(' Years', ''))
        if payment_term_int <= i:
            deposit = 0
        else:
            deposit = yearly_invest_amount
        
        if i > 0:
            su_bonus = 0
        else:
            su_bonus = calculate_bonus()
        
        if i == 0:
            loyalty_bonus = 0
            total_deposit = (deposit + su_bonus)
            returns = total_deposit + (total_deposit *(roi/100))
            fees = returns * 0.02
            actual_returns = returns - fees
        else:
            if deposit != 0:
                loyalty_bonus = int(df.iloc[i-1]['Account Value (After Fees)']) * 0.002
            else:
                loyalty_bonus = 0
            total_deposit = int(df.iloc[i-1]['Account Value (After Fees)']) + deposit
            returns = total_deposit + (total_deposit *(roi/100))
            if i < 10:
                fees = returns * 0.02
            else:
                fees = returns * 0.016
            actual_returns = returns + loyalty_bonus - fees

        monthly_fees = fees/12

        yearly_dividends = actual_returns * (dividend/100)
        monthly_dividends = yearly_dividends/12

        df_temp = {'Age':age+i, 'Deposit':deposit, 'Start-up Bonus':su_bonus, 'Account Value (After Fees)': actual_returns, 'Yearly Fees':fees, 'Yearly Dividends':yearly_dividends, 'Monthly Dividends':monthly_dividends, 'Loyalty Bonus':loyalty_bonus, 'Monthly Fees':monthly_fees}
        df = df._append(df_temp, ignore_index=True)

df["Age"] = df["Age"].astype(int)
df["Deposit"] = df["Deposit"].astype(int)
df["Start-up Bonus"] = df["Start-up Bonus"].astype(int)
df["Account Value (After Fees)"] = df["Account Value (After Fees)"].astype(int)
df["Yearly Fees"] = df["Yearly Fees"].astype(int)
df["Monthly Fees"] = df["Monthly Fees"].astype(int)
df["Yearly Dividends"] = df["Yearly Dividends"].astype(int)
df["Monthly Dividends"] = df["Monthly Dividends"].astype(int)
df["Loyalty Bonus"] = df["Loyalty Bonus"].astype(int)

df_table = df.drop(['Yearly Fees', 'Monthly Fees'], axis=1)
st.table(df_table)

capital = df['Deposit'].sum()
capital_text = '💲 Total Capital: $' + f'{capital:,}'
capital_tag = '<p style="font-family:sans-serif; font-size: 24px;">'+capital_text+'</p>'
st.markdown(capital_tag, unsafe_allow_html=True)

if dividend > 0:
    total_dividends = df['Yearly Dividends'].sum()
    dividend_text = '💵 Total Dividends Payout: $' + f'{total_dividends:,}'
    dividend_tag = '<p style="font-family:sans-serif; font-size: 24px;">'+dividend_text+'</p>'
    st.markdown(dividend_tag, unsafe_allow_html=True)

chart_data = df[['Account Value (After Fees)', 'Yearly Fees']]
st.bar_chart(chart_data)
