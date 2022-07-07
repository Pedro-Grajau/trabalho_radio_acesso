import numpy as np
import pandas as pd

def log10(num):
    return np.log10(num)

def calculate_path_loss(f, Hm, Hb, d, type):
    
    asm = (((1.1*log10(f))-0.7)*Hm)-((1.56*log10(f))-0.8)
    Lusm = 69.55 + (26.16*log10(f)) - (13.82*log10(Hb)) - asm + ((44.9 - (6.55*log10(Hb)))*log10(d))

    #Urban Area Loss large city (dB)
    if f <= 200:
        al = (8.29*(log10(1.54*Hm)**2))-1.1
        Lul = 69.55 + (26.16*log10(f)) - (13.82*log10(Hb)) - al + ((44.9 - (6.55*log10(Hb)))*log10(d))
    elif f >= 400:
        al = (3.2*(log10(11.75*Hm)**2))-4.97
        Lul = 69.55 + (26.16*log10(f)) - (13.82*log10(Hb)) - al + ((44.9 - (6.55*log10(Hb)))*log10(d))
    else:
        print('frequency range undefine')

    #Suburban Area large city (dB)
    Lsul = Lul - (2*(log10(f/28)**2))-5.4

    #Rural Area large city (Quasi-Open) (dB)
    Lrqol = Lul - (4.78*(log10(f)**2))+(18.33*log10(f))-35.94

    #Rural Area large city (Open Area) (dB)
    Lrol = Lul - (4.78*(log10(f)**2))+(18.33*log10(f))-40.94

    list_models = [Lul, Lsul, Lrqol, Lrol]
    return dict(enumerate(list_models)).get(type)

def create_line_plot(f, Hm, Hb, d):
    list_models = []
    for t in range(4):
        model = calculate_path_loss(f, Hm, Hb, range(1, d+1), t)
        list_models.append(model)
    
    list_models = [list(i) for i in zip(*list_models)]
    chart_data = pd.DataFrame(
        list_models,
        columns=['Lul', 'Lsul', 'Lrqol', 'Lrol'],
    )
    return chart_data