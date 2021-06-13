import discord
import random

client = discord.Client()

t1 = ['Proszę zwrócić uwagę, że ',
      'I tak mam trzy razy mniej czasu, więc proszę pozwolić mi pozwolić powiedzieć: ',
      'Państwo się śmieją, ale ', 'Ja nie potrzebowałem edukacji seksualnej, żeby wiedzieć, że ',
      'No niestety: ', 'Gdzie leży przyczyna problemu? Ja państwu powiem: ',
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
      'Jak powiedział wybitny krakowianin Stanisław Lem, ',
      'Proszę mnie dobrze zrozumieć: ',
      'Ja chciałem państwu przypomnieć, że ',
      'Niech państwo nie mają złudzeń: ',
      'Powiedzmy to wyraźnie ']
t2 = ['właściciele niewolników ',
      'związkowcy ',
      'trockiści ',
      'tak zwane dzieci kwiaty ',
      'rozmaici urzędnicy ',
      'federaci ',
      'statyści ',
      'ci druhnie i złodzieje ',
      'ludzie wybrani głosami meneli spod budki z piwem ',
      'socjaliści pobożni ', 'socjaliści bezbożni ',
      'komuniści z krzyżem w zębach ',
      'agenci obcych służb ',
      'członkowie Bandy Czworga ',
      'pseudo-masoni z Wielkiego Wschodu Francji ',
      'przedstawiciele czerwonej hołoty ',
      'ci wszyscy ***tfu!*** geje ',
      'funkcjonariusze reżymowej telewizji ',
      'tak zwani ekolodzy ',
      'ci wszyscy ***tfu!*** demokraci ',
      'agenci bezpieki ',
      'feminazistki']
t3 = ['po przeczytaniu Manifestu komunistycznego',
      'którym się brzydzę ',
      'których nienawidzę ',
      'z okolic "Gazety Wyborczej ',
      'czyli taka żydokomuna ',
      'odkąd zniesiono karę śmierci ',
      'którymi pogardzam ',
      'których miejsce w normalnym kraju jest w więzieniu ',
      'na polecenie Brukseli ',
      'posłusznie ',
      'bezmyślnie ',
      'z nieprawdopodobną pogardą dla człowieka ',
      'za pieniądze podatników ',
      'zgodnie z ideologią LGBTQZ ',
      'za wszelką cenę ',
      'zupełnie bezkarnie ',
      'całkowicie bezkarnie ',
      'o poglądach na lewo od komunizmu ',
      'celowo i świadomie ',
      'z premedytacją ',
      'od czasów Okrągłego stołu ',
      'w ramach postępu ', ]
t4 = ['udają homoseksualistów ',
      'niszczą rodzinę ',
      'idą do polityki ',
      'zakazują góralom robienia oscypków',
      'organizują paraolimpiady ',
      'wprowadzają ustrój w którym raz na cztery lata można sobie wybrać pana ',
      'ustawiają fotoradary ',
      'wprowadzają dotacje ',
      'wydzielają buspasy ',
      'podnoszą wiek emerytalny ',
      'rżną głupa ',
      'odbierają dzieci rodzicom ',
      'wprowadzają absurdalne przepisy ',
      'umieszczają dzecie w szkołach koedukacyjnych ',
      'wprowadzają parytety ',
      'nawołują do podniesienia podatków ',
      'próbują wyrzucić kierowców z miast ',
      'głoszą brednię o globalnym ocieplaniu ',
      'zakazują posiadanie broni ',
      'nie dopuszczają prawicy do władzy ',
      'próbują skłócić Polskę z Rosją ',
      'głoszą brednie o globalnym ociepleniu ',
      'uczą dzieci homoseksualizmu '
      ]
t5 = ['żeby podawać wszystkich tresurze',
      'bo taka jest ich natura',
      'bo chcą wszystko kontrolować',
      'bo nie rozumieją, że socjalizm nie działa ',
      'żeby wreszcie zapanował socjalizm',
      'dokładnie tak jak tow. Janosik',
      'zamiast pozwolić ludziom zarabiać',
      'żeby wyrwać kobiety z domu',
      'bo to jest w Internecie, tak zwanych ludzi pracy',
      'zamiast pozwolić decydować konsumentowi ',
      'żeby nie opłacało się mieć dzieci ',
      'zamiast obniżyć podatek ',
      'bo nie rozumieją że selekcja naturalna jest czymś dobrym ',
      'żeby mężczyźni przestali być agresywni',
      'bo dzięki temu mogą brać łapówki',
      'bo dzięki temu mogą kraść',
      'bo dostaną za to pieniądze ',
      'bo tak się uczy w państwowej szkole ',
      'bo bez tego ***tfu*** demokracja nie może istnieć ',
      'bo głupich jest więcej niż mądrych ',
      'bo chcą tworzyć raj na ziemi ',
      'bo chcą niszczyć cywilizację białego człowieka ']

t6 = ['co ma zresztą tyle samo sensu co zawody w szachach dla debili. ',
      'co zostało dokładnie zaplanowane w Magdalence przez śp. generała Kiszczaka.',
      'i trzeba być idiotą, żeby popierać taki system.',
      'ale nawet ja jeszcze dożyję normalnych czasów.',
      'co dowodzi że wyskrobano nie tych co trzeba.',
      'a zwykłym ludziom wmawiają, że im coś "dadzą".',
      '-cóż chcieliście ***tfu*** demokracji, tam macie!',
      'dlatego trzeba zlikwidować koryto, a nie zmieniać świnie',
      'a wystarczy przestać wypłacać zasiłki.',
      'podczas gdy normalni ludzie uważani są za dziwaków.',
      'co w wieku XIX po prostu by wyśmiano',
      '-dlatego trzeba przywrócić normalność.',
      'ale w wolnej Polsce pójdą siedzieć.',
      'przez kolejne kadencje.',
      'o czym się nie mówi',
      'i właśnie dlatego Europa umiera.',
      'ale przyjdą Muzułmanie i zrobią porządek.',
      '- tak samo zresztą jak za Hitlera',
      '- proszę zobaczyć co się dzieje za Zachodzie jeśli mi państwo nie wierzą.',
      'co lat temu sto nikomu nie przyszło by do głowy.'
      ]

trigger = ['rząd', 'rzad', 'podat', ' pis ','pis ', 'duda', '***** ***']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        res = [ele for ele in trigger if (ele in message.content.lower())]
        if str(bool(res)) == 'True':
            await message.channel.send(t1[random.randint(0, len(t1) - 1)] + t2[random.randint(0, len(t2) - 1)] + t3[
                random.randint(0, len(t3) - 1)] + t4[random.randint(0, len(t4) - 1)] + t5[
                                           random.randint(0, len(t5) - 1)] + t6[random.randint(0, len(t6) - 1)])


client.run('')
