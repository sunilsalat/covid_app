

def slugify_slug(slug):
    new_slug = slug.split()
    a = ''
    for i in new_slug:
        if i == (new_slug[-1]):
            a = a + str(i)
        else:
            a = a + str(i) + '_'
    return a

# covid html code below
'''

 file = ('WHO-COVID-19-global-data_india.csv')
    with open(file) as f:
        content = csv.reader(f)

        deaths, cases, dates = [], [], []
        for index,row in enumerate(content):
            try:
                death = int(row[6])
                case = int(row[4])
                date = datetime.strptime(row[0], '%d-%m-%Y')
            except:
                print(f'missing data {index}')
            else:
                deaths.append(death)
                cases.append(case)
                dates.append(date)


    data = {
        'type':'bar',
        'x':dates,
        'y':cases,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6
    }

    my_layout={
        'title':'Daily Cases In India',
        'xaxis':{'title':'date'},
        'yaxis':{'title':'Number of cases'}
    }

    fig={'data':data, 'layout':my_layout}
    offline.plot(fig, filename='corona.html')

'''

