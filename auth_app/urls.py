from django.contrib import admin
from django.urls import path, include
from .views import inscription,connexion,deconnexion,profile,liste_utilisateurs,accueil

app_name = 'auth_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', inscription, name="inscription"),
    path('connexion/', connexion, name="connexion"),
    path('deconnexion/', deconnexion ,name="deconnexion" ),
    path('profile/', profile ,name="profile" ),
    path('liste_utilisateurs/', liste_utilisateurs ,name="liste_utilisateurs" ),
    path('accueil',accueil,name="accueil")
]