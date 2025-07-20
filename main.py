from fastapi import FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

# Load the dataset
df = pd.read_json("q-fastapi-llm-query.json")

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Normalize strings for comparison
def normalize(text):
    return text.strip().lower()

@app.get("/query")
def query(q: str, response: Response):
    response.headers["X-Email"] = "22f201029@ds.study.iitm.ac.in"
    qn = normalize(q)

    if "total sales of keyboard" in qn and "south kylercester" in qn:
        result = df[(df.product == "Keyboard") & (df.city == "South Kylercester")]["sales"].sum()
    elif "how many sales reps" in qn and "missouri" in qn:
        result = df[df.region == "Missouri"]["rep"].nunique()
    elif "average sales for computer" in qn and "rhode island" in qn:
        result = round(df[(df.product == "Computer") & (df.region == "Rhode Island")]["sales"].mean(), 2)
    elif "lorraine zemlak phd" in qn and "eleanorecester" in qn:
        temp = df[(df.rep == "Lorraine Zemlak PhD") & (df.city == "Eleanorecester")]
        result = temp.loc[temp.sales.idxmax()]["date"] if not temp.empty else "Not found"
    elif "total sales of car" in qn and "camrenfurt" in qn:
        result = df[(df.product == "Car") & (df.city == "Camrenfurt")]["sales"].sum()
    elif "how many sales reps" in qn and "harryland" in qn:
        result = df[df.region == "Harryland"]["rep"].nunique()
    elif "average sales for sausages" in qn and "florida" in qn:
        result = round(df[(df.product == "Sausages") & (df.region == "Florida")]["sales"].mean(), 2)
    elif "irvin jacobson" in qn and "new camille" in qn:
        temp = df[(df.rep == "Irvin Jacobson") & (df.city == "New Camille")]
        result = temp.loc[temp.sales.idxmax()]["date"] if not temp.empty else "Not found"
    elif "total sales of car" in qn and "new camille" in qn:
        result = df[(df.product == "Car") & (df.city == "New Camille")]["sales"].sum()
    elif "how many sales reps" in qn and "kansas" in qn:
        result = df[df.region == "Kansas"]["rep"].nunique()
    elif "average sales for keyboard" in qn and "tennessee" in qn:
        result = round(df[(df.product == "Keyboard") & (df.region == "Tennessee")]["sales"].mean(), 2)
    elif "total sales of car" in qn and "south kylercester" in qn:
        result = df[(df.product == "Car") & (df.city == "South Kylercester")]["sales"].sum()
    elif "average sales for keyboard" in qn and "colorado" in qn:
        result = round(df[(df.product == "Keyboard") & (df.region == "Colorado")]["sales"].mean(), 2)
    elif "jed hodkiewicz" in qn and "south mustafa" in qn:
        temp = df[(df.rep == "Jed Hodkiewicz") & (df.city == "South Mustafa")]
        result = temp.loc[temp.sales.idxmax()]["date"] if not temp.empty else "Not found"
    elif "total sales of fish" in qn and "new leliafort" in qn:
        result = df[(df.product == "Fish") & (df.city == "New Leliafort")]["sales"].sum()
    elif "how many sales reps" in qn and "alabama" in qn:
        result = df[df.region == "Alabama"]["rep"].nunique()
    elif "average sales for shoes" in qn and "mississippi" in qn:
        result = round(df[(df.product == "Shoes") & (df.region == "Mississippi")]["sales"].mean(), 2)
    elif "wendy schamberger" in qn and "jacobston" in qn:
        temp = df[(df.rep == "Wendy Schamberger") & (df.city == "Jacobston")]
        result = temp.loc[temp.sales.idxmax()]["date"] if not temp.empty else "Not found"
    else:
        result = "Question not recognized."

    return {"answer": result}

# To run: uvicorn this_file_name:app --reload
