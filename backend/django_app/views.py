# views.py
import pandas as pd
from django.http import HttpResponse

def get_te(request):
    # Load data from CSV file
    nom_fichier = 'transport.csv'
    df = pd.read_csv(nom_fichier)

    # Demande à l'utilisateur d'entrer une phrase
    phrase_utilisateur = input("Entrez une phrase : ")

    # Filter data based on user input
    resultats_filtrés = df[df.iloc[:, 0].str.lower() == phrase_utilisateur.lower()]

    # Prepare HTML content for the response
    if not resultats_filtrés.empty:
        # Get the value from the second column for the first matched row
        result_value = resultats_filtrés.iloc[0, 1]
        html_content = f"<p>Résultat trouvé : {result_value}</p>"
    else:
        html_content = "<p>Aucun résultat trouvé.</p>"

    # Return HTML response
    return HttpResponse(html_content)
