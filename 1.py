
edades =[int(x) for x in input("ingresa edades separadas por espacio :").split()]
media=sum(edades) / len(edades)
mediana = sorted(edades)[len(edades)//2]
print(f"\media (promedio) : {media:.1f} años")
print(f"\mediana(valor central): {mediana} años")
import matplotlib.pyplot as  plt 
plt.plot(edades ,'o-',label='edades')
plt.axhline(media, color='r' , label=f'media: {media:.1f}')
plt.axhline(mediana, color='g', label=f'mediana: {mediana }')
plt.legend()
plt.show()
