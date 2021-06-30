#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df = pd.read_csv('full_limpo.csv')
df = df.drop(['Unnamed: 0'],axis=1)
df.head()


# In[6]:


df.columns #visualizar todas as colunas do data set 


# In[7]:


df.shape #quantidade de dados 


# In[8]:


df.info() # informações sobre os dados 


# In[17]:


df.isnull().sum() # isnull metodo que verfica valores nulos, sum() soma todas os valores 


# In[13]:


a = df.price.median()


# In[14]:


df['price'] = df['price'].fillna(a)  #função fillna()substitui os valores por de price por a
df['condo'] = df['condo'].fillna(0)  # ou zero 


# In[16]:


df = df.dropna() #remove linhas com valores nulos 


# In[18]:


df.shape


# In[19]:


df.index = df['id']
df = df.drop(['id'],axis=1)
df.head()


# In[21]:


df.price.hist();


# In[22]:


import seaborn as sns
sns.distplot(df['price']);


# In[25]:


df.describe()


# In[24]:


df = df[df.price <= 20000]


# In[26]:


import matplotlib.pyplot as plt


# In[27]:


plt.figure(figsize=(10,6))
plt.scatter(df['area'],df['price'], color = 'k', alpha=0.2)
plt.ylim([0,10000])
plt.xlabel('Área',fontsize=18)
plt.ylabel('Preço do aluguel',fontsize=18)


# In[28]:


df2 = df.sample(500) # sample() pega uma quantidade de dados do banco para plotar os graficos 


# In[29]:


sns.pairplot(df2, kind='reg')


# In[30]:


sns.pairplot(df2, plot_kws={'alpha':0.2})


# In[31]:


df.corr() # calculada a correlação 


# In[32]:


sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")


# In[33]:


df.boxplot('price')


# In[34]:


sns.boxplot(x='neighborhood', y='price', data=df)


# In[35]:


centro = ['Centro','Bela Vista','Bom Retiro','Cambuci','Consolação','Vila Monumento','Luz',
          'Higienópolis','Liberdade','República','Santa Cecília','Sé','Paraíso','Santa Efigênia',
         'Aclimação','Campos Eliseos','Campos Elíseos','Cerqueira César','Planalto Paulista',
         'Vila Monte Alegre','Vila Buarque','Jardim da Glória','Vila Moinho Velho']

norte = ['Norte','Anhanguera','Brasilândia','Casa Verde','Cachoeirinha','Freguesia do Ó','Jaçanã','Jaraguá',
    'Limão','Mandaqui','Perus','Pirituba','Santana','São Domingos','Tremembé','Tucuruvi','Vila Maria','Vila Iório',
    'Vila Medeiros','Vila Guilherme','Jardim Peri Peri','Vila Constança','City América','Jardim Yara',
        'Vila Paulistana','Sitio Botuquara','Jardim Shangrila','Jardim Franca','Vila Isolina Mazzei','Chora Menino',
        'Vila Zat','Água Fria','Jardim Japão','Vila Mangalot','Vila Carbone','Sítio Botuquara','Horto Florestal',
        'Vila Nova Mazzei','Imirim','Jardim São Paulo','Vila Libanesa','Vila Americana','Parque São Luís',
        'Lauzane Paulista','Vila Palmeiras','Vila Ede','Vila Prado']

sul = ['Sul','Chácara Klabin','Campo Belo','Campo Limpo','Capão Redondo','Cidade Ademar','Cidade Dutra','Cursino','Grajaú',
    'Itaim Bibi','Ipiranga','Jabaquara' ,'Jardim Ângela' ,'Jardim São Luís','Marsilac', 'Moema',
    'Moema Pássaros','Moema Índios','Morumbi','Parelheiros','Pedreira','Sacomã','Jardim Avenida',
    'Santo Amaro','Socorro','Saúde','Vila Andrade','Vila Mariana','Vila Olímpia','Vila Mascote','Brooklin',
       'Vila Gumercindo','Vila Cruzeiro','Vila Gertrudes','Vila Arriete','Parque Colonial','Vila Clementino',
       'Vila Sofia','Vila Uberabinha','Jardim Dom Bosco','Jardim Aeroporto','Vila Congonhas','Indianópolis',
       'Brooklin Novo','Brooklin Paulista','Cidade das Monções','Cidade Monções','Jardins','Vila Nova Conceição',
      'Chácara Inglesa','Vila Santa Maria','Balneário Mar Paulista','Ferreira','Jardim Prudência','Chácara Flora',
      'Vila Tramontano','Jardim Hípico','Chácara Nossa Senhora do Bom Conselho','Cidade Domitila','Vila Castelo',
       'Chácara Santo Antônio','Jardim das Acacias','Vila Santo Estéfano','Alto Da Boa Vista','Parque Lagoa Rica',
      'Jardim Petrópolis','Guarapiranga','Jardim Cordeiro','Jardim dos Estados','Chácara Santa Maria',
      'Jardim das Acácias','Jardim Aurélia','Jardim Ampliação','Jardim Satélite','Interlagos','Jardim da Saude',
      'Jardim Represa','Jardim Vitória Régia','Jardim Sandra','Real Parque','Vila Dom Pedro I','Vila Guarani',
       'Chácara Vista Alegre','Vila Cordeiro','Jardim Santo Antoninho','Vila Santa Catarina','Nova Piraju',
      'Jordanópolis','Jardim Iracema','Vila Anhangüera','Vila Nair','Jardim Leonor','Chácara Bosque do Sol',
      'Vila Império','Vila Imperio','Jardim dos Lagos','Jardim Vilas Boas','Jardim Panorama','Chácara Monte Alegre',
       'Jardim Caboré','Jardim Taquaral','Praia da Lagoa','Jardim Marajoara','Paulicéia','Varginha',
       'Cidade Jardim','Jardim Francisco Mendes','Jardim Santa Tereza','Alto da Boa Vista','Parque Maria Fernandes']

leste = ['Leste','Água Rasa','Aricanduva','Artur Alvim','Belém','Brás','Cangaíba','Carrão','Cidade Líder',
    'Cidade Tiradentes','Ermelino Matarazzo','Guaianases','Itaim Paulista','Itaquera','Vila Invernada',
    'Jardim Helena','José Bonifácio','Lajeado','Mooca','Pari','Parque do Carmo','Penha','Vila Primavera',
    'Ponte Rasa','São Lucas','São Mateus','São Miguel','São Rafael','Sapopemba','Tatuapé','São João Clímaco',
         'Quarta Parada','Jardim Tietê','Vila Antonieta','Cidade Mãe do Céu','Vila Regente Feijó','Vila Antonina',
         'Chácara Belenzinho','Belenzinho','Jardim Egle','Cidade Vargas','Cidade Satélite Santa Bárbara',
    'Vila Curuçá','Vila Formosa','Vila Jacuí','Vila Matilde','Vila Prudente','Mooca','Tatuapé','Carandiru',
         'Mirandópolis','Vila Brasilina','Móoca','Jardim Anália Franco','Parque São Jorge','Sítio Pinheirinho',
        'Vila Pierina','Vila São Silvestre','Vila Ema','Parque Novo Mundo','Jardim Paraguaçu','Vila Santo Estevão',
        'Conjunto Habitacional Barreira Grande','Vila Santa Clara','Parque Savoy City','Jardim Avelino',
        'Vila Azevedo','Vila Dalila','Vila Bertioga','Jardim Popular']


oeste = ['Oeste','Alto de Pinheiros','Barra Funda','Butantã','Jaguará','Jardim Paulista','Jardim Paulistano',
    'Jardim Europa','Jardim América','Lapa','Morumbi','Perdizes','Pinheiros','Raposo Tavares','Rio Pequeno'
    'Vila Leopoldina','Vila Madalena','Vila Sônia','Sumarezinho','Sumaré','Boaçava','Jardim das Vertentes',
        'Rio Pequeno','Vila Leopoldina','Panamby','Jardim Monte Kemel','Pompeia','Vila Pompéia',
         'Vila Anglo Brasileira','Vila Romana','Pacaembu','Água Branca','Jardim Guedala','Jardim Everest',
        'Vila Gomes','Jardim das Bandeiras','Jardim Umuarama','Jardim Esmeralda','Jaguaré','Jardim Bonfiglioli',
        'Vila Inah','Jardim Rizzo','Vila Suzana','Parque Ipê','Vila Indiana','Cidade São Francisco',
         'Granja Julieta','Bela Aliança','Caxingui','Vila Tiradentes','Lar São Paulo',
        'Vila Progredior','Vila São Francisco','Vila Prel','Jardim Celeste']


# In[36]:


def checar_zona(df,lista):
    df = df[df.address.str.contains(('|').join(lista))]
    df['zona'] = str(lista[0])
    return df


# In[37]:


df1 = checar_zona(df,oeste)
df1.shape


# In[38]:


df2 = checar_zona(df,sul)
df3 = checar_zona(df,leste)
df4 = checar_zona(df,centro)
df5 = checar_zona(df,norte)


# In[39]:


nenhuma = ['Nenhuma']
bairros = nenhuma + oeste + sul + leste + centro + norte
def checar_zona_nenhuma(df,lista):
    df = df[~df.address.str.contains(('|').join(lista))]
    df['zona'] = str(lista[0])
    return df


# In[40]:


df6 = checar_zona_nenhuma(df,bairros)
df6.shape


# In[41]:


df6.head()


# In[42]:


df_final = pd.concat([df1,df2,df3,df4,df5])


# In[43]:


df_final = df_final.drop_duplicates(subset=['address','price'], keep='last')
df_final.shape


# In[45]:


sns.boxplot(x='zona', y='price', data=df_final);


# In[46]:


sns.pairplot(df_final, hue='zona');


# In[47]:


ax = sns.FacetGrid(df_final, col='zona', size=6.5)
ax.map(plt.scatter, 'area','price',alpha=0.3)


# In[52]:



import plotly.graph_objs as go
from plotly.offline import iplot


# In[53]:


trace1 = go.Scatter(x = df1.area,
                   y = df1.price,
                   mode='markers', 
                   name='Oeste',
                   marker = dict(color = 'rgba(255,128,255,0.8)'),
                    text=df1.zona)

trace2 = go.Scatter(x = df2.area,
                   y = df2.price,
                   mode='markers', 
                   name='Sul',
                   marker = dict(color = 'rgba(255,128,2,0.8)'),
                    text=df2.zona)

trace3 = go.Scatter(x = df3.area,
                   y = df3.price,
                   mode='markers', 
                   name='Leste',
                   marker = dict(color = 'rgba(0,255,0,0.8)'),
                    text=df3.zona)

trace4 = go.Scatter(x = df4.area,
                   y = df4.price,
                   mode='markers', 
                   name='Centro',
                   marker = dict(color = 'rgba(0,125,100,0.8)'),
                    text=df4.zona)

trace5 = go.Scatter(x = df5.area,
                   y = df5.price,
                   mode='markers', 
                   name='Norte',
                   marker = dict(color = 'rgba(0,0,255,0.8)'),
                    text=df5.zona)

data = [trace1, trace2, trace3, trace4, trace5]
layout = dict(title='Área e Preço do Aluguel em SP',
             xaxis=dict(title='Área'),
             yaxis=dict(title='Preço'))

fig = dict(data = data, layout=layout)
iplot(fig)


# In[51]:


pip install plotly


# In[ ]:




