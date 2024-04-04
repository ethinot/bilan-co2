# views.py
import pandas as pd
from django.http import HttpResponse

def get_te(_):
    # Load data from CSV file
    nom_fichier = 'transport.csv'
    df = pd.read_csv(nom_fichier)

    # Demande à l'utilisateur d'entrer une phrase
    phrase_utilisateur = input("Entrez une phrase : ")
    phrase_utilisateur2=input("traget:")
    # Filter data based on user input
    resultats_filtrés = df[df.iloc[:, 0].str.lower() == phrase_utilisateur.lower()]

    # Prepare HTML content for the response
    if not resultats_filtrés.empty:
        # Get the value from the second column for the first matched row
        result_value = float(resultats_filtrés.iloc[0, 1])
        i=int(phrase_utilisateur2)
        print(i)
        total_result = result_value * i
        print (total_result)
        html_content = f"<p>Résultat trouvé : {result_value}</p><p>total : {total_result}</p>"

    else:
        html_content = "<p>Aucun résultat trouvé.</p>"

    # Return HTML response
    return HttpResponse(html_content)
