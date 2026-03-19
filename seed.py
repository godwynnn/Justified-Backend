import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

from api.models import Sermon, Event, Leader

def seed():
    Sermon.objects.all().delete()
    
    sermons = [
        {"title": "Walking in Faith", "speaker": "Pastor John Doe", "date": "2026-03-10", "scripture": "Hebrews 11:1", "notes_url": "https://images.unsplash.com/photo-1490730141103-6cac27aaab94?q=80&w=2940&auto=format&fit=crop"},
        {"title": "The Power of Prayer", "speaker": "Pastor John Doe", "date": "2026-03-03", "scripture": "James 5:16", "notes_url": "https://images.unsplash.com/photo-1445445290350-18a3b86e0b5b?q=80&w=2831&auto=format&fit=crop"},
        {"title": "Faith Over Fear", "speaker": "Pastor Jane Smith", "date": "2026-02-24", "scripture": "Isaiah 41:10", "notes_url": "https://images.unsplash.com/photo-1507692049790-de58290a4334?q=80&w=2940&auto=format&fit=crop"},
        {"title": "Grace Abounding", "speaker": "Pastor John Doe", "date": "2026-02-17", "scripture": "Romans 5:20", "notes_url": "https://images.unsplash.com/photo-1428366890462-dd4baecf492b?q=80&w=2832&auto=format&fit=crop"},
        {"title": "Light of the World", "speaker": "Pastor Jane Smith", "date": "2026-02-10", "scripture": "Matthew 5:14", "notes_url": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?q=80&w=2940&auto=format&fit=crop"},
        {"title": "Strength in Weakness", "speaker": "Pastor John Doe", "date": "2026-02-03", "scripture": "2 Corinthians 12:9", "notes_url": "https://images.unsplash.com/photo-1499591934245-40b55745b905?q=80&w=2942&auto=format&fit=crop"},
    ]
    
    for s in sermons:
        Sermon.objects.create(**s)
        
    print("Database seeded with sermons successfully.")

if __name__ == '__main__':
    seed()
