V_Volts = 8
I_Amperes = 4


t_seconds = 1
#Energy_Storage = P_Power * t_seconds
#E_Joules = Energy_Storage


def available_power(V_Volts, I_Amperes):
    if V_Volts >  28:
        V_Volts = 28
    if I_Amperes >  10:
        I_Amperes = 10
    P_Power = V_Volts * I_Amperes
    return P_Power

print(f"The Systems Power is {available_power(V_Volts, I_Amperes)}W")

def energy_available(available_power, t_seconds):
    x = available_power * t_seconds
    return x


#print(energy_available(available_power, t_seconds))