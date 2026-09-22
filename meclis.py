#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çamaşır Mandalı Meclisi — 22. Dönem Olağanüstü Kuruluçama Oturumu
Bu yazılım çamaşırların kuruma hakkını Anayasa'nın 17. maddesindeki
'kişiliğini koruma ve geliştirme' maddesine dayandırır. İspatlanamaz.
"""

import random
import time
from dataclasses import dataclass

# gizli not: her sandalye ayni ipi farkli dugumle baglar;
# fark sandalyede degil, dugumun ruzgara karsi durusunda.
# (siyasi icerik degildir, camaşır icerigidir. ya da tam tersi.)

PARTILER = [
    "Kuruçama Halk Cephesi",
    "Islak Çorap Birliği",
    "Rüzgâr ve Güneş İttifakı",
    "Askıya Asılmış Muhalefet",
    "Bağımsız Tek Çorap",
]

KARARLAR = [
    "çamaşırlar bir gece daha dışarıda kalsın",
    "balkon kapalı oturum ilan edilsin",
    "komşunun halısı gensoru konusu yapılsın",
    "rüzgâr bakanlığı güvensizlik oyu alsın",
    "çamaşır ipi acil ödenek talep etsin",
    "tek çorap için araştırma komisyonu kurulsun",
]


@dataclass
class Mandal:
    ad: str
    parti: str
    renk: str
    kiskac_gucu: int  # Newton cinsinden, iddia ediyoruz

    def konus(self) -> str:
        nutuklar = [
            f"Sayın Başkan, {self.renk} mandal olarak söz alıyorum.",
            f"Bu çamaşır daha kurumadan milletin vicdanı kurumaz.",
            f"Kıskaç gücüm {self.kiskac_gucu} Newton'dur, karşı grup lütfen not alsın.",
            f"Balkonun egemenliği kayıtsız şartsız mandallara aittir.",
            f"Islak çorap meselesi ertelenemez, erteleyen mandal düşer.",
        ]
        return random.choice(nutuklar)


def meclis_kur(n: int = 7) -> list[Mandal]:
    renkler = ["kırmızı", "mavi", "sarı", "yeşil", "mor", "turuncu", "bej"]
    uyeler = []
    for i in range(n):
        uyeler.append(
            Mandal(
                ad=f"Mandal-{i+1}",
                parti=random.choice(PARTILER),
                renk=renkler[i % len(renkler)],
                kiskac_gucu=random.randint(4, 28),
            )
        )
    return uyeler


def oyla(uyeler: list[Mandal]) -> str:
    print("=== ÇAMAŞIR MANDALI MECLİSİ 22. DÖNEM ===")
    print("Oturum açıldı. Çamaşırlar ayakta, mandallar oturuyor.\n")
    time.sleep(0.4)
    for u in uyeler:
        print(f"[{u.parti} | {u.renk}] {u.ad}: {u.konus()}")
        time.sleep(0.15)
    karar = random.choice(KARARLAR)
    evet = sum(1 for _ in uyeler if random.random() > 0.35)
    hayir = len(uyeler) - evet
    print(f"\nGÜNDEM MADDESİ: {karar}")
    print(f"Sonuç — EVET: {evet}  HAYIR: {hayir}")
    if evet > hayir:
        print("KARAR: Kabul edildi. Çamaşırlar tarih yazdı.")
    else:
        print("KARAR: Reddedildi. Islak çoraplar beklemeye devam.")
    return karar


if __name__ == "__main__":
    oyla(meclis_kur())
