class ovp:

    def __init__(COMMON, cm0,cm1,cm2,cm3,cm4,cm5,cm6,cm7,cm8,cm9,cm10, 
                 cm11,cm12,cm13,cm14,cm15,cm16,cm17,cm18,cm19,cm20,
		 cm21,cm22,cm23,cm24,cm25,cm26,cm27,cm28,cm29,cm30,
		 cm31,cm32,cm33,cm34,cm35,cm36,cm37,cm38,cm39):


	COMMON.TIME = cm0
	COMMON.STEP = cm1
	COMMON.STEP01 = cm2
	COMMON.STEP02 = cm3
	COMMON.SMIN = cm4
	COMMON.DABSI = cm5
	COMMON.DRLTI = cm6
	COMMON.STEPMD = cm7
	COMMON.TIMEND = cm8
	COMMON.NAME = cm9
	COMMON.nLength = cm10
	COMMON.NSTEP = cm11
	COMMON.SYSPRN = cm12
	COMMON.NITER = cm13
	COMMON.ITR = cm14
	COMMON.CODE = cm15
	COMMON.NUMINT = cm16
	COMMON.NUMPP = cm17
	COMMON.CODSTP = cm18
	COMMON.CODGRF = cm19
	COMMON.NEWINT = cm20
	COMMON.MINSTP = cm21
	COMMON.RLMAX = cm22
	COMMON.RLMIN = cm23
	COMMON.MSHEPS = cm24
	COMMON.INTMAX = cm25
	COMMON.PI = cm26
	COMMON.REZB = cm27
	COMMON.REZC = cm28
	COMMON.REZD = cm29		
	COMMON.RELYX = cm30
	COMMON.XNMPXL = cm31
	COMMON.YNMPXL = cm32
	COMMON.XNMSMB = cm33
	COMMON.YNMSMB = cm34
	COMMON.NCOLOR = cm35
	COMMON.NMVPAG = cm36
	COMMON.MODES = cm37
	COMMON.IK4 = cm38
	COMMON.IS4 = cm39
	

    def Execute(COMMON, XOUT, PAR, WRK, DOF):
	res = return_result(COMMON, XOUT, WRK)
	return res



def return_result(COMMON, XOUT, WRK):
	comm = [COMMON.TIME, 
		COMMON.STEP,
		COMMON.STEP01,
		COMMON.STEP02,
		COMMON.SMIN,
		COMMON.DABSI,
		COMMON.DRLTI,
		COMMON.STEPMD,
		COMMON.TIMEND,
		COMMON.NAME,
		COMMON.nLength,
		COMMON.NSTEP,
		COMMON.SYSPRN,
		COMMON.NITER,
		COMMON.ITR,
		COMMON.CODE,
		COMMON.NUMINT,
		COMMON.NUMPP,
		COMMON.CODSTP,
		COMMON.CODGRF,
		COMMON.NEWINT,
		COMMON.MINSTP,
		COMMON.RLMAX,
		COMMON.RLMIN,
		COMMON.MSHEPS,
		COMMON.INTMAX,
		COMMON.PI,
		COMMON.REZB,
		COMMON.REZC,
		COMMON.REZD,		
		COMMON.RELYX,
		COMMON.XNMPXL,
		COMMON.YNMPXL,
		COMMON.XNMSMB,
		COMMON.YNMSMB,
		COMMON.NCOLOR,
		COMMON.NMVPAG,
		COMMON.MODES,
		COMMON.IK4,
		COMMON.IS4]

	return [comm, XOUT, WRK]