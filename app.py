import streamlit as st
from streamlit_folium import st_folium
from geopy.distance import geodesic
from okumura_hata import calculate_path_loss, create_line_plot
from map_folium import create_map

### STREAMLIT
st.set_page_config(page_title='Rádio Acesso', page_icon=':satellite:')

st.markdown("### :satellite: Predição de Perda de Potência")
st.text('')
column_1, column_2 = st.columns(2)

with column_1:
    st.markdown("##### Estação Rádio Base")
    lat_erb = st.text_input('Latitude' , '-2.58031')
    lon_erb = st.text_input('Longitude', '-44.2372')

with column_2:
    st.markdown("##### Destino")
    lat_dest = st.text_input('Latitude' , '-2.5199')
    lon_dest = st.text_input('Longitude', '-44.1396')

with st.sidebar:
    st.subheader("Entre com as informações")
    types = ('Cidade Grande', 'Suburbio', 'Zona Rural (Quasi-Open)', 'Zona Rural (Area Aberta)')
    f  = st.number_input(label = "Entre com a Frequência (MHz)", value=900)
    Hb = st.number_input(label = "Entre com a altura da antena da estação base (m)", value=40)
    Hm = st.number_input(label = "Entre com a altura da antena do terminal móvel (m)", value=1.5)
    dp  = st.number_input(label = "Entre com a distância (km)", value=15)
    t  = st.selectbox("Entre com o modelo de região", types)

ERB, DESTINY = (float(lat_erb), float(lon_erb)), (float(lat_dest), float(lon_dest))
map_folium = create_map(ERB, DESTINY, dp)

d = geodesic(ERB, DESTINY).km
st_map = st_folium(map_folium, height = 450, width = 725)

st.warning(f'Distância entre os pontos é de {round(d, 2)}km')
if st.button('Calcular'):
    if d > dp:
        st.error("A distância entre os pontos está fora do range de acesso")
    elif f > 2200 or f < 150:
        st.error("A frequencia permitida está entre 150MHz e 2200MHz")
    else:
        path_loss = calculate_path_loss(f, Hb, Hm, d, types.index(t))
        table = create_line_plot(f, Hm, Hb, dp)
    
        st.info(f'A perda de potência localizada é de {round(path_loss, 2)} decibéis')
        st.markdown("#### Gráfico de perda de potência pela distância")
        st.line_chart(table)
