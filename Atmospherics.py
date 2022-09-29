
"""This file holds the globaly needed values for computing attenuation.
The dictionary below 'lines' comes from 'Table 1' in the artical by Meeks and Lilley:
THE MICROWAVE SPECTRUM OF OXYGEN IN THE EARTH'S ATMOSPHERE"""

lines={ 1 : ( 56.2648, 118.7505 ) ,
		3 : ( 58.4466, 62.4863 ) ,
		5 : ( 59.5910, 60.3061 ) ,
		7 : ( 60.4348, 59.1642 ) ,
		9 : ( 61.1506, 58.3239 ) ,
		11 : ( 61.8002, 57.6125 ) ,
		13 : ( 62.4112, 56.9682 ) ,
		15 : ( 62.9980, 56.3634 ) ,
		17 : ( 63.5685, 55.7839 ) ,
		19 : ( 64.1272, 55.2214 ) ,
		21 : ( 64.6779, 54.6728 ) ,
		23 : ( 65.2240, 54.1294 ) ,
		25 : ( 65.7626, 53.5960 ) ,
		27 : ( 66.2978, 53.0695 ) ,
		29 : ( 66.8313, 52.5458 ) ,
		31 : ( 67.3627, 52.0259 ) ,
		33 : ( 67.8923, 51.5091 ) ,
		35 : ( 68.4205, 50.9949 ) ,
		37 : ( 68.9478, 50.4830 ) ,
		39 : ( 69.4741, 49.9730 ) ,
		41 : ( 70.0000, 49.4648 ) ,
		43 : ( 70.5249, 48.9582 ) , # This is the same as the meeks and lilley artical, however RADTRAN gives 70.5244, not 70.5249
		45 : ( 71.0497, 48.4530 ) }