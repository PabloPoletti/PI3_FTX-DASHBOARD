from cProfile import label
import ccxt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from PIL import Image
import math
import plotly.graph_objects as go
from datetime import datetime
import calendar

st.set_page_config(page_icon="📈", page_title="Crypto Dashboard")
exchange = ccxt.ftx()

# cambiar nombres por BTC solo por ej
symbol_list=['BTC/USD', 'ETH/USD', 'USDT/USD', 'AXS/USD', 'BNB/USD', 'XRP/USD', 'LTC/USD', 'MATIC/USD', 'SOL/USD', 'DOGE/USD']
timeframe_list=['1d','15s','1m', '5m', '15m', '1h',  '1w', '1M']
ema_list=[30,7,14,21,50,100,200]
#cant_dias=[30,60,90,180,365,730]
#agregar botones de varianza, volumen, etc?

#image = Image.open('IMAGEN.jpg') # IMAGEN


#st.image(image,use_column_width=True) # IMAGEN A USAR
def main_page():

            
            st.title('RESUMEN DE COTIZACIONES')
            
            #ftx= ccxt.ftx() # utilizo phemex Exchange Markets
            #=eleccion # simbolo de la moneda
            #timeframe=tiempo

            #now = datetime.utcnow()
            #unixtime = calendar.timegm(now.utctimetuple())
            #since = (unixtime - ((60*60*24*dias)/(288)) * 1000) # UTC timestamp in milliseconds)

            col1, col2,col3,col4,col5 = st.columns(5)
        
            variacion_diaria = exchange.fetch_ohlcv(symbol='BTC/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col1.metric('BTC', df_market_var_diaria['close'].values[-1], "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            variacion_diaria = exchange.fetch_ohlcv(symbol='ETH/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col2.metric('ETH', df_market_var_diaria['close'].values[-1], "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            variacion_diaria = exchange.fetch_ohlcv(symbol='BNB/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col3.metric('BNB', round((df_market_var_diaria['close'].values[-1]),2), "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            variacion_diaria = exchange.fetch_ohlcv(symbol='SOL/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col4.metric('SOL', round((df_market_var_diaria['close'].values[-1]),2), "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            variacion_diaria = exchange.fetch_ohlcv(symbol='MATIC/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col5.metric('MATIC', round((df_market_var_diaria['close'].values[-1]),4), "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            col1, col2,col3,col4,col5 = st.columns(5)

            variacion_diaria = exchange.fetch_ohlcv(symbol='USDT/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col1.metric('USDT', df_market_var_diaria['close'].values[-1], "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            variacion_diaria = exchange.fetch_ohlcv(symbol='AXS/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col2.metric('AXS', df_market_var_diaria['close'].values[-1], "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            variacion_diaria = exchange.fetch_ohlcv(symbol='XRP/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col3.metric('XRP', round((df_market_var_diaria['close'].values[-1]),2), "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            variacion_diaria = exchange.fetch_ohlcv(symbol='LTC/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col4.metric('LTC', round((df_market_var_diaria['close'].values[-1]),2), "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )

            variacion_diaria = exchange.fetch_ohlcv(symbol='DOGE/USD', timeframe='1d', limit=86400)
            df_market_var_diaria=pd.DataFrame(variacion_diaria, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            col5.metric('DOGE', round((df_market_var_diaria['close'].values[-1]),4), "{:.2%}".format(((((df_market_var_diaria['close'].values[-1])/(df_market_var_diaria['close'].values[-2]))-1))) )


def pageI():
            
            st.title('ANALISIS GRAFICO')

            col1, col2 , col3, col4 = st.columns(4)

            with col1:
                    eleccion = st.selectbox(
                    'Menu Crypto',
                    (symbol_list))
                    
            with col2:
                    tiempo = st.selectbox(
                    "Time Frame",
                    timeframe_list  )

            with col3:
                    ematime = st.selectbox(
                    "Cant. Dias Media Mov.",
                    ema_list  )

            with col4:
                    vartime = st.selectbox(
                    "Cant. Dias VAR y Desv. STD",
                    ema_list  )

            ohlcv = exchange.fetch_ohlcv(symbol=eleccion, timeframe=tiempo, since=None, limit=5000)
            df_market=pd.DataFrame(ohlcv, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            df_market['timestamp']=pd.to_datetime(df_market['timestamp'],unit='ms')
            df_market['SMA'] = df_market.close.rolling(ematime).mean()
            df_market['VAR'] = df_market.close.rolling(vartime).var()
            df_market['DESV'] = df_market.close.rolling(vartime).std()

            portada=eleccion.replace('/USD','')

            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.25, 
                        subplot_titles=(str("Valores Históricos de "+portada), 'Volumen'),
                        row_width=[0.4, 0.8])

            fig.add_trace(go.Candlestick(x=df_market['timestamp'],
                                                open = df_market['open'],
                                                high = df_market['high'],
                                                low = df_market['low'],
                                                close = df_market['close'], 
                                                name="OHLC"),row=1, col=1)

            fig.add_trace(go.Scatter(x=df_market['timestamp'], y=df_market['SMA'], name=(('Media Movil')),line=dict(color='purple', width=1)),row=1, col=1)


            fig.update(layout_xaxis_rangeslider_visible=True)

            df_market['color']=['red' if (x>y) else 'green' for x,y in zip(df_market['open'],df_market['close'])]

            fig.add_trace(go.Bar(
                x=df_market['timestamp'],
                y=df_market['volume'],
                marker_color = df_market['color'],
                name="Volumen"), row=2, col=1)

            fig.update_layout(height=600, width=800)
                         
            st.plotly_chart(fig)

            st.header("Varianza")
            fig2=go.Figure(data=[go.Scatter(x=df_market['timestamp'], 
                                            y=df_market['VAR'], 
                                            name=('Varianza'),
                                            showlegend=True,
                                            line=dict(color='Blue', 
                                            width=2))])
            fig2.update_layout(height=400, width=800)
            st.plotly_chart(fig2)

            st.header("Desviacion Estandar")
            fig3=go.Figure(data=[go.Scatter(x=df_market['timestamp'], 
                                            y=df_market['DESV'], 
                                            name=('STD'),
                                            showlegend=True,
                                            line=dict(color='Green', 
                                            width=2))])
            fig3.update_layout(height=400, width=800)

            st.plotly_chart(fig3)

# Side Bar #######################################################

symbol_list2=['BTC/USD', 'ETH/USD', 'USDT/USD', 'AXS/USD', 'BNB/USD', 'XRP/USD', 'LTC/USD', 'MATIC/USD', 'SOL/USD', 'DOGE/USD']

def pageII():

            '''
            # CALCULADORA EN USD
            '''

            st.title('CALCULADORA EN USD')
            
            eleccion2 = st.selectbox(
                    'Menu Crypto',
                    (symbol_list2))

            ohlcv2 = exchange.fetch_ohlcv(symbol=eleccion2, timeframe='1d', since=None, limit=86400)
            df_market_calculadora=pd.DataFrame(ohlcv2, columns=['timestamp','open', 'high', 'low', 'close','volume'])

            cantidad = st.number_input(label= str("Inserte una cantidad de "+eleccion2))
            st.write('RESULTADO: ',float(cantidad*(df_market_calculadora['close'].values[-1])),' USD')

            cantidad2 = st.number_input(label= str("Inserte una cantidad de USD"))

            st.write('RESULTADO: ',float(cantidad2)/((df_market_calculadora['close'].values[-1])), eleccion2)

def pageIII():


            st.title('CALCULADORA EN CRYPTOS')

            col1,col2 = st.columns(2)

            
            with col1:
                    eleccion3 = st.selectbox(
                        'Crypto 1',
                        (symbol_list2))
            ohlcv3 = exchange.fetch_ohlcv(symbol=eleccion3, timeframe='1d', since=None, limit=86400)
            df_market_calculadora2=pd.DataFrame(ohlcv3, columns=['timestamp','open', 'high', 'low', 'close','volume'])

        
            with col2: 
                    eleccion4 = st.selectbox(
                        'Crypto 2',
                        (symbol_list2))
            ohlcv4 = exchange.fetch_ohlcv(symbol=eleccion4, timeframe='1d', since=None, limit=86400)
            df_market_calculadora3=pd.DataFrame(ohlcv4, columns=['timestamp','open', 'high', 'low', 'close','volume'])

            #col1,col2 = st.columns(2)

            #with col1:
                    #cantidad3 = st.number_input(label= str("1.Inserte una cantidad de "+eleccion3))

            #with col2:
                    #cantidad4 = st.number_input(label= str("2.Inserte una cantidad de "+eleccion4))
            cantidad3=1
            cantidad4=1

            if cantidad3 != 0 and cantidad4 != 0:
                    result = (float(cantidad3*(df_market_calculadora2['close'].values[-1])))/(float(cantidad4*(df_market_calculadora3['close'].values[-1])))
            else:
                    result = 0

            st.write('RESULTADO: ',cantidad3,eleccion3,' es igual a', result, eleccion4)

def pageIV():
            st.title('TASA IMPLICITA DE FUTUROS')

            symbol_list_fut3=['BTC-1230', 'ETH-1230', 'USDT-1230', 'AXS-1230', 'BNB-1230', 'XRP-1230', 'LTC-1230', 'MATIC-1230', 'SOL-1230', 'DOGE-1230']
            symbol_list_fut6=['BTC-0331', 'ETH-0331']
            Futurestime=['3 Meses','6 Meses']
            
            vencimiento=st.selectbox(
                        "Vencimiento Futuros",
                        Futurestime)
            fecha_actual= datetime.now()
            vto_3m = datetime(2022,12,31)
            vto_6m = datetime(2023,3,31)

            if vencimiento == '3 Meses':
                listafut = symbol_list_fut3
                dias_vto=(vto_3m-fecha_actual).days

            else:
                listafut = symbol_list_fut6
                dias_vto=(vto_6m-fecha_actual).days

            eleccionfut = st.selectbox(
                    'Elegir Futuro de Crypto',
                    (listafut))

            if vencimiento == '3 Meses':
                eleccionspot=eleccionfut.replace('-1230','/USD')
            else:
                eleccionspot=eleccionfut.replace('-0331','/USD')
            
            ohlcv5 = exchange.fetch_ohlcv(symbol=eleccionfut, timeframe='1d', since=None, limit=86400)
            df_market_fut=pd.DataFrame(ohlcv5, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            
            ohlcv6 = exchange.fetch_ohlcv(symbol=eleccionspot, timeframe='1d', since=None, limit=86400)
            df_market_spot=pd.DataFrame(ohlcv6, columns=['timestamp','open', 'high', 'low', 'close','volume'])
            
            
            tasa_imp= round(((df_market_fut['close'].values[-1]/df_market_spot['close'].values[-1])-1),4)

            tna = round(((365/dias_vto)*tasa_imp),4)
            tea = round((((1+(tna/12))**12)-1),4)

            st.write('La tasa Implicita de Futuros de ',eleccionspot, ' a ',  vencimiento, ' es: ', (tasa_imp),'%', ' Nominal para ',dias_vto, ' Dias')
            st.write('La tasa Implicita de Futuros de ',eleccionspot, ' a ',  vencimiento, ' es: ', (tna),'%', ' TNA')
            st.write('La tasa Implicita de Futuros de ',eleccionspot, ' a ',  vencimiento, ' es: ', (tea),'%', ' TEA')
            

            

page_names_to_funcs = {
    'I. Resumen de Cotizaciones': main_page,
    'II. Análisis Gráfico': pageI,
    'III. Calculadora en USD': pageII,
    'IV. Calculadora en Cryptos': pageIII,
    'V. Tasa Implicita de Futuros': pageIV}

selected_page = st.sidebar.selectbox("Seleccione página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()