from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

PROFORMA_VALIDE = {"fournisseur":"fourn1", "date_emission":"2026-01-01", "montant_total":1000, "devise":"EUR"}


def test_post_id_ignore():
    post_rep = client.post("/proformas", json={**PROFORMA_VALIDE, "id":999})
    assert post_rep.status_code == 201
    assert post_rep.json()["id"] != 999


def test_post_puis_get_retrouve_la_proforma():
    # 1. créer la proforma
    post_response = client.post("/proformas", json=PROFORMA_VALIDE)
    assert post_response.status_code == 201

    # 2. récupérer l'id renvoyé par l'API
    nouvel_id = post_response.json()["id"]

    # 3. relire la proforma avec cet id
    get_response = client.get(f"/proformas/{nouvel_id}")
    assert get_response.status_code == 200

    # 4. vérifier qu'on retrouve ce qu'on a envoyé
    assert get_response.json()["fournisseur"] == PROFORMA_VALIDE["fournisseur"]
    assert get_response.json()["montant_total"] == PROFORMA_VALIDE["montant_total"]

def test_post_valide_renvoie_201_avec_id():
    
    from app.main import cpt_id
    
    good_response = client.post(
            "/proformas",
            json={**PROFORMA_VALIDE})
    
    assert good_response.status_code == 201
    assert isinstance(good_response.json()["id"], int)
    assert good_response.json()["id"] == cpt_id + 1


def test_post_montant_negatif_renvoie_422():

    negative_response = client.post(
        "/proformas",
        json={**PROFORMA_VALIDE, "montant_total":-1000,})
    
    assert negative_response.status_code == 422

def test_post_devise_invalide_renvoie_422():    
    badDevise_response = client.post(
        "/proformas",
        json={**PROFORMA_VALIDE, "devise":"GBP"})
    
    assert badDevise_response.status_code == 422


def test_get_proforma1():
    response = client.get("/proformas/1")
    assert response.status_code == 200
    
    
def test_get_proforma999():
    response = client.get("/proformas/999")
    assert response.status_code == 404