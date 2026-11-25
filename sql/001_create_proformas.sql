CREATE TABLE IF NOT EXISTS proformas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    fournisseur TEXT NOT NULL,
    date_emission DATE NOT NULL,
    montant_total NUMERIC(20,2) NOT NULL CHECK (montant_total > 0),
    devise TEXT NOT NULL CHECK (devise IN ('EUR','USD','XAF'))
);

