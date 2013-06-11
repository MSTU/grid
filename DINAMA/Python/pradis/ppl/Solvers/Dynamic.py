from Solver import *

class Dynamic (Solver):
	def __init__ (self, rnglist, 
			save 	= default,   
			end 	= default,    
			out 	= default,    
			smax 	= default,   
			smin 	= default,
			drlti 	= default,  
			dabsi 	= default,  
			drltu 	= default,  
			dabsu 	= default,  
			drltx 	= default,
			dabsx 	= default,  
			flag 	= default,   
			itr 	= default,    
			debug 	= default,  
			optim 	= default,
			control 	= default, 
			mode 	= default,   
			change 	= default,
			outs 	= default,   
			predict 	= default, 
			method 	= default, 
			weight 	= default, 
			second 	= default,
			ignore 	= default,
			atm 	= default,
			scale 	= default,  
			checkm 	= default, 
			outper 	= default, 
			outvar 	= default,	
			prttime = default,
			rlmin 	= default,  
			msheps 	= default, 
			parerr 	= default, 
			pspprt 	= default, 
			err 	= default, 
			desc=default):
		if (method == default):
			scheme = 0
		if (method == "Stoermer"):
			scheme = 0
		if (method == "Newmark"):
			scheme = 1
		if (method == "Explicit_Euler"):
			scheme = 2
		if (method == "Implicit_Euler"):
			scheme = 3
		if (method == "Trapecia"):
			scheme = 4
				
		self.this = Solver ("SHTERM", rnglist,
			save,   
			end,    
			out,
			smax,
			smin,
			drlti,  
			dabsi,  
			drltu,  
			dabsu,
			drltx,
			dabsx,  
			flag,   
			itr,    
			debug,  
			optim,
			control, 
			mode,   
			change,
			outs,   
			predict, 
			scheme, 
			weight, 
			second,
			ignore,
			atm,
			scale,  
			checkm, 
			outper, 
			outvar,	
			prttime,
			rlmin,  
			msheps, 
			parerr, 
			pspprt, 
			err,desc)
