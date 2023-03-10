import pandas as pd
import matplotlib.pyplot as plt
import numpy
# Carica il file CSV in un DataFrame di Pandas
df = pd.read_csv(r'D:\Leonardo\VQG_final\loss_function graph\loss_valuesVQG_1_Final_gredy_search.csv')

# Estrae i valori numerici dalle stringhe delle colonne 'Epoch' e 'Loss'
df['Epoch'] = df['Epoch'].str.extract('(\d+)')
df['Loss'] = df['Loss'].str.extract('(\d+\.\d+)').astype(float)





plt.plot(df["Epoch"].astype(str), df['Loss'])


#plt.plot(lista_epochs.astype(str), lista_loss)

# Aggiunge un titolo e delle etichette agli assi
plt.title('Loss per Epoch')
plt.xlabel('epoch')
plt.ylabel('Loss')

# Mostra il grafico
plt.savefig('loss_vqg_coco.png')
