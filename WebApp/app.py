import joblib
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title='На пульсе ❤️ Fit_predict  ❤️ Держим руку на пульсе ❤️ Цифровой прорыв', page_icon = 'http://134.122.83.163/heart/heart_logo.png', layout = 'wide', initial_sidebar_state = 'auto')

# load trained models and selected features

diagnoses = [
'Артериальная гипертензия',
'ОНМК',
'Прочие заболевания сердца',
'Сердечная недостаточность',
'Стенокардия, ИБС, инфаркт миокарда'
]


models = dict()
feats = dict()
for d in diagnoses:
    models[d] = joblib.load('models/Дом хоз/'+ d +'_Дом хоз')
    feats[d] = list(pd.read_excel('feats/Дом хоз/'+ d +'_Дом хоз.xlsx')['cols'].values)

st.markdown("![](http://134.122.83.163/heart/heart114.png) ")

st.sidebar.subheader("Домашнее хозяйство")

water = st.sidebar.selectbox('Источник воды', 
    ['перекачиваемая вода','артезианский колодец','скважина района',
    'скважина домохозяйства','бак с водой',
    'вода в бутылках / таре','река'], key='1')

bycicle = st.sidebar.selectbox('Велосипед', 
    ['есть','нет'], key='2')

income = st.sidebar.number_input(label="Ежемесячный доход", value=18000, key='3')

sq = st.sidebar.number_input(label="Площадь жилья", value=50, key='4')

rooms = st.sidebar.number_input(label="Число комнат", value=2, key='5')

pc = st.sidebar.selectbox('ПК', 
    ['есть','нет'], key='6')

pc_count = st.sidebar.number_input(label="Число ПК", value=1, key='7')

income_food = st.sidebar.selectbox('Часть дохода на еду', 
    ['1/2 (половина)','2/3','1/3','1/10 или менее','почти все'], key='8')

garage = st.sidebar.selectbox('ПК', 
    ['есть','нет'], key='9')

farm = st.sidebar.selectbox('Ферма', 
    ['есть','нет'], key='10')

fridge = st.sidebar.selectbox('Холодильник', 
    ['есть','нет'], key='11')

income_food = st.sidebar.selectbox('Достаток по срав с друг', 
    ['очень низкий','низкий','средний','относительно высокий','очень высокий'], key='12')

money_food = st.sidebar.number_input(label="Деньги на пищу", value=100, key='13')

dacha = st.sidebar.number_input(label="Площадь дачи", value=100, key='14')

auto = st.sidebar.number_input(label="Число авто", value=1, key='15')

cooking_out = st.sidebar.number_input(label="Готовка вне дома, месяц", value=1, key='16')

tv = st.sidebar.number_input(label="Число телев ", value=1, key='17')

lavka = st.sidebar.selectbox('Лавка', 
    ['нет','есть'], key='18')

def txt2bin(txt):
    if txt == 'есть':
        return 1
    else:
        return 0

if st.button('Рассчитать вероятность'):

    item = {}

    item['Велосипед'] = txt2bin(bycicle)
    item['Гараж'] = txt2bin(garage)
    item['Готовка вне дома, месяц'] = cooking_out
    item['Деньги на пищу'] = money_food
    item['Достаток по срав с друг'] = income_food
    item['Ежемес доход'] = income
    item['Источник воды'] = water
    item['Лавка'] = txt2bin(lavka)
    item['ПК'] = txt2bin(pc)
    item['Площадь дачи'] = dacha
    item['Площадь жилья'] = sq
    item['Ферма'] = txt2bin(farm)
    item['Холодильник'] = txt2bin(fridge)
    item['Часть дохода на еду'] = income_food
    item['Число ПК'] = pc_count
    item['Число авто'] = auto
    item['Число комнат'] = rooms
    item['Число телев'] = tv

    #prepare data to fit the model
    df = pd.DataFrame(item, index=[0])

    data_diagnos = []
    data_risk = []

    for m in models:
        data_diagnos.append(m)
        data_risk.append(models[m].predict_proba(feats[m])[1] * 100)

    chart_df = pd.DataFrame()
    chart_df['Риск, %'] = data_risk
    chart_df['Диагноз'] = data_diagnos

    fig = px.bar(chart_df, x='Риск, %', 
                y='Диагноз', 
                title="Вероятность развития заболеваний сердечно-сосудистой системы",
                range_x=(0, 100),
                color='Риск, %',
                width=1500,
                height=600
                )

    st.plotly_chart(fig)
    