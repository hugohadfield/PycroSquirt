# PycroSquirt 

A Python Microsquirt V3 library

Real Time variables returned with "A" commands.

Some values are scaled for best use of memory as indicated by 'scale and translate'.. The scaling and translation values are used as follows:
   msValue = userValue / scale - translate
   userValue = (msValue + translate) * scale 
Where msValue is the value stored in MS2/Extra, and userValue is the scaled human readable form using the indicated 'Units' in the table.

Variable Name
data type
location (index)
scale, translate
Units
Description
seconds
U16
0
1/256, 0
sec
counter that continuously counts from 0 to 65535
pulseWidth1
U16
2
0.000666, 0.0
sec
 
pulseWidth2
U16
4
0.000666, 0.0
sec
 
rpm
U16
6
1,0
RPM
 
advance
S16
8
0.1, 0
deg
 
squirt
U08
10
bits
Bit  Description when high
 0    inj1 squirt (firing1)
 1    inj2 squirt (firing2)
 2    scheduled 1 to squirt (sched1)
 3    injecting 1 (inj1)
 4    scheduled 2 (sched2)
 5    injecting 2 (inj2)
 6    boost control Off (tentative)
engine
U8
11
bits
Engine current status
Bit  Description when high
 0      running (ready)
 1      cranking (crank)
 2      after start enrichment (ASE) (startw) 
 3      in warmup (warmup)
 4      acceleration mode (accaen)
 5      in deceleration mode (accden)
 6      
 7      idle on (tentative)

afrtgt1
U08
12
10, 0
AFR
Air Fuel Ratio target 1
afrtgt2
U08
13
10, 0
AFR
Air Fuel Ratio target 2
wbo2_en1
U08
14
1, 0
indicates wether wide band AFR is valid
wbo2_en2
U08
15
1, 0
indicates wether wide band AFR is valid
barometer
S16
16
0.1, 0
kPa
real time barometer for altitude correction
map
S16
18
0.1, 0
kPa
 MAP value used for fuel calculations
mat
S16
20
 ºF - 0.1, 0
 ºC - 0.05555,             -320

ºF
ºC
 
 Manifold air temperature
coolant
S16
22
 ºF - 0.1, 0
 ºC - 0.05555,             -320

ºF
ºC
 
 Coolant temperature
tps
S16
24
0.1, 0
%
 Throttle position
batteryVoltage
S16
26
0.1, 0
V
 Battery voltage
afr1
S16
28
0.1, 0
AFR
Real time Air Fuel Ratio for VE1
afr2
S16
30
0.1, 0
AFR
Real time Air Fuel Ratio for VE2
knock
S16
32
0.1, 0
V
knock value in volts
egoCorrection1
S16
34
%
Exhaust gas correction (1) amount in per cent
egoCorrection2
S16
36
%
Exhaust gas correction (2) amount in per cent
airCorrection
S16
38
%
Gair
warmupEnrich
S16
40
%
Warmup enrichment
accelEnrich
S16
42
0.1, 0
ms
 Acceleraton enrichment length in milliSeconds
tpsfuelcut
S16
44
%
 
baroCorrection
S16
46
%
 Barometer Correction (Gbaro)
gammaEnrich
S16
48
%
 Total Gamma Enrichments
veCurr1
S16
50
0.1, 0
%
 Real time VE value in use (table 1)
veCurr2
S16
52
0.1, 0
%
Real time VE value in use (table 2)
iacstep
S16
54
%
 
coldAdvDeg
S16
56
0.1, 0
s
 
tpsDOT
S16
58
0.1, 0
%/sec
rate of change of the throttle position
mapDOT
S16
60
kPa/sec
rate of change of the manifold absolute pressure
dwell
U16
62
.0666, 0
ms
The ignition coil dwell
maf
S16
64
?
 
fuelload
S16
66
0.1, 0
%
Blend of MAP and TPS
fuelCorrection
S16
68
%
Per cent alcohol in the fuel
portStatus
U08
70
%
spare port status bit
Bit  Description when high
 0    
 1    
 2    
 3    
 4    
 5    
 6    

knockRetard
U08
71
0.1, 0
deg
 
EAEFuleCorr
U16
72
%
 
egoV
S16
74
0.01, 0
V
 
egoV2
S16
76
0.01, 0
V
 
status1
U08
78
 
status2
U08
79
 
status3
U08
80
 
status4
U08
81
 
looptime
U16
82
0.6667, 0
us
 
status5
U08
84
us
same as istatus5
tpsADC
U16
86
ADC
REAL for calibrator and file indexing
fuelload2
U16
88
%
 
ignload
U16
90
0.01, 0
%
 
ignload2
U16
92
0.01, 0
%
 
U08
104
Bit  Description when high
 0    sync_error
 1    sync_status 
deltaT
S32
106
us
Normalized time between trigger pulses, "fills in" missing teeth
wallfuel
U32
110
us
 
gpioadc0
U16
114
 
gpioadc1
U16
116
 
gpioadc2
U16
118
 
gpioadc3
U16
120
 	 	 
gpioadc4
U16
122
 	 	 
gpioadc5
U16
124
 	 	 
gpioadc6
U16
126
 	 	 
gpioadc7
U16
128
 	 	 
gpiopwmin0
U16
130
 	 	 
gpiopwmin1
U16
132
 	 	 
gpiopwmin2
U16
134
 	 	 
gpiopwmin3
U16
136
 	 	 
gpioport0
U8
138
1.0, 0.0
 	 
gpioport1
U8
139
1.0, 0.0
 	 
gpioport2
U8
140
1.0, 0.0
 	 
adc6
U16
141
1.0, 0.0
ADC
 
adc7
U16
143
1.0, 0.0
ADC
 
wallfuel2
U32
145
1.000,0.0
us
 
EAEFuelCorr2
U16
149
1.0, 0.0
%
 
boostduty
U8
151
1.0, 0.0
%
 
checksum
U8
152
1,0
XOR checksum for tuning software to validate data. Not presently used by existing tuning s/w
ochBlockSize
U8
153
extra checksum byte
