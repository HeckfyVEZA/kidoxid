import streamlit as st
import math
from gabars import gabars_choose
st.set_page_config(layout='wide')
st.header("Расчёт площади живого сечения для клапанов КИД® и ОКСИД®")
st.markdown('---')
# st.subheader("Расчёт производится при помощи следующей формулы:")
# formulas = st.columns(2)
# formulas[0].write('')
# formulas[0].write('')
# formulas[0].write('')
# formulas[0].write('')
# formulas[0].latex(r'''S = \frac{Vд \cdot Sд \cdot kпр}{\left(\frac{2 \cdot ΔP}{ρ}\right)^{0.5}}''')
# formulas[1].markdown('''<i><b>Где:</b></i>''', unsafe_allow_html=True)
# formulas[1].markdown('''<i><b>Vд</b> – скорость потока воздуха в открытой двери при закрытом клапане, м/с;</i>''', unsafe_allow_html=True)
# formulas[1].markdown('''<i><b>Sд</b> – площадь открытой двери, м²;</i>''', unsafe_allow_html=True)
# formulas[1].markdown('''<i><b>kпр</b> – коэффициент, учитывающий конструктивные особенности клапана. Для КИД® его можно принять равным 1,7;</i>''', unsafe_allow_html=True)
# formulas[1].markdown('''<i><b>ΔP</b> – перепад давления на клапане при закрытой двери, соответствует избыточному давлению в тамбур-шлюзе, Па;</i>''', unsafe_allow_html=True)
# formulas[1].markdown('''<i><b>ρ</b> – плотность воздуха, кг/м³</i>''', unsafe_allow_html=True)
# st.markdown('---')
p_norm = 101325
M_air = 28.98/1000
R = 8.314
def ro_air(t_vozd):
    t_vozd = float(t_vozd.replace(',', '.'))
    ro = (p_norm * M_air)/(R * (t_vozd + 273.15))
    return round(ro, 3)
def life_s(V, S, k, dP, ro):
    V = float(V.replace(',', '.'))
    S = float(S.replace(',', '.'))
    k = float(k.replace(',', '.'))
    dP = float(dP.replace(',', '.'))
    ro = float(ro.replace(',', '.'))
    return math.ceil((V * S * k)/(((2*dP)/ro)**.5)*1000)/1000
cols_input = st.columns(4)
st.session_state.valve = cols_input[0].selectbox('Клапан', options=('КИД', 'ОКСИД'))
if st.session_state.valve == 'КИД':
    st.session_state.kid_option_0 = cols_input[0].selectbox('Тип клапана', options=(1,2,3))
    kid_otions_info = {1: "клапан стенового типа, механизм настройки давления открытия клапана находится внутри корпуса", 2: "клапан канального типа, механизм настройки давления открытия клапана находится внутри корпуса", 3: "клапан канального типа, механизм настройки давления открытия клапана находится снаружи корпуса"}
    cols_input[0].info(kid_otions_info[st.session_state.kid_option_0])
    st.session_state.kid_option_1 = cols_input[0].selectbox('Исполнение', options=('Н', 'К', 'В', 'КВ'))
else:
    st.session_state.oksid_option_0 = cols_input[0].selectbox('Тип клапана', options=('канальный', 'стеновой'))
    st.session_state.oksid_option_1 = cols_input[0].selectbox('Устройство воздухоприёмное', options=('РОН110', 'РОН120','РОН130','0'), index=3)
    st.session_state.oksid_option_2 = cols_input[0].selectbox('Монтажная рама', options=('МРЗ' if st.session_state.oksid_option_0 == 'стеновой' else 'МРП','0'), index=1)
    st.session_state.oksid_option_3 = cols_input[0].selectbox('Исполнение', options=('Н', 'К', 'МС', 'МСК'))
st.session_state.T = cols_input[1].text_input('Температура воздуха, °С', value='0')
st.session_state.V = cols_input[1].text_input('Скорость воздуха в открытой двери при закрытом клапане, м/с', value='0')
st.session_state.S = cols_input[3].text_input('Площадь открытой двери, м²', value='0')
if  st.session_state.valve == 'КИД':
    if st.session_state.kid_option_0 == 1:
        cols_input[3].image('https://i.postimg.cc/NMpLHNTW/kid1.png')
    elif st.session_state.kid_option_0 == 2:
        cols_input[3].image('https://i.postimg.cc/RZ5f9DTR/kid2.png')
    elif st.session_state.kid_option_0 == 3:
        cols_input[3].image('https://i.postimg.cc/CxcqDxgv/kid3.png')
else:
    if st.session_state.oksid_option_0 == 'канальный':
        cols_input[3].image('https://i.postimg.cc/cHRYvM43/oxid-canal.png')
    else:
        cols_input[3].image('https://i.postimg.cc/7Yd6yJqr/oxid-wall.png')
st.session_state.dP = cols_input[2].text_input('Избыточное давление в тамбур-шлюзе, Па', value='0')
st.session_state.kpr = cols_input[2].text_input('Коэффициент, учитывающий конструктивные особенности клапана', value='1.7')
try:
    ro = ro_air(st.session_state.T)
    st.session_state.lifeS = life_s(st.session_state.V, st.session_state.S, st.session_state.kpr, st.session_state.dP, str(ro))
    st.info(f'Площадь живого сечения: {str(st.session_state.lifeS)} м²')
    try:
        if st.session_state.valve == 'КИД':
            st.dataframe(list(map(lambda x:  x.split(" | "), gabars_choose(st.session_state.valve, st.session_state.lifeS, valve_type=st.session_state.kid_option_0, blya=st.session_state.kid_option_1))))
        else:
            st.dataframe(list(map(lambda x:  x.split(" | "), gabars_choose(st.session_state.valve, st.session_state.lifeS, ron=st.session_state.oksid_option_1, isp=st.session_state.oksid_option_3, mrp=st.session_state.oksid_option_2, kan_wall=st.session_state.oksid_option_0))))
    except Exception as err:
        st.write(err)
except Exception as error:
    pass