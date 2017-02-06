import numpy as np
from scipy.integrate import odeint

# y= [a, adot]
def friedmannEqs(y, t, Omega_M0, Omega_DE0, Omega_rad0, w, H0):
    a, adot= y
    Omega_k0= 1.-Omega_M0-Omega_DE0-Omega_rad0
    dadt= H0*np.sqrt(Omega_M0*a**-1.+Omega_rad0*a**-2.+Omega_DE0*a**(-3.*w-1.)+Omega_k0)
    daSqdtSq= -(H0/2.)*adot*(Omega_M0*a**-3.+2.*Omega_rad0*a**(-4)+(1.+3.*w)*Omega_DE0*a**(-3.*(1.+w)))/(np.sqrt(Omega_M0*a**-3.+Omega_rad0*a**(-4)+Omega_DE0*a**(-3.*(1+w))+ Omega_k0*a**-2.))
    dydt= [dadt, daSqdtSq]
    return dydt


def specificUniverse(Omega_M0, Omega_rad0, Omega_DE0, w, H0, factor_sToGyr, a_0= 1.):
    # H0 in seconds
    t0= 1/H0  # s
    t0_Gyr= t0/factor_sToGyr  # Gyr
    
    Omega_k0= 1.-Omega_M0-Omega_DE0-Omega_rad0
    
    print 'Omega_k: %s'%(Omega_k0)
    
    #a_0= 1.
    dadt_0= H0*np.sqrt(Omega_M0*a_0**-1.+Omega_rad0*a_0**-2.+Omega_DE0*a_0**(-3.*w-1.)+Omega_k0)
    y0 = [a_0, dadt_0]

    # t>t0
    logt= np.arange(np.log10(t0_Gyr),6,.01)
    tpos= 10.**logt  # Gyr
    tpos= tpos*factor_sToGyr  # seconds
    sol = odeint(friedmannEqs, y0, tpos, args=(Omega_M0, Omega_DE0, Omega_rad0, w, H0))
    a_tpos= sol[:, 0]
    adot_tpos= sol[:, 1]
    
    # t<t0
    logt= np.arange(np.log10(t0_Gyr),0.,-.01)
    tneg= 10.**logt  # Gyr
    tneg= tneg*factor_sToGyr  # seconds
    sol = odeint(friedmannEqs, y0, tneg, args=(Omega_M0, Omega_DE0, Omega_rad0, w, H0))
    a_tneg= sol[:, 0]
    adot_tneg= sol[:, 1]
    
    # reverse and combine
    tneg= list(tneg)
    tneg.reverse()
    a_tneg= list(a_tneg)
    a_tneg.reverse()
    adot_tneg= list(adot_tneg)
    adot_tneg.reverse()
    
    t= np.array(tneg+list(tpos))
    a= np.array(a_tneg+list(a_tpos))
    adot= np.array(adot_tneg+list(adot_tpos))
    
    return [a, adot, t]


def totDensity(a, Omega_M0, Omega_rad0, Omega_DE0, w):
    # returns rho/rho_crit
    return Omega_M0*a**-3.+Omega_rad0*a**-4.+ Omega_DE0*a**(-3.*(1+w))

def universeAge(a, a0, H0, Omega_M0, Omega_rad0, Omega_DE0, w, factor_sToGyr):
    import scipy.integrate as sp
    
    def dt(a, key): 
        Omega_k0= 1.-Omega_M0[key]-Omega_DE0[key]-Omega_rad0[key]
        dadt= H0*np.sqrt(Omega_M0[key]*a**-1.+Omega_rad0[key]*a**-2.+Omega_DE0[key]*a**(-3.*w[key]-1.)+Omega_k0)
        return 1/dadt

    for key in a:
        print 't0 for %s:\n%f (Gyrs)\n'%(key, sp.quad(dt, 0., a0, args= (key,))[0]/factor_sToGyr)

    print 't0 using H0 given (Gyrs): %s' %(1./(H0*factor_sToGyr)) 
