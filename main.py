import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import base64
import numpy as np
import pandas as pd
from Monsters import *



st.title('Monster Builder')
st.write("""
This app makes it possible to create basic monster statblock depends on party strength
***
""")

st.sidebar.title("Please select party stats and type of monster")
difficulty_modif = st.sidebar.slider('Combat difficulty', 0.1, 2.0, 1.0, step=0.05)
party_size = st.sidebar.number_input('Party size', step=1, min_value=1)
party_lvl = st.sidebar.number_input('Average level', step=1, min_value=1)
GB_lvl = st.sidebar.number_input('Average global buff level', step=1, min_value=0)
monster_num = st.sidebar.number_input('Number of monsters', step=1, min_value=1)
monster_type = st.sidebar.selectbox('Moster type', StatPriorBook.keys())
coml = party_size*party_lvl*(1.325**GB_lvl)
dng = round(coml / monster_num)*difficulty_modif
Monster = Monster(dng, StatPriorBook[monster_type], monster_type)
st.write("###   HP:  "+str(Monster.HP)+"  AC:  "+str(Monster.AC))
d = {
    'Str': [Monster.Str, Monster.Modifier(Monster.Str)],
    'Dex': [Monster.Dex, Monster.Modifier(Monster.Dex)],
    'Con': [Monster.Con, Monster.Modifier(Monster.Con)],
    'Int': [Monster.Int, Monster.Modifier(Monster.Int)],
    'Wis': [Monster.Wis, Monster.Modifier(Monster.Wis)],
    'Cha': [Monster.Cha, Monster.Modifier(Monster.Cha)],
}
df = pd.DataFrame(data=d, index=["Stat", "Modifier"])
st.dataframe(df, width=900, height=None, use_container_width=False)
st.write("###   Damage on hit:  "+str(Monster.HitDamage))