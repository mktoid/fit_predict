import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='На пульсе ❤️ Fit_predict  ❤️ Держим руку на пульсе ❤️ Цифровой прорыв', page_icon = 'http://134.122.83.163/heart/heart_logo.png', layout = 'wide', initial_sidebar_state = 'auto')

st.markdown("![](http://134.122.83.163/heart/heart114.png) ")

st.sidebar.subheader("Группы признаков")
group = st.sidebar.radio('', ('Домашнее хозяйство', 'Территориальные', 'Продукты', 'Элементы', 'Традиционные'))

st.title("Домашнее хозяйство")

water = st.selectbox('Источник воды', 
    ['перекачиваемая вода','артезианский колодец','скважина района',
    'скважина домохозяйства','Undefined','бак с водой',
    'вода в бутылках / таре','река'], key='1')

bycicle = st.selectbox('Велосипед', 
    ['есть','нет'], key='2')

income = st.number_input(label="Ежемесячный доход", value=18000, key=3)

sq = st.number_input(label="Площадь жилья", value=50, key=3)

rooms = st.number_input(label="Число комнат", value=2, key=3)

pc = st.selectbox('ПК', 
    ['есть','нет'], key='4')

pc_count = st.number_input(label="Число ПК", value=1, key=3)

