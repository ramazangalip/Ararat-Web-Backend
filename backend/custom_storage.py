from django.core.files.storage import Storage
from supabase import create_client
from django.conf import settings
import mimetypes

class SupabaseStorage(Storage):
    def __init__(self):
        # Ayarlardaki URL ve Key ile Supabase bağlantısını kurar
        self.client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    def _save(self, name, content):
        # Dosya tipini (jpg, png vb.) belirle
        content_type, _ = mimetypes.guess_type(name)
        if not content_type:
            content_type = 'application/octet-stream'

        file_data = content.read()
        
        # Supabase Bucket'a yükle
        self.client.storage.from_(settings.SUPABASE_BUCKET_NAME).upload(
            path=name,
            file=file_data,
            file_options={"content-type": content_type}
        )
        return name

    def url(self, name):
        # Resmin internetten erişilecek tam adresini döndürür
        return f"{settings.SUPABASE_URL}/storage/v1/object/public/{settings.SUPABASE_BUCKET_NAME}/{name}"

    def exists(self, name):
        return False