 def steel_ratio_check():


def rebar_suggestion():

    dbar_sizes = [20, 25, 28, 32]
    n_list =[]
    num_layer_list = []

    dbarprime_sizes = []
    nprime_list = []

    for dbar in dbar_sizes:
        import math
        Abar = (math.pi)* (dbar**2)/4

        rho_max = (3/7) * (0.85*fc*beta1)/fy
        deff_initial= h-cc-tie-dbar*0.5
        As_max = rho_max * b * deff_initial

        n = math.ceil(As_max/Abar)
        n_list.append(n)

        num_layer = next(layer for layer in range(1,6) if (b - 2*cc - 2*tie - (n/layer)*dbar) / ((n/layer)-1) > dbar)
        num_layer_list.append(num_layer)

        dbarprime = dbar
        dbar_sizes.append(dbarprime)

        if num_layer >1 and n/num_layer>2:
            nprime = 3
        else:
            nprime = 2
        nprime_list.append(nprime)
    
    dict = {'Bottom Bars': dbar_sizes, 'Qty(bottom)':n_list, 'Layer':num_layer_list, 'Top Bars': dbarprime_sizes, 'Qty(top)':nprime_list}
    import pandas as pd
    df = pd.DataFrame(dict)
    return df

print('')
print(rebar_suggestion())
print('')