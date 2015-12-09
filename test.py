#!/usr/bin/python 
#!/usr/bin/env python 
# 
#	_________ 
# U 
# ch0	Vdd	->	5V 
# ch1	Vref	->	5V 
# ch2	Agnd	->	GND 
# ch3	clk	->	GPIO11 
# ch4	Dout	->	GPIO9 
# ch5	Din	->	GPIO10 
# ch6	shdn/cs ->	GPIO8 
# ch7	Dgnd	->	GND 
#	________ 
# 
#ch0->luce 
#ch1->temperatura 
#ch2->corrente1 
#ch3->corrente2 
#ch4->corrente3 
#ch5->corrente4 

import spidev 
import time 
import os 
import math 
import sys 

# Open SPI bus 
spi = spidev.SpiDev() 
spi.open(0,0) 

# Function to read SPI data from MCP3008 chip 
# Channel must be an integer 0-7 
def ReadChannel(channel): 
adc = spi.xfer2([1,(8+channel)<<4,0]) 
data = ((adc[1]&3) << 8) + adc[2] 
return data 

# calcolo voltaggio 
def ConvertVolts(data,places): 
volts = (data * 4.89) / float(1023) 
volts = round(volts,places) 
return volts 

# calcolo temperatura 
def ConvertTemp(data,places): 
temp = 0 
temp = (((data * 48.87)/float(1023))-float(3)) 
temp = round(temp,places) 
return temp 

# calcolo corrente 1 (V0=1,88V) 
def ConvertCorr1(data,places): 
corr1 = (((data*float(0.004887))-float(1.88))*10) 
corr1 = round(corr1,places) 
return corr1 

# calcolo corrente 2 (V0=2,41V) 
def ConvertCorr2(data,places): 
corr2 = 0 
maxVal2 = 0 
corr2 = (((data*float(0.004887))-float(2.418))*10) 
corr2 = round(corr2,places) 
# for _ in range(100): 
# maxVal2 = max(maxVal2, corr2) 
# if maxVal2 > corr2: 
# corr2 = maxVal2 
return corr2 

# calcolo corrente 3 (V0=2,41V) 
def ConvertCorr3(data,places): 
corr3 = 0 
maxVal3 = 0 
corr3 = (((data*float(0.004887))-float(2.41))*10) 
corr3 = round(corr3,places) 
# for _ in range(100): 
# maxVal3 = max(maxVal3, corr3) 
# if maxVal3 > corr3: 
# corr3 = maxVal3 
return corr3 

# calcolo corrente 4 (V0=2,42V) 
def ConvertCorr4(data,places): 
corr4 = 0 
maxVal4 = corr4 
corr4 = (((data*float(0.004887))-float(2.42))*10) 
corr4 = round(corr4,places) 
for _ in range(100): 
maxVal4 = max(maxVal4, corr4) 
if maxVal4 > corr4: 
corr4 = maxVal4 
return corr4 

# canali sensore 
luce_channel = 0 
temp_channel = 1 
corr1_channel = 2 
corr2_channel = 3 
corr3_channel = 4 
corr4_channel = 5 


while True: 

# lettura luce raw 
luce_level = ReadChannel(luce_channel) 
luce_volts = ConvertVolts(luce_level,2) 

# lettura temperatura raw 
temp_level = ReadChannel(temp_channel) 
temp_volts = ConvertVolts(temp_level,2) 
temp = ConvertTemp(temp_level,2) 

#lettura sensore corrente1 raw 
corr1_level = ReadChannel(corr1_channel) 
corr1_volts = ConvertVolts(corr1_level,2) 
corr1 = ConvertCorr1(corr1_level,2) 

#lettura sensore corrente2 raw 
corr2_level = ReadChannel(corr2_channel) 
corr2_volts = ConvertVolts(corr2_level,2) 
corr2 = ConvertCorr2(corr2_level,2) 

#lettura sensore corrente3 raw 
corr3_level = ReadChannel(corr3_channel) 
corr3_volts = ConvertVolts(corr3_level,2) 
corr3 = ConvertCorr3(corr3_level,2) 

#lettura sensore corrente4 raw 
corr4_level = ReadChannel(corr4_channel) 
corr4_volts = ConvertVolts(corr4_level,2) 
corr4 = ConvertCorr4(corr4_level,2) 

#calcolo potenza totale assorbita 
potenza = (228 * (corr1+corr2+corr3+corr4)) 
potenza = max(round(potenza,2),float(0.00)) 

# stampa i risultati 
print("--------------------------------------------") 
print("Luce: {} ({}V)".format(luce_level,luce_volts)) 
print("Temperatura: {} ({}V) {} gradi".format(temp_level,temp_volts,temp)) 
print("Sensore 1: {} ({}V) {} Ampere".format(corr1_level,corr1_volts,corr1)) 
print("Sensore 2: {} ({}V) {} Ampere".format(corr2_level,corr2_volts,corr2)) 
print("Sensore 3: {} ({}V) {} Ampere".format(corr3_level,corr3_volts,corr3)) 
print("Sensore 4: {} ({}V) {} Ampere".format(corr4_level,corr4_volts,corr4)) 
print("Potenza totale: {} Watt".format(potenza)) 

# tempo tra una lettura e l'altra 
time.sleep(1)
