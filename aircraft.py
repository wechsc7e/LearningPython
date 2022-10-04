#!/usr/bin/env python3
#Aircraft Weight and Balance Script

aircraft=input("Which Aircraft Are You Flying Today? (Piper/Cessena) ")
weight_passengers=int(input("What Is The Weight of The Passengers? "))
weight_baggage=int(input("What Is The Weight of The Baggage? "))
quant_fuel=int(input("How Many Gallons of Fuel? "))
weight_fuel=quant_fuel*6.02

if aircraft=="Piper":
    if weight_passengers+weight_baggage+weight_fuel>895:
        print("Aircraft is Overweight")
    else:
        print("Aircraft Is Within Weight Limits")
if aircraft=="Cessena":
    if weight_passengers+weight_baggage+weight_fuel>759:
        print("Aircraft is Overweight")
    else:
        print("Aircraft Is Within Weight Limits")
