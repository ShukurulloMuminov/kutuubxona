from django.db import models


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=50, blank=True, null=True)
    kurs = models.PositiveSmallIntegerField(default=1)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    class JINS_CHOICES(models.TextChoices):
        ERKAK = 'Erkak', 'Erkak'
        AYOL = 'Ayol', 'Ayol'

    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10, choices=JINS_CHOICES.choices, blank=True, null=True)
    t_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50, blank=True, null=True)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        if self.muallif:
            return f"{self.nom} [{self.muallif.ism}]"
        return self.nom


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, blank=True, null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, blank=True, null=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.SET_NULL, blank=True, null=True)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytargan_sana = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.talaba.ism} -- {self.kitob.nom}"
