import numpy as np
import matplotlib.pyplot as plt




x = np.linspace(-3, 3, 50)
y = 2*x + 1
y1= x*x
plt.figure() #Définir une fenêtre d'image

plt.xlabel('x axes')
plt.ylabel('y axes,')

plt.plot(x, y,label='first one') #Tracer une courbe (x, y)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--',label='second one') #courbes avec styles et couleurs

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.3,-1,1,2.2]) #    plt.yticks([-2,-1.3,-1,1,2.2],['bad','not bad','goog','really good'])

plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

plt.legend(loc='upper right')

plt.show()