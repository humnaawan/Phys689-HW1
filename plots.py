import numpy as np
import matplotlib.pyplot as plt
import os

legendFontSize= 14
axisLabelFontSize= 18
tickLabelFontSize= 16

colors= ['r', 'g', 'b', 'm', 'y', 'c']
fixedColor= 'k'

def scaleFactorPlot(a, t, H0, factor_sToGyr, xMax= 100, yMax= 5,
                    plotTitle= '', legendloc= 4,
                    savePlots= False, outDir= None, filenameTag= ''):
    # t, H0 in seconds
    # a, t are dictionaries
    plt.clf()
    for i, key in enumerate(a):
        tscaled= t[key]/factor_sToGyr   # now in Gyr
        plt.plot(tscaled, a[key], '.', label= key, color= colors[i])
        plt.plot(tscaled, a[key], color= colors[i])
    plt.xlim(0, xMax)   
    plt.ylim(0, yMax) 
    t0= 1/H0  # s
    t0= t0/factor_sToGyr # Gyr
    
    plt.plot([t0, t0], [0.,yMax], label= '$Today$', color= fixedColor)
    plt.title(plotTitle, fontsize= axisLabelFontSize)
    plt.xlabel(r'$t \ (Gyr)$', fontsize= axisLabelFontSize)
    plt.ylabel('$a$', fontsize= axisLabelFontSize)
    plt.tick_params(axis='x', labelsize=tickLabelFontSize)
    plt.tick_params(axis='y', labelsize=tickLabelFontSize)
    plt.legend(fontsize= legendFontSize, loc= legendloc)#bbox_to_anchor= (0.7, 1.7))
    
    fig= plt.gcf()
    fig.set_size_inches(12,6)
    if savePlots:
        workDir= os.getcwd()
        os.chdir(outDir)
        plt.savefig('%sscaleFactorPlot.eps'%(filenameTag),bbox_inches='tight', format= 'eps')
        os.chdir(workDir)
    plt.show()

def adotPlot(adot, t, H0, factor_sToGyr, xMax= 100, yMin= 0, yMax= 5,
             plotTitle= '', legendloc= None,
             savePlots= False, outDir= None, filenameTag= ''):
    # t, H0 in seconds
    # adot, t are dictionaries
    plt.clf()
    for i, key in enumerate(adot):
        tscaled= t[key]/factor_sToGyr   # now in Gyr
        plt.plot(tscaled, adot[key]*factor_sToGyr, '.', label= key, color= colors[i])
        plt.plot(tscaled, adot[key]*factor_sToGyr, color= colors[i])
    plt.xlim(0, xMax)
    plt.ylim(yMin, yMax)
    t0= 1/H0  # s
    t0= t0/factor_sToGyr # Gyr
    
    plt.plot([t0, t0], [yMin,yMax], label= '$Today$', color= fixedColor)
    plt.plot([0, xMax], [0., 0.], ':', color= fixedColor)
    plt.title(plotTitle, fontsize= axisLabelFontSize)
    plt.xlabel(r'$t \ (Gyr)$', fontsize= axisLabelFontSize)
    plt.ylabel('$\dot{a} \ (Gyr^{-1})$', fontsize= axisLabelFontSize)
    plt.tick_params(axis='x', labelsize=tickLabelFontSize)
    plt.tick_params(axis='y', labelsize=tickLabelFontSize)
    if legendloc is None:
        plt.legend(fontsize= legendFontSize, bbox_to_anchor= (1.0, .9))
    else:
        plt.legend(fontsize= legendFontSize, loc= legendloc)
    fig= plt.gcf()
    fig.set_size_inches(12,6)
    if savePlots:
        workDir= os.getcwd()
        os.chdir(outDir)
        plt.savefig('%sadotPlot.eps'%(filenameTag),bbox_inches='tight', format= 'eps')
        os.chdir(workDir)
    plt.show()

def densityPlot(rhoTotal, t, H0, factor_sToGyr, xMax= 40, yMax= 30,
                plotTitle= '',
                savePlots= False, outDir= None, filenameTag= ''):
    plt.clf()
    for i, key in enumerate(rhoTotal):
        tscaled= t[key]/factor_sToGyr   # now in Gyr
        plt.plot(tscaled, rhoTotal[key], '.', label= key, color= colors[i])
        plt.plot(tscaled, rhoTotal[key], color= colors[i])
    plt.xlim(0, xMax)
    plt.ylim(0, yMax)
    t0= 1/H0  # s
    t0= t0/factor_sToGyr # Gyr
    plt.plot([t0, t0], [0.,yMax], label= '$Today$', color= fixedColor)
    plt.title(plotTitle, fontsize= axisLabelFontSize)
    plt.xlabel(r'$t \ (Gyr)$', fontsize= axisLabelFontSize)
    plt.ylabel(r'$\rho_{tot}/\rho_{crit, 0}$', fontsize= axisLabelFontSize)
    plt.tick_params(axis='x', labelsize=tickLabelFontSize)
    plt.tick_params(axis='y', labelsize=tickLabelFontSize)
    plt.legend(loc=1, fontsize= legendFontSize)
    
    fig= plt.gcf()
    fig.set_size_inches(12,6)
    if savePlots:
        workDir= os.getcwd()
        os.chdir(outDir)
        plt.savefig('%sdensityPlot.eps'%(filenameTag),bbox_inches='tight', format= 'eps')
        os.chdir(workDir)
    plt.show()


def HubbleConstantPlot(a, adot, t, H0, factor_sToGyr, xMax= 40, yMax= 300,
                       plotTitle= '',
                       savePlots= False, outDir= None, filenameTag= ''):
    H= {}   # 1/s
    plt.clf()
    for i, key in enumerate(a):
        H[key]= adot[key]/a[key]  # 1/s
        H[key]= H[key]*3.086*10**19
        tscaled= t[key]/factor_sToGyr   # now in Gyr
        plt.plot(tscaled, H[key], '.', label= key, color= colors[i])
        plt.plot(tscaled, H[key], color= colors[i])
    plt.xlim(0, xMax)   
    plt.ylim(0, yMax)
    t0= 1/H0  # s
    t0= t0/factor_sToGyr # Gyr
    plt.plot([t0, t0], [0.,yMax], label= '$Today$', color= fixedColor)
    plt.plot([0, xMax], [H0*3.086*10**19, H0*3.086*10**19], '-.', color= fixedColor,
             label= '$Input \ H_0: %s \ (km/s/Mpc)$'%(H0*3.086*10**19))
    plt.title(plotTitle, fontsize= axisLabelFontSize)
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
        plt.savefig('%sHubbleConstantPlot.eps'%(filenameTag),bbox_inches='tight', format= 'eps')
        os.chdir(workDir)
    plt.show()



