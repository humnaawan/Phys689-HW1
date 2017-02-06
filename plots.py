import numpy as np
import matplotlib.pyplot as plt
import os

legendFontSize= 14
axisLabelFontSize= 18
tickLabelFontSize= 16

def scaleFactorPlot(a, t, H0, factor_sToGyr, xMax= 100, yMax= 5,
                    savePlots= False, outDir= None, filenameTag= ''):
    # t, H0 in seconds
    # a, t are dictionaries
    plt.clf()
    for key in a:
        tscaled= t[key]/factor_sToGyr   # now in Gyr
        plt.plot(tscaled, a[key], label= key,)

    plt.xlim(0, xMax)   
    plt.ylim(0, yMax) 
    t0= 1/H0  # s
    t0= t0/factor_sToGyr # Gyr
    
    plt.plot([t0, t0], [0.,yMax], label= '$Today$')    
    plt.xlabel(r'$t \ (Gyr)$', fontsize= axisLabelFontSize)
    plt.ylabel('$a$', fontsize= axisLabelFontSize)
    plt.tick_params(axis='x', labelsize=tickLabelFontSize)
    plt.tick_params(axis='y', labelsize=tickLabelFontSize)
    plt.legend(fontsize= legendFontSize, loc= 4)#bbox_to_anchor= (0.7, 1.7))
    
    fig= plt.gcf()
    fig.set_size_inches(12,6)
    if savePlots:
        workDir= os.getcwd()
        os.chdir(outDir)
        plt.savefig('%sscaleFactorPlot.pdf'%(filenameTag),bbox_inches='tight', format= 'pdf')
        os.chdir(workDir)
    plt.show()


def densityPlot(rhoTotal, t, H0, factor_sToGyr, xMax= 40, yMax= 30,
                savePlots= False, outDir= None, filenameTag= ''):
    plt.clf()
    for key in rhoTotal:
        tscaled= t[key]/factor_sToGyr   # now in Gyr
        plt.plot(tscaled, rhoTotal[key], label= key)

    plt.xlim(0, xMax)   
    plt.ylim(0, yMax)
    t0= 1/H0  # s
    t0= t0/factor_sToGyr # Gyr
    plt.plot([t0, t0], [0.,yMax], label= '$Today$')
    plt.xlabel(r'$t \ (Gyr)$', fontsize= axisLabelFontSize)
    plt.ylabel(r'$\rho_{tot}/\rho_{crit, 0}$', fontsize= axisLabelFontSize)
    plt.tick_params(axis='x', labelsize=tickLabelFontSize)
    plt.tick_params(axis='y', labelsize=tickLabelFontSize)
    plt.legend(loc=0, fontsize= legendFontSize)
    
    fig= plt.gcf()
    fig.set_size_inches(12,6)
    if savePlots:
        workDir= os.getcwd()
        os.chdir(outDir)
        plt.savefig('%sdensityPlot.pdf'%(filenameTag),bbox_inches='tight', format= 'pdf')
        os.chdir(workDir)
    plt.show()


def HubbleConstantPlot(a, adot, t, H0, factor_sToGyr, xMax= 40, yMax= 300,
                       savePlots= False, outDir= None, filenameTag= ''):
    H= {}   # 1/s
    plt.clf()
    for key in a:
        H[key]= adot[key]/a[key]  # 1/s
        H[key]= H[key]*3.086*10**19
        tscaled= t[key]/factor_sToGyr   # now in Gyr
        plt.plot(tscaled, H[key], label= key)
    plt.xlim(0, xMax)   
    plt.ylim(0, yMax)
    t0= 1/H0  # s
    t0= t0/factor_sToGyr # Gyr
    plt.plot([t0, t0], [0.,yMax], label= '$Today$')
    plt.plot([0, xMax], [H0*3.086*10**19, H0*3.086*10**19], 'k', label= '$Input \ H_0: %s \ (km/s/Mpc)$'%(H0*3.086*10**19))
    
    plt.xlabel(r'$t \ (Gyr)$', fontsize= axisLabelFontSize)
    plt.ylabel(r'$H(t) (km/s/Mpc)$', fontsize= axisLabelFontSize)
    plt.tick_params(axis='x', labelsize=tickLabelFontSize)
    plt.tick_params(axis='y', labelsize=tickLabelFontSize)
    plt.legend(fontsize= legendFontSize, loc=1) #bbox_to_anchor= (1.3,0.7))
    
    fig= plt.gcf()
    fig.set_size_inches(12,6)
    if savePlots:
        workDir= os.getcwd()
        os.chdir(outDir)
        plt.savefig('%sHubbleConstantPlot.pdf'%(filenameTag),bbox_inches='tight', format= 'pdf')
        os.chdir(workDir)
    plt.show()



