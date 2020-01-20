# In acest proiect voi tratata analiza si vizualizarea datelor unui fisier csv in care s-au inserat campuri cu informatii
# despre diferite filme artistice

# importam modulul pandas pentru citirea fisierului csv sub forma de dataframe
import pandas as pd
# importam modulele seaborn si matplotlib pentru constructia si afisarea graficelor
import seaborn as sns
import matplotlib.pyplot as plt
# cu ajutorul modulului warnings nu se vor afisa niciodata mesaje de avertizare
import warnings
warnings.filterwarnings('ignore')

# citirea fisierului csv sub forma de dataframe
# afisarea numarului campurilor (linii x coloane) structurii de date
filme = pd.read_csv('fisierul_meu.csv')
print(80 * '*')
print('Dataframe-ul are urmatorul continut:\n', filme.head(15), filme.tail(15))
print('Structura dataframe-ului (linii si coloane) este:', filme.shape)
print(80 * '*')

# afisarea unui rezumat al dataframe-ului ce include tipul datelor si verificarea lipsei datelor
print('\n', filme.info())
print(80 * '*')

# afisarea statisticii fiecarei coloane al dataframe-ului
print('Statistica fiecarei coloane din dataframe este:\n',filme.describe())
print(80 * '*')

# pregatirea dataframe-ului inainte de inceperea analizei datelor
# verificarea duplicatelor si valorilor NaN existente in dataframe(am utilizat metodele isnull(), respectiv duplicated())
print('Total valorilor NaN existente in fiecare coloane este:\n',filme.isnull().sum())
print('Numarul duplicatelor campurilor inserate in df este:',sum(filme.duplicated()))
print(80 * '*')

# afisarea titlurilor filmelor inserate in dataframe care incep cu litera 'A' si se termina cu litera 'n'
# am utilizat metodele starstwith(), respectiv endswith()
titlu_film = filme[(filme['Titlu'].str.startswith('A') & filme['Titlu'].str.endswith('n'))]['Titlu']
print('Filmele care incep cu lit. A si se termina in litera n sunt:\n',titlu_film)
print(80 * '*')

# sortarea in ordine descendenta a titlurilor filmelor in functie de anul de productie
# (primele 15 filme, respctiv ultimele 15 filme)
# am utilizat metoda sort_values
sortare_filme_p15 = filme[['Titlu', 'An']].sort_values('An', ascending=False).head(15)
sortare_filme_u15 = filme[['Titlu', 'An']].sort_values('An', ascending=False).tail(15)
print('Sortarea in ordine descendenta a titlurilor filmelor in fct de anul productiei:\n',sortare_filme_p15)
print('\n',sortare_filme_u15)
print(80 * '*')

# afisarea titlurilor filmelor inserate in dataframe care s-au produs in Statele Unite ale Americii si au fost produse in studiorile de productie 20th Century Fox
tara_film = filme[(filme['Tara'] == 'United States of America') & (filme['Studio'] == '20th Century Fox')][['Titlu','Studio','Tara']]
print('Filmele produse in SUA in studiourile 20th Century Fox sunt:\n',tara_film)
print(80 * '*')

# afisarea filmelor cu cel mai mic buget estimat, respectiv cel mai mare buget estimat
def buget_mic_mare(coloana):
    # utilizam metoda idxmin() pentru aflarea indexului filmului cu cel mai mic buget
    index_mic = filme[coloana].idxmin()
    # utilizam metoda idxmax() pentru aflarea indexului filmului cu cel mai mare buget
    index_mare = filme[coloana].idxmax()
    # metoda loc are rolul de a selecta randurile(index)si coloanele intr-un dataframe
    mare = pd.DataFrame(filme.loc[index_mare, :])
    mic = pd.DataFrame(filme.loc[index_mic, :])
    # printarea titlurilor filmelor cu cel mai mic si cel mare buget
    print('Filmul cu cel mai mare buget estimat este:', filme['Titlu'][index_mare], '->', filme['Buget'][index_mare],\
          'USD')
    print('Filmul cu cel mai mic buget estimat este:', filme['Titlu'][index_mic], '->', filme['Buget'][index_mic],\
          'USD')
    return pd.concat([mare, mic], axis=1)  # returneaza concatenarea dataframe-urilor
# apelarea functiei
buget_mic_mare('Buget')
print(80 * '*')

# afisarea titlurilor, anilor de productie si actorilor ale filmelor de genul Thriller sau Action
gen_film = filme[(filme['Gen'] == 'Thriller') | (filme['Gen'] == 'Action')][['Titlu', 'Gen']]
print('Filmele genul Action sau Thriller sunt:\n',gen_film)
print(80 * '*')

# afisarea numelor regizorilor care au regizat filme care au durata cuprinsa in intervalul [180,240] minute
durata_film = filme[(filme['Durata'] >= 180) & (filme['Durata'] <= 240)][[ 'Regizor','Durata']]
print('Filmele cu durata cuprinsa in intervalul 180-240 min:\n',durata_film)
print(80 * '*')

# afisarea duratei medii pentru fiecare gen de film
# metoda groupby() imparte datele in grupuri in fuctie pe baza unor criterii
# metoda mean() returneaza media unei axe
media_gen_durata = filme[['Durata', 'Gen']].groupby('Gen').mean()
print('Durata medie pentru fiecare gen de film este:\n',media_gen_durata)
print(80 * '*')

# afisarea titlului filmului cu ratingul cel mai mare, respectiv cel mai mic pentru fiecare gen
rating_film_gen_mare = filme.sort_values('Rating', ascending = False).groupby('Gen')['Titlu','Rating'].max()
rating_film_gen_mic =  filme.sort_values('Rating', ascending = False).groupby('Gen')['Titlu','Rating'].min()
print('Filmul cu ratingul cel mai mare pentru fiecare gen:\n',rating_film_gen_mare)
print('\n')
print('Filmul cu ratingul cel mai mic pentru fiecare gen:\n',rating_film_gen_mic)
print(80 * '*')

# afisarea numelelor actorilor care sunt protagonistii filmelor care au limba principala lb. romana sau lb.spaniola
limba_actor = filme[(filme['Limba'] == 'Romanian') | (filme['Limba'] == 'Spanish')]['Actor_principal']
print('Actorii protagonisti in filmele cu limba principala lb.romana sau spaniola sunt:\n',limba_actor)
print(80 * '*')

# vizualizarea datelor din dataframe
# reprezentarea grafica a distributiilor duratelor, ratingurilor si anilor de productie in dataframe
# distributia datelor intr-un dataframe se realizeaza cu ajutorul reprezentarilor grafice tip histograma
# histogramele sunt realizare cu methoda hist()
# metoda show() afiseaza o figura

filme['Durata'].plot.hist(title='Distributia duratelor filmelor din dataframe', color = 'b')
plt.xlabel('Durata filmului')
plt.ylabel('Numarul filmelor')
plt.show()
filme['Rating'].plot.hist(title='Distributia ratingurilor filmelor din dataframe', color = 'b')
plt.xlabel('Ratingul filmului')
plt.ylabel('Numarul filmelor')
plt.show()
filme['An'].plot.hist(title='Distributia anilor de productie ale filmelor din dataframe', color = 'b')
plt.xlabel('Anul productiei')
plt.ylabel('Numarul filmelor')
plt.show()

# reprezentarea grafica a corelatiei dintre anul de productiei al filmului si durata filmului
# functia regplot() creeaza o linie de regresie intre 2 parametri (in cazul nostru anul filmului respectiv durata,
# buget si rating) si ajuta la vizualizarea relatiei lineare dintre acestia
ax = sns.regplot(x=filme['An'], y=filme['Durata'],color='b')
#setarea titlului si a coordonatelor graficului de tip scatter.
ax.set_title('Corelatia dintre anul de productie si durata',fontsize=16)
ax.set_xlabel('An productie',fontsize=13)
ax.set_ylabel('Durata filmului [min]',fontsize=13)
#setarea marimii si stilul figurii
# plotarea graficului
sns.set(rc={'figure.figsize':(11,8)})
sns.set_style('ticks', {'xtick.major.size': 8, 'ytick.major.size': 8})
plt.show()

#reprezentarea grafica a corelatiei dintre anul de productiei al filmului si bugetul filmului
ax = sns.regplot(x=filme['An'], y=filme['Buget'],color='b')
#setarea titlului si a coordonatelor graficului de tip scatter.
ax.set_title('Corelatia dintre anul de productie si bugetul estimat',fontsize=16)
ax.set_xlabel('An productie',fontsize=13)
ax.set_ylabel('Bugetul filmului [USD]',fontsize=13)
#setarea marimii si stilul figurii
#plotarea graficului
sns.set(rc={'figure.figsize':(11,8)})
sns.set_style('ticks', {'xtick.major.size': 8, 'ytick.major.size': 8})
plt.show()

#reprezentarea grafica a corelatiei dintre anul de productiei al filmului si ratingul filmului
ax = sns.regplot(x=filme['An'], y=filme['Rating'],color='b')
##setarea titlului si a coordonatelor graficului de tip scatter.
ax.set_title('Corelatia dintre anul de productie si rating',fontsize=16)
ax.set_xlabel('An productie',fontsize=13)
ax.set_ylabel('Rating',fontsize=13)
#setarea marimii si stilul figurii
#plotarea figurii
sns.set(rc={'figure.figsize':(11,8)})
sns.set_style('ticks', {'xtick.major.size': 8, 'ytick.major.size': 8})
plt.show()

# afisarea unui grafic de tip boxplot ce reprezinta corelatia dintre tipul filmului si durata acestuia
# setarea componentelor graficului de tip boxplot
sns.boxplot(data=filme, x = 'Tip', y = 'Durata')
#setarea titlului si stilului figurii
plt.title('Corelatia dintre tipul filmului si durata', fontsize = 16)
sns.set_style('ticks', {'xtick0.major.size': 8, 'ytick.major.size': 8})
# plotarea figurii
plt.show()

#afisarea unui grafic de tip barplot orizonatal in care sunt reprezentate cele mai bine cotate 20 de filme
#metoda nlargest() returneaza primele 20 de randuri dupa coloana data in ordine descendenta
top_20_rating = filme.nlargest(20,'Rating')
#setarea componentelor graficului de tip boxplot
sns.barplot(x='Rating', y='Titlu', data=top_20_rating, palette='Blues')
plt.xlabel('Rating')
plt.ylabel('Titlul filmului')
#setarea marimii si stilului figurii
sns.set(rc={'figure.figsize':(11,7)})
sns.set_style('ticks', {'xtick.major.size': 8, 'ytick.major.size': 8})
#setarea titlului figurii
plt.title('Top 20 cele mai bine cotate filme', fontsize = 16)
#plotarea figurii
plt.show()

#afisarea unui grafic de tip barplot orizonatal in care sunt reprezentate cele mai bine lungi 20 de filme
top_20_durata = filme.nlargest(20,'Durata')
sns.barplot(x='Durata', y='Titlu', data=top_20_durata, palette='Greens')
#setarea componentelor graficului de tip boxplot
plt.xlabel('Durata [min]')
plt.ylabel('Titlul filmului')
#setarea marimii si stilului figurii
sns.set(rc={'figure.figsize':(11,7)})
sns.set_style('ticks', {'xtick.major.size': 8, 'ytick.major.size': 8})
#setarea titlului figurii
plt.title('Top 20 cele mai lungi filme', fontsize = 16)
#plotarea figurii
plt.show()

# afisarea unui grafic de tip lmplot care afiseaza relatia dintre ratingul ,durata si limba principala a filmului
# lmplot este o reprezentare grafica liniara cu parametri aditionali
# parametrul 'Limba' este subset al graficului si va fi desenat separat
# setarea fundalului figurii
sns.set_style('white')
#setarea componentelor si titlului graficului
sns.lmplot(data=filme, x='Rating', y='Durata', fit_reg=False, hue='Limba', size=6, aspect=1)
plt.title('Relatie rating - durata - limba', fontsize = 14)
#setarea numelui coordonatelor
plt.xlabel('Rating')
plt.ylabel('Durata [min]')
#setarea paletelor de culori
#plotarea figurii
plt.show()

# afisarea unui grafic de tip lmplot care afiseaza relatia dintre ratingul ,durata si tara de provenienta a filmului
# parametrul 'Tara' este subset al graficului si va fi desenat separat (hue)
# setarea fundalului figurii
sns.set_style('white')
#setarea componentelor si titlului graficului
sns.lmplot(data=filme, x='Rating', y='Durata', fit_reg=False, hue='Tara', size=6, aspect=1)
plt.title('Relatie rating - durata - tara', fontsize = 14)
#setarea numelui coordonatelor
plt.xlabel('Rating')
plt.ylabel('Durata [min]')
#setarea paletelor de culori
sns.color_palette('dark')
#plotarea figurii
plt.show()


