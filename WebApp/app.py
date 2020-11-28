import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title='На пульсе ❤️ Fit_predict  ❤️ Держим руку на пульсе ❤️ Цифровой прорыв', page_icon = 'http://134.122.83.163/heart/heart_logo.png', layout = 'wide', initial_sidebar_state = 'auto')

st.markdown("![](http://134.122.83.163/heart/heart114.png) ")

st.sidebar.subheader("Домашнее хозяйство")

water = st.sidebar.selectbox('Источник воды', 
    ['перекачиваемая вода','артезианский колодец','скважина района',
    'скважина домохозяйства','бак с водой',
    'вода в бутылках / таре','река','Undefined'], key='1')

bycicle = st.sidebar.selectbox('Велосипед', 
    ['есть','нет'], key='2')

income = st.sidebar.number_input(label="Ежемесячный доход", value=18000, key=3)

sq = st.sidebar.number_input(label="Площадь жилья", value=50, key=3)

rooms = st.sidebar.number_input(label="Число комнат", value=2, key=3)

pc = st.sidebar.selectbox('ПК', 
    ['есть','нет'], key=4)

pc_count = st.sidebar.number_input(label="Число ПК", value=1, key=3)

income_food = st.sidebar.selectbox('Часть дохода на еду', 
    ['1/2 (половина)','2/3','1/3','1/10 или менее','почти все'], key=4)

garage = st.sidebar.selectbox('ПК', 
    ['есть','нет'], key=5)

farm = st.sidebar.selectbox('Ферма', 
    ['есть','нет'], key=5)

fridge = st.sidebar.selectbox('Холодильник', 
    ['есть','нет'], key=5)

income_food = st.sidebar.selectbox('Достаток по срав с друг', 
    ['очень низкий','низкий','средний','относительно высокий','очень высокий'], key=6)

money_food = st.sidebar.number_input(label="Деньги на пищу", value=100, key=7)

dacha = st.sidebar.number_input(label="Площадь дачи", value=100, key=7)

auto = st.sidebar.number_input(label="Число авто", value=1, key=7)

cooking_out = st.sidebar.number_input(label="Готовка вне дома, месяц", value=1, key=7)

tv = st.sidebar.number_input(label="Число телев ", value=1, key=7)

lavka = st.sidebar.selectbox('Лавка', 
    ['нет','есть'], key=5)


chart_df = pd.DataFrame()
chart_df['Риск, %'] = [11, 7, 18, 16, 22]
chart_df['Диагноз'] = ['Артериальная гипертензия','ОНМК','Сердечная недостаточность',
 'Стенокардия, ИБС, инфаркт миокарда',
 'Прочие заболевания сердца']

fig = px.bar(chart_df, x='Риск, %', 
             y='Диагноз', 
             title="Вероятность развития заболеваний сердечно-сосудистой системы",
             range_x=(0, 100),
             color='Риск, %',
             width=1500,
             height=700
            )

st.plotly_chart(fig)

