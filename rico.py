import pandas as pd

datatrain = pd.read_excel('TrainsetTugas1ML.xlsx')
datatest = pd.read_excel('TestsetTugas1ML.xlsx')
trainrow = datatrain.shape[0]
testrow = datatest.shape[0]

def perulangan(kolom1, kategori1, kolom2, kategori2):
    i = 0
    for j in range(trainrow):
        if (datatrain[kolom1][j] == kategori1) & (datatrain[kolom2][j] == kategori2):
            i += 1
    return i

def rumus(kolom1, kategori1, kolom2, kategori2, tipeincome):
    hasil = perulangan(kolom1, kategori1, kolom2, kategori2)/tipeincome
    return hasil

moreincome = 0
lessincome = 0
for i in range(trainrow):
    if(datatrain['income'][i]=='>50K'):
        moreincome += 1
    else:
        lessincome += 1

peluangMore = moreincome/trainrow
peluangLess = lessincome/trainrow

output=[]
for j in range(testrow):
    PelAge_more = rumus('age', datatest['age'][j], 'income', '>50K', moreincome)
    PelAge_less = rumus('age', datatest['age'][j], 'income', '<=50K', lessincome)
    
    Pelworkclass_more = rumus('workclass', datatest['workclass'][j], 'income', '>50K', moreincome)
    Pelworkclass_less = rumus('workclass', datatest['workclass'][j], 'income', '<=50K', lessincome)
    
    PelEdu_more = rumus('education', datatest['education'][j], 'income', '>50K', moreincome)
    PelEdu_less = rumus('education', datatest['education'][j], 'income', '<=50K', lessincome)
    
    Pelmstatus_more = rumus('marital-status', datatest['marital-status'][j], 'income', '>50K', moreincome)
    Pelmstatus_less = rumus('marital-status', datatest['marital-status'][j], 'income', '<=50K', lessincome)
    
    Pelocc_more = rumus('occupation', datatest['occupation'][j], 'income', '>50K', moreincome)
    Pelocc_less = rumus('occupation', datatest['occupation'][j], 'income', '<=50K', lessincome)
    
    Pelrelationship_more = rumus('relationship', datatest['relationship'][j], 'income', '>50K', moreincome)
    Pelrelationship_less = rumus('relationship', datatest['relationship'][j], 'income', '<=50K', lessincome)
    
    Pelhours_more = rumus('hours-per-week', datatest['hours-per-week'][j], 'income', '>50K', moreincome)
    Pelhours_less = rumus('hours-per-week', datatest['hours-per-week'][j], 'income', '<=50K', lessincome)
    
    PelMore = PelAge_more*Pelworkclass_more*PelEdu_more*Pelmstatus_more*Pelocc_more*Pelrelationship_more*Pelhours_more*peluangMore
    PelLess = PelAge_less*Pelworkclass_less*PelEdu_less*Pelmstatus_less*Pelocc_less*Pelrelationship_less*Pelhours_less*peluangLess
    
    if(PelMore > PelLess):
        output.append('>50K')
    else:
        output.append('<=50K')

print(output)
final = pd.DataFrame({'income': output}, index=datatest['id'])
final.to_excel("final.xlsx")
          
