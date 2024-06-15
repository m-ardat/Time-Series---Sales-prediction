# Импорт библиотек
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

tuple_drugs = ('СУПРАСТИН', 'ТЕРАФЛЮ', 'ИНГАВИРИН', 'НУРОФЕН', 'АРБИДОЛ',
              'МИРАМИСТИН', 'НИМЕСИЛ', 'КАГОЦЕЛ', 'МАКСИКОЛД', 'КЕТАНОВ',
              )
MAE_total = [56.65, 213.65, 48.67, 162.07, 118.88, 103.36, 170.07, 82.87, 171.73, 58.08]
WAPE_total = [9.94, 7.31, 16.41, 20.71, 15.3, 17.89, 8.13, 24.31, 10.35, 10.14]
BIAS_total = [0.81, 55.6, 17.19, 53.33, -70.47, -90.75, -118.32, -78.66, -51.92, -19.7]
dict_total_drugs = {'drug': tuple_drugs,
                    'MAE': MAE_total,
                    'WAPE': WAPE_total,
                    'BIAS': BIAS_total
                    }

df_us_drug = pd.DataFrame(dict_total_drugs)

# Название
st.title("Предсказание продаж товаров из ассортимента аптек")
# Добавляем боковую панель слева
st.sidebar.title("Выберите товар из списка")
# Добавляем кнопку-переключатель в боковую панель слева
preparation = st.sidebar.radio(label="Выберите препарат:",
                               options=[*tuple_drugs, 'ВСЕ'],
                               index=0
                               )
st.sidebar.markdown('Данный сервис демонстрирует прогнозы продаж некоторых товаров,'
                    'полученных моделью `CatboostRegressor`')
# Создаем график
if preparation == 'ВСЕ':
    st.subheader("Полученные метрики по товарам")
    fig1 = px.bar(dict_total_drugs, x='MAE', y='drug')
    st.plotly_chart(fig1)
    fig2 = px.bar(dict_total_drugs, x='WAPE', y='drug')
    fig2.update_traces(marker_color='gray')
    st.plotly_chart(fig2)
    fig3 = px.bar(dict_total_drugs, x='BIAS', y='drug')
    fig3.update_traces(marker_color='green')
    st.plotly_chart(fig3)
else:
    # загружаем картинку
    img = Image.open(f"plotly_gr/{preparation}.png")
    # отображаем картинку используя streamlit
    st.image(img, use_column_width=True)
    st.subheader('Метрики')
    # Фильтруем данные по выбранному препарату
    selected_drug_data = df_us_drug[df_us_drug['drug'] == preparation]
    selected_drugtable = selected_drug_data[['drug', 'MAE', 'WAPE', 'BIAS']]
    st.table(selected_drugtable)

