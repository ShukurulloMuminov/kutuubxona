from django.shortcuts import render, redirect

from .forms import *
from django.db.models import Count
from datetime import datetime, date



def home_page_view(request):
    return render(request, 'home_page_view.html')



def muallif_view(request):
    form = MuallifForm()
    if request.method == "POST":
        Muallif.objects.create(
            ism=request.POST.get("ism"),
            jins=request.POST.get("jins"),
            t_sana=request.POST.get("t_sana"),
            kitob_soni = request.POST.get("kitob_soni") if request.POST.get("kitob_soni") else 0,
            tirik=request.POST.get("tirik") == "on",
        )
        return redirect('/mualliflar/')

    mualliflar = Muallif.objects.all()

    context = {
        'form': form,
        "mualliflar": mualliflar
    }
    return render(request, 'mualliflar.html', context)

def muallif_update_view(request, id):
        muallif = Muallif.objects.get(id=id)
        if request.method == "POST":
            muallif.ism = request.POST.get("ism")
            muallif.jins = request.POST.get("jins")
            t_sana_str = request.POST.get('t_sana')
            if t_sana_str:
                muallif.t_sana = datetime.strptime(t_sana_str, "%Y-%m-%d").date()
            muallif.kitob_soni = request.POST.get("kitob_soni") or 0
            muallif.tirik = 'tirik' in request.POST
            muallif.save()
            return redirect('/mualliflar/')
        context = {
            'muallif': muallif,

        }
        return render(request, 'muallif_update.html', context)


def muallif_details_view(request, muallif_id):

    muallif = Muallif.objects.get(id=muallif_id)

    context = {
        "muallif": muallif
    }
    return render(request, 'mualliflar_details.html', context)

def muallif_delete_view( request,  muallif_id):

    m = Muallif.objects.get(id=muallif_id)
    m.delete()

    return  redirect('/mualliflar/')

def muallif_delete_confirm_view( request, muallif_id):
    m = Muallif.objects.get(id=muallif_id)

    context = {
        'muallif': m
    }
    return render(request, 'muallif_delete_confirm.html', context)

def kitoblar_view(request):
        form =KitobForm()
        if request.method == "POST":
            form = KitobForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/kitoblar/')

        kitob = Kitob.objects.all()

        context = {
            "kitoblar": kitob,
            'forms': form
        }
        return render(request, 'kitoblar.html', context)


def kitoblar_details_view(request, kitoblar_id):

    kitoblar = Kitob.objects.get(id=kitoblar_id)
    context = {
        "kitoblar": kitoblar
    }

    return render(request, 'kitoblar_details.html', context)

def kitoblar_delete_view(request, kitob_id):
    k = Kitob.objects.get(id=kitob_id)

    k.delete()

    return redirect('/kitoblar/')

def kitoblar_delete_confirm_view(request, kitob_id):

    k = Kitob.objects.get(id=kitob_id)
    context = {
        'kitoblar' : k
    }
    return render(request, 'kitoblar_delete_confirm.html', context)






def rekordlar_view(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/record/')

    else:
        form = RecordForm()

    rekordlar = Record.objects.all()
    context = {
        "form" : form,
        "rekordlar": rekordlar
    }

    return render(request, 'rekordlar.html', context)

def rekordlar_details_view(request, rekordlar_id):
    rekordlar = Record.objects.get(id=rekordlar_id)
    context = {
        "rekordlar": rekordlar

    }

    return render(request, 'rekordlar_details.html', context)

def record_delete_view(request, record_id):
    r = Record.objects.get(id=record_id)
    r.delete()

    return redirect('/record/')


def record_delete_confirm_view(request, record_id):

    r = Record.objects.get(id=record_id)

    context = {
        'rekordlar': r
    }

    return render(request, 'record_delete_confirm.html', context)



def tirik_mualliflar_view(request):

    tirik_mualliflar=Muallif.objects.filter(tirik=True)

    context = {
        "tirik_mualliflar": tirik_mualliflar
    }
    return render(request, 'tirik_mualliflar.html', context)


def top3_sahifa_view(request):
    top3_sahifa_view = Kitob.objects.order_by('-sahifa')[:3]
    context = {
        "top3_sahifalar": top3_sahifa_view
    }
    return render(request, 'top3_sahifa.html', context)


def top3_muallif_view(request):

    top3_mualliflar = (
        Muallif.objects
        .annotate(kitoblar_count=Count('kitob'))
        .order_by('-kitoblar_count')[:3]
    )

    context = {
        "top3_mualliflar": top3_mualliflar
    }
    return render(request, 'top3_muallif.html', context)

def rekordlar_sanasi_view(request):
    oxirgi_3_record = Record.objects.order_by('-olingan_sana')[:3]

    context = {

        "oxirgi_3_record": oxirgi_3_record

        }
    return render(request, 'rekordlar_sanasi.html', context)

def tiriklar_kitobi_view(request):
    tiriklar_kitobi = Kitob.objects.filter(muallif__tirik=True)

    context = {
        "tiriklar_kitobi": tiriklar_kitobi
    }
    return render(request, 'tiriklar_kitobi.html', context)


def tarixiy_view(request):

    tarixiy = Kitob.objects.filter(janr='Tarixiy')

    context = {
        "tarixiy": tarixiy
    }
    return render(request, 'tarixiy.html', context)


def eng_katta_view(request):
    eng_katta = Muallif.objects.order_by('t_sana')[:3]

    context = {
        "eng_katta": eng_katta
    }
    return render(request, 'eng_katta.html', context)

def eng_kop_kitob_view(request):

    mualliflar = Muallif.objects.annotate(kitob_soni=Count('kitoblar')).filter(kitob_soni__gte=10)


    mualliflar_data = []


    for muallif in mualliflar:

        kitoblar = Kitob.objects.filter(muallif=muallif)
        mualliflar_data.append({
            'muallif': muallif,
            'kitoblar': kitoblar
        })

    context = {
        'mualliflar_data': mualliflar_data
    }
    return render(request, 'kitoblari_10ta.html', context)




def kutubxona_view(request):
    form = KutubxonachiForm()
    if request.method == "POST":
        kutubxonachi_form=KutubxonachiForm(request.POST)
        if kutubxonachi_form.is_valid():
            Kutubxonachi.objects.create(
                ism=request.POST.get("ism"),
                ish_vaqti=request.POST.get("vaqt"),
            )
        return redirect("/kutubxona/")

    kutubxona=Kutubxonachi.objects.all()
    context = {
        'kutubxona': kutubxona
    }
    return render(request, 'kutubxona.html', context)

def kutubxona_details_view(request, kutubxona_id):
    k = Kutubxonachi.objects.get(id=kutubxona_id)


    context = {
        'kutubxona': k
    }
    return render(request, 'kutubxona_details.html', context)

def kutubxona_delete_view(request, kutubxona_id):

    k = Kutubxonachi.objects.get(id=kutubxona_id)
    k.delete()

    return redirect('/kutubxona/')

def kutubxona_delete_confirm_view(request, kutubxona_id):
    k = Kutubxonachi.objects.get(id=kutubxona_id)

    context = {
        'kutubxona': k
    }

    return render(request, 'kutubxona_delete_confirm.html', context)

def kitoblar_update_view(request, id):
    kitoblar = Kitob.objects.get(id=id)
    mualliflar = Muallif.objects.all()

    if request.method == "POST":
        kitoblar.nom = request.POST.get("nom")
        kitoblar.janr = request.POST.get("janr")
        kitoblar.sahifa = request.POST.get("sahifa")

        muallif_id = request.POST.get("muallif_id")
        if muallif_id:
            kitoblar.muallif = Muallif.objects.get(id=muallif_id)

        kitoblar.save()
        return redirect('/kitoblar/')

    context = {
        'kitoblar': kitoblar,
        'mualliflar': mualliflar

    }

    return render(request, 'kitoblar_update.html', context)


