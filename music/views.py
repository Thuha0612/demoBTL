from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.http import HttpResponse
from . models import Music, Vocab

# Create your views here.
def main(request):
    music = Music.objects.all().order_by('title')
    music_list = list(Music.objects.all().order_by('title').values())
    return render(request, 'main.html', {'musics': music, 'music_list': music_list})

def index(request):
    music = Music.objects.all().order_by('title')
    music_list = list(Music.objects.all().order_by('title').values())
    return render(request, 'home.html', {'musics': music, 'music_list': music_list})

def add(request):
    if(request.method == "POST"):
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        audio = request.FILES.get('audio_file')
        image = request.FILES.get('cover_image')
        lyric = request.POST.get('lyrics')
        vocab = request.POST.get('vocabulary')
        # Vocab = request.POST.get('vocab')
        
        data = Music.objects.create(
            title=title, artist=artist, audio_file=audio, cover_image=image, lyrics=lyric, vocabulary=vocab
            # , Vocab = Vocab
        )
        data.save()
        return redirect('music:home')
    return render(request, 'add.html')
def vocabulary(request):
    vocab=Vocab.objects.all().order_by('eng')
    vocab_data = Vocab.objects.all().order_by('eng').values('eng', 'meaning')
    music = Music.objects.all().order_by('title')
    music_list = list(Music.objects.all().order_by('title').values())
    return render(request, 'vocab.html', {'vocabs':vocab,'vocab_data': vocab_data,'musics': music, 'music_list': music_list })

# def vocab(request):
#     if request.method == "POST":
#         eng = request.POST.get('eng')
#         vocab_type = request.POST.get('type')
#         meaning = request.POST.get('meaning')
        
#         data = Vocab.objects.create(
#             eng=eng, type=vocab_type, meaning=meaning
#         )
#         data.save()
#         return redirect('music:home')
    
#     return render(request, 'vocab.html')