
def biggest( self ):
	pass
def middle( self ):
	pass
def smallest( self ):
	pass


class Ray:
	
	def __init__( self, frequency ):
		import Atmospherics
		self.frequency = frequency	
		self.lines = Atmospherics.lines
		import math
		self.math = math
		"""I import math and assign it to an attribute of Ray so that I can use it's
		methods anywhere"""
		
		if frequency > 300.0:
			self.computeWaterAttenuation = biggest
		elif frequency > 60.0:
			self.computeWaterAttenuation = middle
		else:
			self.computeWaterAttenuation = smallest
		
		
	def computeCoefficients( self, inputValueTuple ):
		"""This is the over-arching funtion call to compute attenuation coefficients;
		all the funtions then are modular and can be swapped out without affecting the 
		functionality of the Ray class"""
		
		self.pressure = inputValueTuple[0]
		self.humidity = inputValueTuple[1]
		self.temperature = inputValueTuple[2]
		
		oxygenAttenuation = self.computeOxygenAttenuation()
		waterAttenuation = self.computeWaterAttenuation( self )
		
		return (oxygenAttenuation, waterAttenuation)
		
	def computeOxygenAttenuation( self, c1 = 2.6742 ):	
		"""Function for computing the attenuation coefficient due to oxygen
		written according to the paper by Meeks and Lilley:
		THE MICROWAVE SPECTRUM OF OXYGEN IN THE EARTH'S ATMOSPHERE"""
		
		def deltaNu( Pressure, Temperature ):
			a = 1.95 * self.math.pow(10,6)
			b = .25
			if Pressure < 267:
				b = .75
			if Pressure > 19:
				b = 0.25*(1.0+(self.math.log(267.41/Pressure))/1.323)
			return( a * Pressure * ( 0.21 + 0.78 * b  ) * ( 300 / Temperature ) ** 0.85 )
	
	
		P = self.pressure
		T = self.temperature
		mega = self.math.pow( 10, 6 )
		giga = self.math.pow( 10, 9 )
		c1 = c1 / giga 	#you will notice that c1 has a default value in the method signature of
						#computeOxygenAttenuation( self, c1 = 2.6742 ); this is a constant for sake of units.
						# I was getting 9 orders of magnitude too large before I divided by 10^9
		nu = self.frequency * giga
		deltaNuSquared = deltaNu( P, T )**2
		
		gammaConstants = ( c1 * P * nu * nu / ( T * T * T ) ) * deltaNu( P, T )
		sumForGamma = 0
		
		for n in range(1,45,2):
		
			#this is the origional Fortran code for the summation, it was in a similar 'for' loop
			"""
            SUM=SUM+((1.0/((NUPL(N)-NU)**2+DNU12)+ &
            1.0/((NUPL(N)+NU)**2+DNU12))* &
            (FN*(2.0*FN+3.0)/(FN+1.0))+ &
            (1.0/((NUMI(N)-NU)**2+DNU12)+ & 
            1.0/((NUMI(N)+NU)**2+DNU12))* &
            (FN+1.0)*(2.0*FN-1.0)/FN+ &
            1.0/(NU**2+DNU12)* &
            2.0*(FN**2+FN+1.0)*(2.0*FN+1.0)/(FN**2+FN))* &
            EXP(-2.0684*FN*(FN+1.0)/T) 
            """
            
            #this is the Python equivlent. I have inserted white space to make it easier to read (maybe).
            #self.lines is referencing a dictionary in the file 'Atmospherics.py' such that 
            # self.lines[ n ][0] accesses the record (a tuple) coresponding to the key 'n' and then
            # accesses the record at index '0'
			sumForGamma += ( ( 1.0 / ( ( self.lines[ n ][0] * giga - nu )**2 + deltaNuSquared ) + 1.0 / ( ( self.lines[ n ][0] * giga + nu )**2 + deltaNuSquared ) ) * ( n * ( 2.0 * n + 3.0 ) / ( n + 1.0 ) ) + ( 1.0 / ( ( self.lines[ n ][1] * giga - nu )**2 + deltaNuSquared )  +  1 / ( ( self.lines[ n ][1] * giga + nu )**2 + deltaNuSquared ) ) * ( (n+1)*(2*n-1)/n ) + ( 1.0 / ( nu**2 + deltaNuSquared ) ) * ( 2 * ( n**2 + n + 1 ) * ( 2 * n + 1 ) / ( n * ( n + 1 ) ) ) ) * self.math.exp( -2.06844 * n * ( n + 1 ) / T )
	
		return( gammaConstants * sumForGamma )
	
	
	
	def computeWaterAttenuation( self ):
		"""Function to compute the attenuation coefficient due to oxygen by three different techniques
		dependant upon the frequency; above 300 GHz according to the Thesis by Norman E Gaut:
		STUDIES OF ATMOSPHERIC WATER VAPOR BY MEANS OF PASSIVE MICROWAVE TECHNIQUES"""
	
		"""This function is dynamicaly assigned by the constructor dependant upon the frequency,
		this is done to avoid evaluating an 'if' statement on every call to this function"""
		pass