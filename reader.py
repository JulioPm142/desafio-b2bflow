from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def Buscar_usuarios():
    try:
        res = supabase.table("Users").select("Number","Name").execute()
        print("connection successful! Sample data:", res.data)
        return res.data

    except Exception as e:
        print("connection failed", e)
        return None
