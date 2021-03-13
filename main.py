import discord
import random
client = discord.Client()

t1 = ['Proszę zwrócić uwagę, że ',
      'I tak mam trzy razy mniej czasu, więc proszę pozwolić mi pozwolić powiedzieć: ',
      'Państwo się się śmieją, ale ', 'Ja nie potrzebowałem edukacji seksualnej, żeby wiedzieć, że ',
      'No niestety: ', 'Grzie leży przyczyna problemu? Ja państwu powiem: ',
      'Państwo chyba nie widzą, że ',
      'Oświadczam kategorycznie: ',
      'Powtarzam: ',
      'Powiedzmy to z całą mocą: ',
      'W Polsce dzisiaj ',
      'Państwo sobie nie zdają sprawy, że ',
      'To ja przepraszam bardzo: ',
      'Otóż nie wiem, czy pan wie, że ',
      'Yyyyy... ', 'Ja chcę powiedzieć jedną rzecz: ',
      'Trzeba powiedzieć jasno: ',
      'Jak powiedział wybitny krakowianin Stanisłąw Lem, ',
      'Proszę mnie dobrze zrozumieć: ',
      'Ja chciałem państwu przypomnieć, że ',
      'Niech państwo nie mają złudzeń: ',
      'Powiedzmy to wyraźnie ']
t2 = ['właściciele niewolników ',
      'związkowcy ',
      'trockiści ',
      'tak zwane dzieci kwiaty ',
      'rozmaici urzędnicy ',
      'federaści ',
      'etatyści ',
      'ci drunie i złodzieje ',
      'ludzie wybrani głosami meneli spod budki z piwem ',
      'socjaliści pobożni ', 'socjaliści bezbożni ',
      'komuniści z krzyżem w zębach ',
      'agenci obcych służb ',
      'członkowie Bandy Czworga ',
      'pseudo-masoni z Wielkiego Wschodu Francji ',
      'przedstawiciele czerwonej hołoty ',
      'ci wszyscy (tfu!) geje ',
      'funkcjonariusze reżymowej telewizji ',
      'tak zwani ekolodzy ',
      'ci wszyscy (tfu!) demokraci ',
      'agenci bezpieki ',
      'feminazistki']
t3 = ['po przeczytaniu Manifestu komunistycznego',
      'którym się brzydze',
      'których nienawidzę',
      'z okolic "Gazety Wyborczej',
      'czyli taka żydokomuna',
      'odkąd zniesiono karę śmierci',
      'którymi pogardzam',
      'których miejsce w normalnym kraju jest w więzieniu',
      'na polecenie Brukseli',
      'posłusznie',
      'bezmyślnie',
      'z nieprawdopodobną pogardą dla człowieka',
      'za pieniądze podatników',
      'zgodnie z ideologią LGBTQZ',
      'za wszelką cenę',
      'zupełnie bezkarnie',
      'całkowicie bezkarnie',
      'o poglądach na lewo od komunizmu',
      'celowo i świadomie',
      'z premedytacją',
      'od czasów Okrągłego stołu',
      'w ramach postępu', ]
t4 = ['rząd','rzad','podatki','pis','duda','***** ***']
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('elo'):
        await message.channel.send('elo')

@client.event
async def on_message(message):
    res = [ele for ele in t4 if (ele in message.content)]
    if str(bool(res)) == 'True':
        await message.channel.send(t1[random.randint(0, 20)] + t2[random.randint(0, 20)] + t3[random.randint(0, 20)])



client.run('ODE5OTk2ODY5MzE2MzEzMDg5.YEuvmA.EF3zxuwAdH6XMJ3qGswAwwuE6gw')
