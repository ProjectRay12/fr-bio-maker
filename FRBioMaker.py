import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

#----------------image setup----------------
emblemCodex=[
    ['dsTktuQ','8NDH06n','37OYYcl','XAposRo','yGbviTW','BUaBUQT','IhKsIOy','MggfJYn','UKyyqQv','eb6yC6j','jwI0Gj9','RKuPfOT','y9rSfFN','6mpXNyb'],
    ['VXQQRAW','AHNgpcJ','DoNuQyD','yvXGBoV','6mnGgeQ','i7VsuQL','mjav63V','vxOzpeQ','YjJ5iHe','3UB7oeU','DdhYiV6','S5jSC97','UDhGpEY','fF14MzS'],
    ['qncXU7t','4xhUu91','dGPPrS6','mpYGshV','QVcG252','Unj2ycE','NrJI4DZ','MEHUbJv','qjG0CA5','TphOIRI','tehIqgR','iQUJ7Uq','Eg4yABU','Z7qWCOH'],
    ['8sspNet','L5vmrvu','YyfPKT9','f2WWAWe','13MVuRe','I23raUq','fVfA33C','u2k8DKF','rp5vIdp','pK7oKjy','9CjxgRh','sGfRJlJ','OkGt4sp','uVRSdGY'],
    ['VImLzPc','7zJAX9j','z72Ba79','qxxCBDU','Yx3PhkQ','IOJ1dfI','UP3TcXX','csL3aZQ','otPQlbl','C34Y7br','JPU1VQa','enVGw2p','eNFssG6','Qa0DdXr'],
    ['HMb8MPT','LwJbqbv','VHJvQd0','3APoeXm','4XFJcMV','nQH9v4o','Pv5755f','hT1zl9U','UrHjYvX','cCH8D1Q','EpYiPBM','MicTAh5','IkSP4sc','zhU2SzF'],
    ['FkRYUhS','7m5kIC9','fSz8xQi','KBJ3bxx','ARkbJIR','Y2rpJ0y','avHDVcX','xJiMGL5','HmaA36K','pFmwlrl','r5RzCzh','iQMJyHc','WhU7JwZ','kMrj5qK'],
    ['IhkNJn0','6vNB29j','HS3lwvm','PytnhtA','erfAbuI','bCsYHUF','MYcYdt9','7D6hHRv','Ym2yz9F','GAWDrI0','IGwlEAU','e56vXNe','valgybD','4YMZjkZ'],
    ['u90Y4uD','7BKsjTY','0DRMjbC','iBmhvYB','RZ0lHM3','yHEv3BB','h1FwKFl','lbguevz','SMn8YCr','hRFLjAM','S8owy84','8qe3sLN','fZvn76O','1wRqKZz'],
    ['lQ9TAh2','MXsUPF1','Jlf2trT','zBbefSe','KXTGtQx','3NtTvtC','h9SZenW','3nVcbst','1M8zVgw','sWAbK69','BsVKlkU','rPUJHop','k5d0mdx','LMrP9TQ'],
    ['afuX6cT','TOv6WlQ','fD7XBvu','sMSU318','Xg2xX8R','lNVIG8M','GEayzvN','shBAGpC','Y8dAOtE','9wx6IRh','8HG3UTr','DKano7V','oiha6iU','4IGS70g'],
    ['m1KCm1K','RfMYS6B','U4e8m4H','Sw9aNdI','IKarnKq','hZdPYGe','lZERDtA','Lbs8pmz','pFU9N18','njFR7ML','M5SG7k3','CZ7MbhS','dU7pFEc','yHLSAsq'],
    ['5vQuH08','V85lSSL','WGtL3pN','R9XHnDq','lJq4MRN','8T4zkjd','RRzzjuB','vZKj21F','7iL8bGg','AYOillV','6Nvpd9L','RTnS1Sw','9tKtH1M','lQmH4SU'],
    ['RrjcAY2','qpJVIKj','gZ7qTTY','5HsmQfT','WPobcI9','Mc22IDC','tcGdjOn','nXHV1C1','S3aLnLn','GxzeGUj','dU2zovc','WV5elFr','lDQ8maq','REOMP4J'],
    ['t0BIdtl','K0t62Am','vxrsMFe','hrYOM6s','dSkKQHm','gVvHjE0','Lbmttpx','hMwiuEu','aGIKabJ','JKXtMGs','PvyhIgu','n5AMSzj','hguEJFI','5PHCjpV'],
    ['glcm6YR','9xgs6nK','qCK8APq','vNVlo8f','osv9qp9','nCHdYO4','XJibV2Q','WHBcLZN','HV2dlQz','2nlYAe8','gWVwCeO','uomKlyB','MNCQghG','1wIDtJe'],
    ['HGZNcZj','oLCcTng','PInQbaM','FRUtfSh','mKADxS5','0tTVBcH','DsXVv7W','KjIXFgy','iVcaWHc','O5xSiaU','DTf9Ivh','RQAFuBr','Z0OMG7s','2vogWaZ'],
    ['c012kR9','15uu93A','wWiF1PO','7GRSB7a','bl3Gft8','POcyDZB','zbgbQpz','hEzwIF9','kd9hdOv','a9zQ9LQ','oDmjUfe','Vwri02P','T8MfW9Z','JGSeOmE'],
    ['FzGy9j8','Vbf7auj','b0RFo3O','hwXnSi1','UjeWF7n','Gq3faIF','Ii0SJKT','Vp9HIZc','oZAjoWa','CD08b22','C2ZJuVV','b9A9K57','jFx0oY7','7xyJjy8'],
    ['lneKO9r','Mj1APyB','If6dJGG','sYm8XHs','wuxIZj5','j6jS8b1','FcyJxUE','XTFBGbY','QxzkUCP','A6Un3Iw','pUEebXl','zGeLV2Q','LfR2ZmU','hxedFtq'],
    ['Wuj2WKM','1mERgUM','qvQqUDf','l9jN0OZ','QvHGEN7','ip2cn2k','BZ1EkVb','jpvpOZU','cwBHzyG','opBNYbJ','BhKbjqa','5qi5hWI','q0WJlWx','LyWqgLp'],
    ['dM8ZsAW','sfSk6P2','iZgyhTZ','n3qvRpc','kVR8gHl','mvSvDmh','wbR3gwO','kRaLXcu','KZd6x03','qkBtRLY','kTliHaP','crgtwWD','51Nud1u','Jsq4G8C'],
    ['GTPz1c3','Z07iIhJ','MKt1wXK','L2p9PGu','9S0ao0L','v8f3vk3','vDfx0jg','eqHQRFQ','G9XyGeb','IK9ELVx','hY99qjc','s2sjTVr','0ZijjMD','JvIRo4Q'],
    ['dXIk2uy','ZhnyrAQ','OnzvSu3','ExtxOuB','HcXJ27S','4gDd1ix','L2LiOAv','R4i3eEz','VrVrFJF','kEcoLs3','lwZVH7T','7rkzc5t','KdiinA3','8MncBBp'],
    ['WoUwFXh','Bxh3ytb','25PEEt6','BiijwM9','2i3ewdp','9kFWF8l','E3odZX0','X7F8BiF','gU0iRjN','lgPswgM','n7YE6qX','w377uwI','W9NkKq0','sgzneAY'],
    ['WSTv0K0','rHJzTMY','lndoL8B','OZBPi6A','947ZGsp','WxJfgVf','D517JUG','th3ypmc','6kEMoHF','kW6P8Y8','FpizC2z','wqSnC0V','6PZKMV5','lrIXexO'],
    ['ssNUPXc','vG1FuLW','YyxdVdT','P6uCEMU','tpGwQbp','hpzmAeI','tcABNWz','MEFp1sd','XFK6xQD','1E0BXvU','JJcThIl','cvtWUw1','KT8XDcR','XZtGIFM']
]
statueCodex=[
    'fnhaNrg',
    'vINYFL3',
    'rAbszDB',
    'cQOFnMr',
    'GFO8dSL',
    'CEo9YCx',
    'uNlFK4i',
    'x7lrvvy',
    'nZtxFeP',
    'UGt2QgY',
    '39LK2UQ',
    'KOTMkxd',
    'VSv3Raz',
    'RFRWPUM',
    'RS4uSiv',
    'nPFlHRn',
    'idYAn9C',
    '2tml7Cw',
    'V8wd6BS',
    'L8dbakA',
    '5RnVCxD',
    'lKe1Dwa',
    '1gJVPor',
    'c1e3Qc1',
    'fyRIUHP',
    'jGdYqDa',
    'VvvXBdK',
    'oDJSk5n'
]

def BreedLookup(breed):
    match breed:
        case 'Aberration':
            return 0
        case 'Aether':
            return 1
        case 'Auraboa':
            return 2
        case 'Banescale':
            return 3
        case 'Bogsneak':
            return 4
        case 'Coatl':
            return 5
        case 'Dusthide':
            return 6
        case 'Emperor':
            return 7
        case 'Everlux':
            return 8
        case 'Fae':
            return 9
        case 'Fathom':
            return 10
        case 'Gaoler':
            return 11
        case 'Guardian':
            return 12
        case 'Imperial':
            return 13
        case 'Mirror':
            return 14
        case 'Nocturne':
            return 15
        case 'Obelisk':
            return 16
        case 'Pearlcatcher':
            return 17
        case 'Ridgeback':
            return 18
        case 'Sandsurge':
            return 19
        case 'Skydancer':
            return 20
        case 'Snapper':
            return 21
        case 'Spiral':
            return 22
        case 'Tundra':
            return 23
        case 'Undertide':
            return 24
        case 'Veilspun':
            return 25
        case 'Wildclaw':
            return 26
        case _:
            return -1

def ElementLookup(element):
    match element:
        case 'Arcane':
            return 0
        case 'Earth':
            return 1
        case 'Ice':
            return 2
        case 'Fire':
            return 3
        case 'Light':
            return 4
        case 'Lightning':
            return 5
        case 'Nature':
            return 6
        case 'Plague':
            return 7
        case 'Shadow':
            return 8
        case 'Water':
            return 9
        case 'Wind':
            return 10
        case '---':
            return -3
        case 'Gold':
            return 11
        case 'Silver':
            return 12
        case 'Shade':
            return 13
        case _:
            return -1

def EmblemLookup(x,y):
    if x==-1 or y==-1:
        return '_______'
    elif x==7 and y==-3:
        return 'ji3UI0u'
    elif y==-3:
        return '_______'
    else:
        return emblemCodex[x][y]

def StatueLookup(statue):
    match statue:
        case 'Aberration':
            return 0
        case 'Aether F':
            return 1
        case 'Aether M':
            return 2
        case 'Auraboa':
            return 3
        case 'Banescale':
            return 4
        case 'Bogsneak F':
            return 5
        case 'Bogsneak M':
            return 6
        case 'Coatl F':
            return 7
        case 'Coatl M':
            return 8
        case 'Fae F':
            return 9
        case 'Fae M':
            return 10
        case 'Guardian F':
            return 11
        case 'Guardian M':
            return 12
        case 'Imperial F':
            return 13
        case 'Imperial M':
            return 14
        case 'Mirror':
            return 15
        case 'Obelisk':
            return 16
        case 'Ridgeback F':
            return 17
        case 'Ridgeback M':
            return 18
        case 'Sandsurge':
            return 19
        case 'Skydancer F':
            return 20
        case 'Skydancer M':
            return 21
        case 'Snapper':
            return 22
        case 'Spiral':
            return 23
        case 'Tundra F':
            return 24
        case 'Tundra M':
            return 25
        case 'Undertide F':
            return 26
        case 'Undertide M':
            return 27
        case _:
            return -1

#----------------root setup----------------

root = tk.Tk()
root.title('Flight Rising Bio Maker')
root.iconbitmap('./FRBM-icon.ico')
# set window dimensions and location
window_width = 1600
window_height = 840
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

#----------------frame setup----------------

# text entry frame
form = ttk.Frame(root, width=800, height=750, relief='solid', borderwidth=2)
form.pack(side='left', padx=20, pady=45, ipadx=10, ipady=10, fill='x', expand=False)
labelColumn = ttk.Label(form, anchor=tk.CENTER, font=('Verdana', 20, 'bold'), borderwidth=2, relief='solid', text="FR DRAGON BIO")
labelColumn.pack(fill='x', expand=False)
data = ttk.Frame(form, relief='solid', borderwidth=2)
data.pack(pady=20, fill='both', expand=True)

# text preview frame
preview = ttk.Frame(root, width=700, height=750, relief='solid', borderwidth=2)
preview.pack(side='right', padx=20, pady=45, ipadx=10, ipady=10, fill='x', expand=False)
name = ttk.Frame(preview, width=224, height=188)
name.pack(fill='x', expand=False)

for frame in [form, preview]:
    frame.pack_propagate(0)
    
#----------------widget setup----------------

#functions for text updates
def UpdateEmblem(event):
    x = BreedLookup(textBreed.get())
    y = ElementLookup(textElement.get())
    previewEmblem.config(text=f'https://i.imgur.com/{EmblemLookup(x,y)}.png')
    #previewEmblem.update()
def UpdateName():
    previewLetter.config(text=textName.get()[:1])
#    previewLetter.update()
    previewName.config(text=textName.get()[1:])
#    previewName.update()
def UpdateStatue(event):
    z = StatueLookup(textStatue.get())
    if z != -1:
        previewStatue.config(text=f'https://i.imgur.com/{statueCodex[z]}.png')
    #previewStatue.update()
def UpdateBio():
    previewQuote.config(text=entryQuote.get('1.0','end'))
#    previewLetter.update()
    previewBio.config(text=entryBio.get('1.0','end'))
#    previewName.update()
def SaveToClipboard():
    copy = tk.Tk()
    copy.withdraw()
    copy.clipboard_clear()
    outputVars={
        'emblem':previewEmblem.cget('text'), 'letter':previewLetter.cget('text'),
        'name':previewName.cget('text'), 'subtitle':previewSubtitle.cget('text'),
        'quote':previewQuote.cget('text').rstrip(), 'author':previewAuthor.cget('text'),
        'statue':previewStatue.cget('text'), 'bio':previewBio.cget('text').rstrip(),
        'location':previewLocation.cget('text'),
        'hoard1':previewHoard1.cget('text'), 'hoard2':previewHoard2.cget('text'),
        'hoard3':previewHoard3.cget('text'), 'hoard4':previewHoard4.cget('text')
    }
    output='''[columns]
[columns]
[center][url=http://www1.flightrising.com/forums/cc/2118304][img]{emblem}[/img][/url][/center]
[nextcol]



[font=Century Gothic]
[size=5][i]❧[/i] [b]{letter}[/b]{name}[/size]
[indent][size=4][i]{subtitle}[/i][/size][/indent]
[/columns]

[font=Century Gothic]
[b]Bio[/b]
-----
[columns]
[url=http://www1.flightrising.com/forums/cc/2118304][img]{statue}[/img][/url]
[nextcol]
[center][i]"{quote}"[/i][/center]
[right]- [url=http://flightrising.com]{author}[/right][/columns]
[center][size=1][size=1]▬▬▬▬▬▬▬▬▬[/size][/size][/center]
[font=Century Gothic]
{bio}
[font=Century Gothic]
[b]Location[/b]
-----
[columns][url=http://www1.flightrising.com/wiki/world-map][img]http://www1.flightrising.com/static/map/icons/wind_2.png[/img][/url]
[nextcol]


[size=5][color=#731D08][b]{location}[/b][/color][/size][/columns]
[font=Century Gothic]
[b]Hoard[/b]
-----
[center][item={hoard1}][item={hoard2}][item={hoard3}][item={hoard4}][/center]


[right][size=1]Bio template created by [url=http://bio-and-resource-codes-fr.tumblr.com/post/149743872226/abyssalrising-abyssalrising-free-to-use-bio]AbyssalRising[/url]
Bio template modified by [url=http://flightrising.com/main.php?p=lair&tab=userpage&id=278363]kirauriel[/url][/size][/right]
[nextcol]
[color=#FF4C26]|
|
|[/color]
[color=#FD9248]|
|
|[/color]
[color=#FEFE54]|
|
|[/color]
[color=#90FF54]|
|
|[/color]
[color=#54CDFE]|
|
|[/color]
[color=#C956FF]|
|
|[/color]
[color=#FF56F5]|
|
|[/color]
[color=#FF4C26]|
|
|[/color]
[color=#FD9248]|
|
|[/color]
[color=#FEFE54]|
|
|[/color]
[color=#90FF54]|
|
|[/color]
[color=#54CDFE]|
|
|[/color]
[color=#C956FF]|
|
|[/color]
[color=#FF56F5]|
|
|[/color]
[color=#FF4C26]|
|
|[/color]
[color=#FD9248]|
|
|[/color]
[color=#FEFE54]|
|
|[/color]
[color=#90FF54]|
|
|[/color]
[color=#54CDFE]|
|
|[/color]
[color=#C956FF]|
|
|[/color]
[color=#FF56F5]|
|
|[/color]'''.format(**outputVars)
    copy.clipboard_append(output)
    copy.update()
    copy.destroy()

# widgets for text entry frame
sectionTop = ttk.Frame(data)
sectionTop.pack(fill='none', expand=False)

frameName = ttk.Frame(sectionTop)
frameName.grid(column=0, row=0, sticky=tk.NW, padx=10, pady=20)
labelName = ttk.Label(frameName, text="Dragon Name")
labelName.pack(fill='x', expand=False)
textName = tk.StringVar()
textName.set('Acrid')
entryName = ttk.Entry(frameName, width=25, textvariable=textName)
entryName.pack(fill='x', expand=False)
buttonName = ttk.Button(frameName, text="Update", command=UpdateName)
buttonName.pack(anchor='e', fill='none', expand=False)

frameSubtitle = ttk.Frame(sectionTop)
frameSubtitle.grid(column=1, row=0, sticky=tk.N, padx=10, pady=20)
labelSubtitle = ttk.Label(frameSubtitle, text="Subtitle")
labelSubtitle.pack(fill='x', expand=False)
textSubtitle = tk.StringVar()
textSubtitle.set('the Test Dragon')
entrySubtitle = ttk.Entry(frameSubtitle, width=40, textvariable=textSubtitle)
entrySubtitle.pack(fill='x', expand=False)

frameLocation = ttk.Frame(sectionTop)
frameLocation.grid(column=2, row=0, sticky=tk.NE, padx=10, pady=20)
labelLocation = ttk.Label(frameLocation, text="Location")
labelLocation.pack(fill='x', expand=False)
textLocation = tk.StringVar()
textLocation.set('Wandering Sornieth')
entryLocation = ttk.Entry(frameLocation, width=50, textvariable=textLocation)
entryLocation.pack(fill='x', expand=False)


labelQuote = ttk.Label(data, text="Quote")
labelQuote.pack(fill='x', expand=False)
entryQuote = tk.Text(data, height=4)
entryQuote.pack(fill='x', expand=False)
entryQuote.insert('1.0', 'And yet, it was. Something was there despite nothing being there. Form gave way to formless. Sharpness became sharper in intagibility. Life left something behind to be born from the nothing.')
labelAuthor = ttk.Label(data, text="Author")
labelAuthor.pack(anchor='e', fill='none', expand=False)
textAuthor = tk.StringVar()
textAuthor.set('Vestige')
entryAuthor = ttk.Entry(data, width=20, textvariable=textAuthor)
entryAuthor.pack(anchor='e', fill='none', expand=False)
labelBio = ttk.Label(data, text="Bio")
labelBio.pack(fill='x', expand=False)
entryBio = ScrolledText(data, height=12)
entryBio.pack(fill='x', expand=False)
entryBio.insert('1.0', 'a big blank void stares back at you')
buttonBio = ttk.Button(data, text="Update", command=UpdateBio)
buttonBio.pack(anchor='e', fill='none', expand=False)


sectionHoard = ttk.Frame(data)
sectionHoard.pack(pady=20, fill='none', expand=False)

labelHoard1 = ttk.Label(sectionHoard, text="Hoard Item 1")
labelHoard1.grid(column=0, row=0)
textHoard1 = tk.StringVar()
textHoard1.set('Boolean')
entryHoard1 = ttk.Entry(sectionHoard, width=25, textvariable=textHoard1)
entryHoard1.grid(column=0, row=1,padx=10)

labelHoard2 = ttk.Label(sectionHoard, text="Hoard Item 2")
labelHoard2.grid(column=1, row=0)
textHoard2 = tk.StringVar()
textHoard2.set('Plague Sprite')
entryHoard2 = ttk.Entry(sectionHoard, width=25, textvariable=textHoard2)
entryHoard2.grid(column=1, row=1,padx=10)

labelHoard3 = ttk.Label(sectionHoard, text="Hoard Item 3")
labelHoard3.grid(column=2, row=0)
textHoard3 = tk.StringVar()
textHoard3.set('Blight Nymph')
entryHoard3 = ttk.Entry(sectionHoard, width=25, textvariable=textHoard3)
entryHoard3.grid(column=2, row=1, padx=10)

labelHoard4 = ttk.Label(sectionHoard, text="Hoard Item 4")
labelHoard4.grid(column=3, row=0)
textHoard4 = tk.StringVar()
textHoard4.set('Enduring Goblin')
entryHoard4 = ttk.Entry(sectionHoard, width=25, textvariable=textHoard4)
entryHoard4.grid(column=3, row=1, padx=10)


sectionBot = ttk.Frame(data)
sectionBot.pack(fill='none', expand=False)

labelBreed = ttk.Label(sectionBot, text="Breed")
labelBreed.grid(column=0, row=0, pady=5)
textBreed = tk.StringVar()
optionBreed = ttk.Combobox(sectionBot, textvariable=textBreed)
optionBreed['values']=(
    'Aberration',
    'Aether',
    'Auraboa',
    'Banescale',
    'Bogsneak',
    'Coatl',
    'Dusthide',
    'Emperor',
    'Everlux',
    'Fae',
    'Fathom',
    'Gaoler',
    'Guardian',
    'Imperial',
    'Mirror',
    'Nocturne',
    'Obelisk',
    'Pearlcatcher',
    'Ridgeback',
    'Sandsurge',
    'Skydancer',
    'Snapper',
    'Spiral',
    'Tundra',
    'Undertide',
    'Veilspun',
    'Wildclaw'
)
optionBreed['state'] = 'readonly'
optionBreed.config(width=15)
optionBreed.set('Mirror')
optionBreed.grid(column=0, row=1, padx=25)

labelElement = ttk.Label(sectionBot, text="Element")
labelElement.grid(column=1, row=0, pady=5)
textElement = tk.StringVar()
optionElement = ttk.Combobox(sectionBot, textvariable=textElement)
optionElement['values']=(
    'Arcane',
    'Earth',
    'Ice',
    'Fire',
    'Light',
    'Lightning',
    'Nature',
    'Plague',
    'Shadow',
    'Water',
    'Wind',
    '---',
    'Gold',
    'Silver',
    'Shade'
)
optionElement['state'] = 'readonly'
optionElement.config(width=15)
optionElement.set('Nature')
optionElement.grid(column=1, row=1, padx=25)

labelStatue = ttk.Label(sectionBot, text="Statue")
labelStatue.grid(column=2, row=0, pady=5)
textStatue = tk.StringVar()
optionStatue = ttk.Combobox(sectionBot, textvariable=textStatue)
optionStatue['values']=(
    'Aberration',
    'Aether F',
    'Aether M',
    'Auraboa',
    'Banescale',
    'Bogsneak F',
    'Bogsneak M',
    'Coatl F',
    'Coatl M',
    'Fae F',
    'Fae M',
    'Guardian F',
    'Guardian M',
    'Imperial F',
    'Imperial M',
    'Mirror',
    'Obelisk',
    'Ridgeback F',
    'Ridgeback M',
    'Sandsurge',
    'Skydancer F',
    'Skydancer M',
    'Snapper',
    'Spiral',
    'Tundra F',
    'Tundra M',
    'Undertide F',
    'Undertide M'
)
optionStatue['state'] = 'readonly'
optionStatue.config(width=15)
optionStatue.set('Mirror')
optionStatue.grid(column=2, row=1, padx=25)

buttonSave = ttk.Button(data, text="Save to Clipboard", command=SaveToClipboard)
buttonSave.pack(anchor='s', pady=20, fill='none', expand=False)

#widgets for text preview frame
x = BreedLookup(textBreed.get())
y = ElementLookup(textElement.get())
previewEmblem = ttk.Label(name, font=('Verdana', 8), text=f'https://i.imgur.com/{EmblemLookup(x,y)}.png')
previewEmblem.pack(side='left', fill='x', expand=False)
optionBreed.bind('<<ComboboxSelected>>', UpdateEmblem)
optionElement.bind('<<ComboboxSelected>>', UpdateEmblem)

previewLeaf = ttk.Label(name, font=('Century Gothic', 15, 'italic'), text="❧")
previewLeaf.pack(side='left', fill='x', expand=False)
previewLetter = ttk.Label(name, font=('Century Gothic', 15, 'bold'), padding=-2, text=textName.get()[:1])
previewLetter.pack(side='left', fill='x', expand=False)
previewName = ttk.Label(name, font=('Century Gothic', 15), text=textName.get()[1:])
previewName.pack(fill='x', expand=False)

previewSubtitle = ttk.Label(preview, font=('Century Gothic', 10, 'italic'), textvariable=textSubtitle)
previewSubtitle.pack(anchor='center', fill='none', expand=False)

secBio = ttk.Label(preview, font=('Century Gothic', 10, 'bold'), text="Bio")
secBio.pack(anchor='w', fill='none', expand=False)
sepBio = ttk.Separator(preview, orient='horizontal')
sepBio.pack(fill='x')

previewQuote = ttk.Label(preview, wraplength=680, font=('Verdana', 10, 'italic'), text=entryQuote.get('1.0','end'))
previewQuote.pack(fill='x', expand=False)
previewAuthor = ttk.Label(preview, wraplength=150, font=('Verdana', 10), textvariable=textAuthor)
previewAuthor.pack(anchor='e',fill='none', expand=False)
sepBio = ttk.Separator(preview, orient='horizontal')
sepBio.pack(fill='x')
previewStatue = ttk.Label(preview, font=('Verdana', 8), text='https://i.imgur.com/_______.png')
previewStatue.pack(anchor='w', fill='none', expand=False)
z = StatueLookup(textStatue.get())
if z != -1:
    previewStatue.config(text=f'https://i.imgur.com/{statueCodex[z]}.png')
optionStatue.bind('<<ComboboxSelected>>', UpdateStatue)
previewBio = ttk.Label(preview, wraplength=680, font=('Century Gothic', 10), text=entryBio.get('1.0','end'))
previewBio.pack(fill='x', expand=False)

secLocation = ttk.Label(preview, font=('Century Gothic', 10, 'bold'), text="Location")
secLocation.pack(anchor='w', fill='none', expand=False)
sepLocation = ttk.Separator(preview, orient='horizontal')
sepLocation.pack(fill='x')

previewLocation = ttk.Label(preview, wraplength=680, font=('Verdana', 18, 'bold'), textvariable=textLocation)
previewLocation.pack(anchor='center', pady=20, fill='none', expand=False)

secHoard = ttk.Label(preview, font=('Century Gothic', 10, 'bold'), text="Hoard")
secHoard.pack(anchor='w', fill='none', expand=False)
sepHoard = ttk.Separator(preview, orient='horizontal')
sepHoard.pack(fill='x')

sectionFooter = ttk.Frame(preview, relief='solid', borderwidth=2)
sectionFooter.pack(anchor='center', fill='x', expand=False)
sectionFooter.columnconfigure(0, weight=1)
sectionFooter.columnconfigure(1, weight=1)
sectionFooter.columnconfigure(2, weight=1)
sectionFooter.columnconfigure(3, weight=1)

previewHoard1 = ttk.Label(sectionFooter, wraplength=150, justify=tk.CENTER, font=('Verdana', 12, 'bold'), textvariable=textHoard1)
previewHoard1.grid(column=0, row=0, padx=10)
previewHoard2 = ttk.Label(sectionFooter, wraplength=150, justify=tk.CENTER, font=('Verdana', 12, 'bold'), textvariable=textHoard2)
previewHoard2.grid(column=1, row=0, padx=10)
previewHoard3 = ttk.Label(sectionFooter, wraplength=150, justify=tk.CENTER, font=('Verdana', 12, 'bold'), textvariable=textHoard3)
previewHoard3.grid(column=2, row=0, padx=10)
previewHoard4 = ttk.Label(sectionFooter, wraplength=150, justify=tk.CENTER, font=('Verdana', 12, 'bold'), textvariable=textHoard4)
previewHoard4.grid(column=3, row=0, padx=10)

#----------------mainloop----------------
root.mainloop()