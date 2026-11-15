from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
from datetime import date

Devise = Literal["EUR", "USD", "XAF"]

cpt_id = 2

class ProformaCreate(BaseModel):
    fournisseur: str
    date_emission: date
    montant_total: float = Field(gt=0, description="Montant nul ou negatif")
    devise: Devise
    
class Proforma(ProformaCreate):
    id: int


liste_proformas = [Proforma(fournisseur="fourn1", date_emission="2026-01-01", montant_total=1000, devise="EUR", id=1),
                   Proforma(fournisseur="fourn2", date_emission="2026-02-01", montant_total=2000, devise="EUR", id=2)]

app = FastAPI()

@app.get("/health")
async def get_status():
    return {"status": "ok"}

@app.get("/proformas")
async def get_proformas():
    return liste_proformas

@app.post("/proformas", status_code=201)
async def post_proformas(proforma: ProformaCreate):

    global cpt_id

    cpt_id+=1
    
    new_prof = Proforma(**proforma.model_dump(), id=cpt_id)
    
    
    liste_proformas.append(new_prof)
    
    return new_prof
    

@app.get("/proformas/{id}")
async def get_proformas_id(id: int):
    for proforma in liste_proformas:
        if proforma.id == id:
            return proforma
    
    raise HTTPException(status_code=404,detail="id inexistant")


