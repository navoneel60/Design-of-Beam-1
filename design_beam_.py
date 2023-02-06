from bdb import effective
from tkinter import FLAT


print('\n-------------------------------------------')
print("BEAM DESIGN CHECK - Rectangular Beam")
print('--------------------------------------------')

while True:
    try:
        print("Please enter material and section properties:")
        fc = float(input("Concrete strength, f'c(MPa) = "))
        fy = float(input("Steel strength, fy (MPa) = "))
        b = float(input("Beam width, b (mm) = "))
        h = float(input("Beam total depth, h (mm) = "))
        print("\nThis program assumes: Concrete cover = 40mm, Stirrups/Links Diameter = 10mm")
    except ValueError:
        print("DATA INPUT ERROR! Try again ")
    else:
        Es = 200000
        ec = 0.003
        ey = fy/Es
        cc = 40
        tie = 10

        beta1 = beta1_value()
        df = rebar_suggestion()

        capacity = []
        classify_member = []
        steel_ratio = []

        for i in range(0, len(df.index)):
            dbar, n, num_layer, dbarprime, nprime = df.iloc[i,:]

            As, Asprime = steel_areas()
            deff, num_layer = effective_depth()
            dprime = topbar_depth()
            fs, fsprime, es, a, c = stress_strain()
            phi, classify = strength_factor_classification()
            Mu, T, C, Cprime = forces_capacity()

            capacity.append(round(Mu))
            classify_member.append(classify)
            steel_ratio.append(steel_ratio_check())

        df['Capacity, Mu(kN-m)'] = capacity
        df['Classification'] = classify_member
        df['Steel Ratio'] = steel_ratio


        print('\n-----------------------------------')
        print('Suggested Reinforcements: ')
        print('----------------------------------')
        import time
        time.steep(1)
        print(df)


        answer = input("\nWould you like to provide reinforcements to check? (y/n) ")
        while answer.lower().startswith("y"):
            try:
                dbar = int(input("Bottom Rebar dia(mm) = "))
                n = int(input("Bottom Rebar Total qty (no.) = "))
                dbarprime = int(input("Top Rebar dia(mm) = "))
                nprime = int(input("Top Rebar Total qty (no.) = "))
            except ValueError:
                print("DATA INPUT ERROR! Try again ")
            if dbar<10 or n<2 or dbarprime<10 or nprime<2:
                print("DATA INPUT ERROR! Minimum 2nos and Minimum 10mm dia")
            else:
                As, Asprime = steel_areas()
                deff, num_layer = effective_depth()
                dprime = topbar_depth()
                fs, fsprime, es, a, c = stress_strain()
                phi, classify = strength_factor_classification()
                Mu, T, C, Cprime = forces_capacity()

                print(f'\nBeam Capacity: Mu = {round(My)} kN-m, \nBeam is under {classify}, \n{steel_ratio_check()}')
                print("\nHave a good day!\n")
                exit()
        else:
            print("\nHave a good day!\n")
            exit()