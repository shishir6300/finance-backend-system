from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Backend System")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Finance Backend</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
            }

            .container {
                text-align: center;
                padding: 60px 20px;
            }

            h1 {
                font-size: 3rem;
                margin-bottom: 10px;
                animation: fadeIn 1.5s ease-in-out;
            }

            p {
                font-size: 1.2rem;
                opacity: 0.85;
            }

            .card {
                backdrop-filter: blur(15px);
                background: rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 30px;
                margin: 30px auto;
                width: 80%;
                max-width: 600px;
                box-shadow: 0 8px 30px rgba(0,0,0,0.3);
                animation: slideUp 1s ease-in-out;
            }

            .btn {
                display: inline-block;
                margin: 10px;
                padding: 12px 25px;
                border-radius: 30px;
                background: linear-gradient(45deg, #00c6ff, #0072ff);
                color: white;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
            }

            .btn:hover {
                transform: scale(1.05);
                background: linear-gradient(45deg, #0072ff, #00c6ff);
            }

            ul {
                list-style: none;
                padding: 0;
                text-align: left;
            }

            li {
                padding: 10px;
                border-bottom: 1px solid rgba(255,255,255,0.2);
            }

            .footer {
                margin-top: 40px;
                font-size: 14px;
                opacity: 0.7;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }

            @keyframes slideUp {
                from { opacity: 0; transform: translateY(40px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>💰 Finance Backend System</h1>
            <p>Smart Financial Tracking API built with FastAPI</p>

            <div class="card">
                <h2>🚀 Quick Access</h2>
                <a href="/docs" class="btn">📄 API Docs</a>
                <a href="/records/" class="btn">📊 Records</a>
                <a href="/summary/" class="btn">📈 Summary</a>
            </div>

            <div class="card">
                <h2>⚡ API Endpoints</h2>
                <ul>
                    <li><strong>POST</strong> /users/ → Create User</li>
                    <li><strong>POST</strong> /records/ → Create Record</li>
                    <li><strong>GET</strong> /records/ → Get Records</li>
                    <li><strong>PUT</strong> /records/{id} → Update Record</li>
                    <li><strong>DELETE</strong> /records/{id} → Delete Record</li>
                    <li><strong>GET</strong> /summary/ → Financial Summary</li>
                </ul>
            </div>

            <div class="footer">
                🚀 Built by Shishir | FastAPI Backend Project
            </div>
        </div>
    </body>
    </html>
    """

# ---------------- USER ----------------
@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# ---------------- RECORDS ----------------
@app.post("/records/", response_model=schemas.RecordOut)
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    if record.type not in ["income", "expense"]:
        raise HTTPException(status_code=400, detail="Type must be 'income' or 'expense'")
    
    if record.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    return crud.create_record(db, record)

@app.get("/records/", response_model=list[schemas.RecordOut])
def get_records(type: str = None, category: str = None, db: Session = Depends(get_db)):
    filters = {"type": type, "category": category}
    return crud.get_records(db, filters)

@app.put("/records/{record_id}", response_model=schemas.RecordOut)
def update_record(record_id: int, data: schemas.RecordUpdate, db: Session = Depends(get_db)):
    record = crud.update_record(db, record_id, data)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

@app.delete("/records/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
    record = crud.delete_record(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"message": "Deleted successfully"}

@app.get("/summary/")
def get_summary(db: Session = Depends(get_db)):
    return crud.get_summary(db)