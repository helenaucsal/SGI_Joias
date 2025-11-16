from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Produto

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"mensagem": "API funcionando com SQLite 🚀"}


@app.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()


@app.post("/produtos")
def cadastrar_produto(nome: str, preco: float, db: Session = Depends(get_db)):
    novo = Produto(nome=nome, preco=preco)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
