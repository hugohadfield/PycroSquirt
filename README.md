# PycroSquirt 

A Python Microsquirt V3 library

Example usage:

<code>
"
from MicroSquirt import MicroSquirt
import time

ms = MicroSquirt('COM7')
for i in range(0,100):
	ms.get_data()
	time.sleep(0.5)
"
</code>


  <p align="left">&nbsp;</p>
  <h3 align="center">Real Time variables returned with "A" commands. 
  </h3>
    <p align="left">Some values are scaled for best use of memory as indicated 
      by 'scale and translate'.. The scaling and translation values are used as 
      follows:<br>
      &nbsp;&nbsp;&nbsp;msValue = userValue / scale - translate<br>
      &nbsp;&nbsp;&nbsp;userValue = (msValue + translate) * scale <br>
      Where msValue is the value stored in MS2/Extra, and userValue is the scaled 
      human readable form using the indicated 'Units' in the table.</p>
<p align="left"></p>
<p align="left"></p>
<table border="1" align="center">
  <tbody><tr> 
    <td width="106"> <div align="center"><strong>Variable Name</strong></div></td>
    <td width="57"> <div align="center"><strong>data type</strong></div></td>
    <td width="66"> <div align="center"><strong>location (index)</strong></div></td>
    <td width="105"> <div align="center"><strong>scale, translate</strong></div></td>
    <td width="59"> <div align="center"><strong>Units</strong></div></td>
    <td width="434"> <div align="center"><strong>Description</strong></div></td>
  </tr>
  <tr> 
    <td> <div align="center">seconds</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">0</div></td>
    <td width="105"> <div align="center">1/256, 0</div></td>
    <td><div align="center">sec</div></td>
    <td>counter that continuously counts from 0 to 65535</td>
  </tr>
  <tr> 
    <td><div align="center">pulseWidth1</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">2</div></td>
    <td width="105"> <div align="center">0.000666, 0.0</div></td>
    <td><div align="center">sec</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">pulseWidth2</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">4</div></td>
    <td width="105"> <div align="center">0.000666, 0.0</div></td>
    <td><div align="center">sec</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">rpm</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">6</div></td>
    <td width="105"> <div align="center">1,0</div></td>
    <td><div align="center">RPM</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">advance</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">8</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">deg</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td> <div align="center">squirt</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">10</div></td>
    <td width="105"> <div align="center"></div></td>
    <td><div align="center">bits</div></td>
    <td><strong>Bit&nbsp;&nbsp;Description&nbsp;when high</strong><br> &nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;inj1 
      squirt (firing1)<br> &nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;inj2 squirt (firing2)<br> 
      &nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;scheduled 1 to squirt (sched1)<br> &nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;injecting 
      1 (inj1)<br> &nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;scheduled 2 (sched2)<br> &nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;injecting 
      2 (inj2)<br> &nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;boost control Off (tentative)</td>
  </tr>
  <tr> 
    <td> <div align="center">engine</div></td>
    <td><div align="center">U8</div></td>
    <td><div align="center">11</div></td>
    <td width="105"> <div align="center"></div></td>
    <td> <div align="center">bits</div></td>
    <td><p>Engine current status<strong><br>
        Bit&nbsp;&nbsp;Description&nbsp;when high</strong><br>
        &nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; running (ready)<br>
        &nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cranking (crank)<br>
        &nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;after start enrichment (ASE) 
        (startw) <br>
        &nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in warmup (warmup)<br>
        &nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; acceleration mode (accaen)<br>
        &nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in deceleration mode (accden)<br>
        &nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
        &nbsp;7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle on (tentative)</p></td>
  </tr>
  <tr> 
    <td> <div align="center">afrtgt1</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">12</div></td>
    <td width="105"> <div align="center">10, 0</div></td>
    <td><div align="center">AFR</div></td>
    <td>Air Fuel Ratio target 1</td>
  </tr>
  <tr> 
    <td> <div align="center">afrtgt2</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">13</div></td>
    <td width="105"> <div align="center">10, 0</div></td>
    <td><div align="center">AFR</div></td>
    <td>Air Fuel Ratio target 2</td>
  </tr>
  <tr> 
    <td> <div align="center">wbo2_en1</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">14</div></td>
    <td width="105"> <div align="center">1, 0</div></td>
    <td><div align="center"></div></td>
    <td>indicates wether wide band AFR is valid</td>
  </tr>
  <tr> 
    <td> <div align="center">wbo2_en2</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">15</div></td>
    <td width="105"> <div align="center">1, 0</div></td>
    <td><div align="center"></div></td>
    <td>indicates wether wide band AFR is valid</td>
  </tr>
  <tr> 
    <td> <div align="center">barometer</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">16</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">kPa</div></td>
    <td>real time barometer for altitude correction</td>
  </tr>
  <tr> 
    <td> <div align="center">map</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">18</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">kPa</div></td>
    <td>&nbsp;MAP value used for fuel calculations</td>
  </tr>
  <tr> 
    <td> <div align="center">mat</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">20</div></td>
    <td width="105"> <p align="left">&nbsp;ºF - 0.1, 0<br>
        &nbsp;ºC - 0.05555, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-320</p></td>
    <td><div align="center">ºF<br>
        ºC<br>
        &nbsp; </div></td>
    <td>&nbsp;Manifold air temperature</td>
  </tr>
  <tr> 
    <td> <div align="center">coolant</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">22</div></td>
    <td width="105"> <p align="left">&nbsp;ºF - 0.1, 0<br>
        &nbsp;ºC - 0.05555, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-320</p></td>
    <td><div align="center">ºF<br>
        ºC<br>
        &nbsp; </div></td>
    <td>&nbsp;Coolant temperature</td>
  </tr>
  <tr> 
    <td> <div align="center">tps</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">24</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;Throttle position</td>
  </tr>
  <tr> 
    <td> <div align="center">batteryVoltage</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">26</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">V</div></td>
    <td>&nbsp;Battery voltage</td>
  </tr>
  <tr> 
    <td><div align="center">afr1</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">28</div></td>
    <td width="105"><div align="center">0.1, 0</div></td>
    <td><div align="center">AFR</div></td>
    <td>Real time Air Fuel Ratio for VE1</td>
  </tr>
  <tr> 
    <td><div align="center">afr2</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">30</div></td>
    <td width="105"><div align="center">0.1, 0</div></td>
    <td><div align="center">AFR</div></td>
    <td>Real time Air Fuel Ratio for VE2</td>
  </tr>
  <tr> 
    <td><div align="center">knock</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">32</div></td>
    <td width="105"><div align="center">0.1, 0</div></td>
    <td><div align="center">V</div></td>
    <td>knock value in volts</td>
  </tr>
  <tr> 
    <td><div align="center">egoCorrection1</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">34</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>Exhaust gas correction (1) amount in per cent</td>
  </tr>
  <tr> 
    <td><div align="center">egoCorrection2</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">36</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>Exhaust gas correction (2) amount in per cent</td>
  </tr>
  <tr> 
    <td> <div align="center">airCorrection</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">38</div></td>
    <td width="105"> <div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>Gair</td>
  </tr>
  <tr> 
    <td> <div align="center">warmupEnrich</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">40</div></td>
    <td width="105"> <div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>Warmup enrichment</td>
  </tr>
  <tr> 
    <td> <div align="center">accelEnrich</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">42</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">ms</div></td>
    <td>&nbsp;Acceleraton enrichment length in milliSeconds</td>
  </tr>
  <tr> 
    <td> <div align="center">tpsfuelcut</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">44</div></td>
    <td width="105"> <div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td> <div align="center">baroCorrection</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">46</div></td>
    <td width="105"> <div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;Barometer Correction (Gbaro)</td>
  </tr>
  <tr> 
    <td> <div align="center">gammaEnrich</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">48</div></td>
    <td width="105"> <div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;Total Gamma Enrichments</td>
  </tr>
  <tr> 
    <td> <div align="center">veCurr1</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">50</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;Real time VE value in use (table 1) </td>
  </tr>
  <tr> 
    <td> <div align="center">veCurr2 </div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">52</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">%</div></td>
    <td>Real time VE value in use (table 2) </td>
  </tr>
  <tr> 
    <td> <div align="center">iacstep</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">54</div></td>
    <td width="105"> <div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td> <div align="center">coldAdvDeg</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">56</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">s</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td> <div align="center">tpsDOT</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">58</div></td>
    <td width="105"> <div align="center">0.1, 0</div></td>
    <td><div align="center">%/sec</div></td>
    <td>rate of change of the throttle position</td>
  </tr>
  <tr> 
    <td><div align="center">mapDOT</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">60</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">kPa/sec</div></td>
    <td>rate of change of the manifold absolute pressure</td>
  </tr>
  <tr> 
    <td><div align="center">dwell</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">62</div></td>
    <td width="105"><div align="center">.0666, 0</div></td>
    <td><div align="center">ms</div></td>
    <td>The ignition coil dwell</td>
  </tr>
  <tr> 
    <td><div align="center">maf</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">64</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">?</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">fuelload</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">66</div></td>
    <td width="105"><div align="center">0.1, 0</div></td>
    <td><div align="center">%</div></td>
    <td>Blend of MAP and TPS</td>
  </tr>
  <tr> 
    <td><div align="center">fuelCorrection</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">68</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>Per cent alcohol in the fuel</td>
  </tr>
  <tr> 
    <td><div align="center">portStatus</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">70</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td><p>spare port status bit<br>
        <strong>Bit&nbsp;&nbsp;Description&nbsp;when high</strong><br>
        &nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;<br>
        &nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;<br>
        &nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;<br>
        &nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;<br>
        &nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;<br>
        &nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;<br>
        &nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;</p></td>
  </tr>
  <tr> 
    <td><div align="center">knockRetard</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">71</div></td>
    <td width="105"><div align="center">0.1, 0</div></td>
    <td><div align="center">deg</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">EAEFuleCorr</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">72</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">egoV</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">74</div></td>
    <td width="105"><div align="center">0.01, 0</div></td>
    <td><div align="center">V</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">egoV2</div></td>
    <td><div align="center">S16</div></td>
    <td><div align="center">76</div></td>
    <td width="105"><div align="center">0.01, 0</div></td>
    <td><div align="center">V</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">status1</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">78</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">status2</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">79</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">status3</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">80</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">status4</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">81</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">looptime</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">82</div></td>
    <td width="105"><div align="center">0.6667, 0</div></td>
    <td><div align="center">us</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">status5</div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">84</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">us</div></td>
    <td>same as istatus5</td>
  </tr>
  <tr> 
    <td><div align="center">tpsADC</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">86</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">ADC</div></td>
    <td>REAL for calibrator and file indexing</td>
  </tr>
  <tr> 
    <td><div align="center">fuelload2</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">88</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">ignload</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">90</div></td>
    <td width="105"><div align="center">0.01, 0</div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">ignload2</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">92</div></td>
    <td width="105"><div align="center">0.01, 0</div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center"></div></td>
    <td><div align="center">U08</div></td>
    <td><div align="center">104</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td><p><strong>Bit&nbsp;&nbsp;Description&nbsp;when high</strong><br>
        &nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;sync_error<br>
        &nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;sync_status <br>
      </p></td>
  </tr>
  <tr> 
    <td><div align="center">deltaT</div></td>
    <td><div align="center">S32</div></td>
    <td><div align="center">106</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">us</div></td>
    <td>Normalized time between trigger pulses, "fills in" missing teeth</td>
  </tr>
  <tr> 
    <td><div align="center">wallfuel</div></td>
    <td><div align="center">U32</div></td>
    <td><div align="center">110</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center">us</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioadc0</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">114</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioadc1</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">116</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioadc2</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">118</div></td>
    <td width="105"><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioadc3</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">120</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioadc4</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">122</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioadc5</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">124</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioadc6</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">126</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioadc7</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">128</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpiopwmin0</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">130</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpiopwmin1</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">132</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpiopwmin2</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">134</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td height="28"><div align="center">gpiopwmin3</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">136</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioport0</div></td>
    <td><div align="center">U8</div></td>
    <td><div align="center">138</div></td>
    <td><div align="center">1.0, 0.0</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioport1</div></td>
    <td><div align="center">U8</div></td>
    <td><div align="center">139</div></td>
    <td><div align="center">1.0, 0.0</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td><div align="center">gpioport2</div></td>
    <td><div align="center">U8</div></td>
    <td><div align="center">140</div></td>
    <td><div align="center">1.0, 0.0</div></td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td height="24"><div align="center">adc6</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">141</div></td>
    <td><div align="center">1.0, 0.0</div></td>
    <td><div align="center">ADC</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td height="24"><div align="center">adc7</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">143</div></td>
    <td><div align="center">1.0, 0.0</div></td>
    <td><div align="center">ADC</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td height="24"><div align="center">wallfuel2</div></td>
    <td><div align="center">U32</div></td>
    <td><div align="center">145</div></td>
    <td><div align="center">1.000,0.0</div></td>
    <td><div align="center">us</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td height="24"><div align="center">EAEFuelCorr2</div></td>
    <td><div align="center">U16</div></td>
    <td><div align="center">149</div></td>
    <td><div align="center">1.0, 0.0</div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td height="24"><div align="center">boostduty</div></td>
    <td><div align="center">U8</div></td>
    <td><div align="center">151</div></td>
    <td><div align="center">1.0, 0.0</div></td>
    <td><div align="center">%</div></td>
    <td>&nbsp;</td>
  </tr>
  <tr> 
    <td height="24"><div align="center">checksum</div></td>
    <td><div align="center">U8</div></td>
    <td><div align="center">152</div></td>
    <td><div align="center">1,0</div></td>
    <td><div align="center"></div></td>
    <td> XOR checksum for tuning software to validate data. Not presently used 
      by existing tuning s/w</td>
  </tr>
  <tr> 
    <td height="24"><div align="center">ochBlockSize</div></td>
    <td><div align="center">U8</div></td>
    <td><div align="center">153</div></td>
    <td><div align="center"></div></td>
    <td><div align="center"></div></td>
    <td>extra checksum byte</td>
  </tr>
</tbody></table>
<div align="center"></div>
