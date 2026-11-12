from contabilidad import supabase
try:
    print("🪣 Buckets disponibles en Supabase Storage:")
    buckets = supabase.storage.list_buckets()
    for b in buckets:
        print(f" - {b.name}")
except Exception as e:
    print(f"❌ Error al listar buckets: {e}")
