#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator Matriks Data Geografis 44 Kecamatan (Magelang & Temanggung)
Untuk Programmatic Local SEO Distributor Beras Premium Ladori
"""

import os
import sys
import json

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

KECAMATAN_DATA = {
    "kabupaten_magelang": {
        "nama_daerah": "Kabupaten Magelang",
        "tipe": "Kabupaten",
        "pusat_koordinat": {"lat": -7.5023, "lng": 110.2185},
        "kecamatan": [
            {"nama": "Mertoyudan", "slug": "mertoyudan", "karakteristik": "Pusat bisnis, perumahan padat, jalur utama Jogja-Magelang, Artos Mall", "rute_hari": "Senin - Sabtu (Setiap Hari)", "landmark": "Dekat Artos Mall & Jl. Mayjen Bambang Soegeng"},
            {"nama": "Muntilan", "slug": "muntilan", "karakteristik": "Sentra grosir pasar tradisional terbesar Magelang, toko sembako padat", "rute_hari": "Selasa & Jumat", "landmark": "Pasar Muntilan & Klenteng Hok An Kiong"},
            {"nama": "Borobudur", "slug": "borobudur", "karakteristik": "Kawasan pariwisata internasional, klaster hotel berbintang, resto & homestay", "rute_hari": "Rabu & Sabtu", "landmark": "Kawasan Taman Wisata Candi Borobudur"},
            {"nama": "Secang", "slug": "secang", "karakteristik": "Simpang pertemuan Magelang - Temanggung - Semarang, lalu lintas logistik", "rute_hari": "Senin & Kamis", "landmark": "Pertigaan Secang & Pasar Secang"},
            {"nama": "Mungkid", "slug": "mungkid", "karakteristik": "Pusat pemerintahan Kabupaten Magelang, perkantoran & perumahan", "rute_hari": "Selasa & Jumat", "landmark": "Kompleks Pemkab Magelang & Candi Mendut"},
            {"nama": "Grabag", "slug": "grabag", "karakteristik": "Sentra pasar sayur lereng Andong, toko kelontong pedesaan", "rute_hari": "Rabu", "landmark": "Pasar Grabag & Pemandian Air Hangat Candi Umbul"},
            {"nama": "Bandongan", "slug": "bandongan", "karakteristik": "Area sub-urban barat Kali Progo, pemukiman padat berkembang", "rute_hari": "Senin & Kamis", "landmark": "Jembatan Kali Progo & Pasar Bandongan"},
            {"nama": "Salaman", "slug": "salaman", "karakteristik": "Pintu gerbang Purworejo - Magelang, sentra bibit tanaman & UMKM", "rute_hari": "Selasa & Sabtu", "landmark": "Pasar Salaman & Bundaran Salaman"},
            {"nama": "Tegalrejo", "slug": "tegalrejo", "karakteristik": "Sentra pendidikan pesantren besar (ribuan santri) & agribisnis", "rute_hari": "Senin & Kamis", "landmark": "Pondok Pesantren API Tegalrejo & Pasar Tegalrejo"},
            {"nama": "Candimulyo", "slug": "candimulyo", "karakteristik": "Sentra durian dan perkebunan, warung sembako pedesaan", "rute_hari": "Rabu", "landmark": "Pasar Baledono & Jalur Candimulyo"},
            {"nama": "Kaliangkrik", "slug": "kaliangkrik", "karakteristik": "Lereng Gunung Sumbing, jalur wisata Nepal van Java, warung wisata", "rute_hari": "Kamis", "landmark": "Nepal van Java Dusun Butuh & Pasar Kaliangkrik"},
            {"nama": "Dukun", "slug": "dukun", "karakteristik": "Lereng Gunung Merapi barat, sentra pertanian dan peternakan", "rute_hari": "Selasa", "landmark": "Jembatan Talang & Pasar Dukun"},
            {"nama": "Sawangan", "slug": "sawangan", "karakteristik": "Jalur Magelang - Boyolali, sentra beras organik dan sayuran", "rute_hari": "Rabu", "landmark": "Ketep Pass & Pasar Sawangan"},
            {"nama": "Tempuran", "slug": "tempuran", "karakteristik": "Kawasan industri tekstil/pabrik & perumahan buruh pabrik", "rute_hari": "Jumat", "landmark": "Kawasan Industri Tempuran & Pasar Tanggulrejo"},
            {"nama": "Ngluwar", "slug": "ngluwar", "karakteristik": "Perbatasan Sleman/DIY, area persawahan subur dan toko kelontong", "rute_hari": "Selasa", "landmark": "Bendungan Ancol Karangtalun"},
            {"nama": "Srumbung", "slug": "srumbung", "karakteristik": "Sentra salak pondoh lereng Merapi, toko desa dan katering hajatan", "rute_hari": "Kamis", "landmark": "Pos Pengamatan Babadan Merapi"},
            {"nama": "Salam", "slug": "salam", "karakteristik": "Pintu masuk DIY - Jateng, jalur arteri logistik truk antar provinsi", "rute_hari": "Senin & Jumat", "landmark": "Jembatan Krasak & Pasar Semampir"},
            {"nama": "Pakis", "slug": "pakis", "karakteristik": "Dataran tinggi Merbabu, sentra sayur-mayur dan toko kelontong lereng", "rute_hari": "Rabu", "landmark": "Pasar Kaponan & Jalur Wisata Kopeng"},
            {"nama": "Windusari", "slug": "windusari", "karakteristik": "Lereng timur laut Gunung Sumbing, perkampungan dan pertanian", "rute_hari": "Kamis", "landmark": "Candi Selogriyo & Pasar Windusari"},
            {"nama": "Kajoran", "slug": "kajoran", "karakteristik": "Perbatasan Wonosobo tenggara, sentra perdagangan desa", "rute_hari": "Jumat", "landmark": "Pasar Kajoran & Air Terjun Sigetik"},
            {"nama": "Ngablak", "slug": "ngablak", "karakteristik": "Kawasan wisata alam lereng Telomoyo & Andong, resto & kafe wisata", "rute_hari": "Rabu", "landmark": "Gunung Telomoyo & Pasar Ngablak"}
        ]
    },
    "kota_magelang": {
        "nama_daerah": "Kota Magelang",
        "tipe": "Kota",
        "pusat_koordinat": {"lat": -7.4797, "lng": 110.2177},
        "kecamatan": [
            {"nama": "Magelang Selatan", "slug": "magelang-selatan", "karakteristik": "Kawasan pemukiman elit, kampus Tidar, rute kuliner Tidar", "rute_hari": "Senin - Sabtu (Setiap Hari)", "landmark": "Bukit Tidar & Terminal Tidar"},
            {"nama": "Magelang Tengah", "slug": "magelang-tengah", "karakteristik": "Jantung perekonomian kota, Pasar Rejowinangun, pusat pertokoan Pecinan", "rute_hari": "Senin - Sabtu (Setiap Hari)", "landmark": "Alun-Alun Magelang & Pasar Rejowinangun"},
            {"nama": "Magelang Utara", "slug": "magelang-utara", "karakteristik": "Sentra perumahan utara, RSJ Soerojo, pertokoan jalan raya Semarang", "rute_hari": "Senin - Sabtu (Setiap Hari)", "landmark": "RSJ Prof. Dr. Soerojo & Taman Kyai Langgeng utara"}
        ]
    },
    "kabupaten_temanggung": {
        "nama_daerah": "Kabupaten Temanggung",
        "tipe": "Kabupaten",
        "pusat_koordinat": {"lat": -7.3167, "lng": 110.1667},
        "kecamatan": [
            {"nama": "Temanggung Kota", "slug": "temanggung-kota", "karakteristik": "Pusat pemerintahan kabupaten, sentra kuliner, Pasar Kliwon", "rute_hari": "Senin, Rabu, Jumat", "landmark": "Alun-Alun Temanggung & Pasar Kliwon"},
            {"nama": "Parakan", "slug": "parakan", "karakteristik": "Kota perdagangan grosir tertua dan tersibuk, pusat kulakan pedagang se-Temanggung", "rute_hari": "Selasa, Kamis, Sabtu", "landmark": "Pasar Legi Parakan & Kawasan Pecinan Parakan"},
            {"nama": "Ngadirejo", "slug": "ngadirejo", "karakteristik": "Pusat ekonomi Temanggung bagian utara, pasar komoditas hasil bumi", "rute_hari": "Selasa & Jumat", "landmark": "Situs Liyangan & Pasar Ngadirejo"},
            {"nama": "Kranggan", "slug": "kranggan", "karakteristik": "Gerbang selatan Temanggung dari arah Secang/Magelang, jalur distribusi utama", "rute_hari": "Senin, Rabu, Jumat", "landmark": "Jembatan Progo Kranggan & Pasar Kranggan"},
            {"nama": "Bulu", "slug": "bulu", "karakteristik": "Jalur penghubung Temanggung - Parakan, industri perkayuan dan warung makan", "rute_hari": "Selasa & Kamis", "landmark": "Jalur Utama Bulu & Rest Area"},
            {"nama": "Candiroto", "slug": "candiroto", "karakteristik": "Sentra perkebunan kopi/cengkeh dan pasar perdagangan utara", "rute_hari": "Kamis", "landmark": "Pasar Candiroto"},
            {"nama": "Kedu", "slug": "kedu", "karakteristik": "Area persawahan subur tengah Temanggung, perumahan dan toko sembako", "rute_hari": "Rabu", "landmark": "Pasar Kedu & Balai Desa Kedu"},
            {"nama": "Jumo", "slug": "jumo", "karakteristik": "Daerah pertanian dan perkebunan tembakau, toko kelontong desa", "rute_hari": "Kamis", "landmark": "Pasar Jumo"},
            {"nama": "Kaloran", "slug": "kaloran", "karakteristik": "Perbatasan barat daya Semarang/Sumowono, warung desa dan katering", "rute_hari": "Senin", "landmark": "Pasar Kaloran"},
            {"nama": "Kandangan", "slug": "kandangan", "karakteristik": "Sentra kerajinan dan perdagangan jalur tembus Secang-Temanggung", "rute_hari": "Rabu", "landmark": "Pasar Kandangan"},
            {"nama": "Pringsurat", "slug": "pringsurat", "karakteristik": "Pintu gerbang perbatasan Semarang (Ambarawa), jalur truk kontainer", "rute_hari": "Senin & Kamis", "landmark": "Terminal Pringsurat & Pasar Pingit"},
            {"nama": "Selopampang", "slug": "selopampang", "karakteristik": "Lereng Gunung Sumbing selatan, persawahan terasering", "rute_hari": "Selasa", "landmark": "Kawasan Lereng Sumbing"},
            {"nama": "Tembarak", "slug": "tembarak", "karakteristik": "Sentra pesantren, pemukiman padat religi dan toko sembako", "rute_hari": "Selasa", "landmark": "Pesantren Tembarak & Pasar Menggoro"},
            {"nama": "Tlogomulyo", "slug": "tlogomulyo", "karakteristik": "Sentra tembakau srintil lereng Sumbing, daya beli musiman tinggi", "rute_hari": "Jumat", "landmark": "Kawasan Sentra Tembakau Sumbing"},
            {"nama": "Bansari", "slug": "bansari", "karakteristik": "Lereng Sindoro selatan, wisata Embung Bansari, toko desa", "rute_hari": "Kamis", "landmark": "Embung Bansari"},
            {"nama": "Bejen", "slug": "bejen", "karakteristik": "Temanggung utara perbatasan Kendal, kawasan hutan jati & pertanian", "rute_hari": "Rabu", "landmark": "Jalur Bejen - Sukorejo"},
            {"nama": "Gemawang", "slug": "gemawang", "karakteristik": "Sentra kopi robusta Temanggung dan batik lokal, warung sembako", "rute_hari": "Senin", "landmark": "Pasar Gemawang"},
            {"nama": "Kledung", "slug": "kledung", "karakteristik": "Celah antara Sindoro dan Sumbing, jalur wisata Wonosobo, resto & kafe", "rute_hari": "Sabtu", "landmark": "Posong & Kledung Park"},
            {"nama": "Tretep", "slug": "tretep", "karakteristik": "Dataran tinggi perbatasan Wonosobo/Kendal, desa pertanian sayur", "rute_hari": "Kamis", "landmark": "Pasar Tretep"},
            {"nama": "Wonoboyo", "slug": "wonoboyo", "karakteristik": "Situs bersejarah emas Wonoboyo, daerah pertanian lereng Sindoro", "rute_hari": "Jumat", "landmark": "Situs Cagar Budaya Wonoboyo"}
        ]
    }
}

def main():
    output_path = os.path.join(DATA_DIR, 'kecamatan_magelang_temanggung.json')
    total_kec = len(KECAMATAN_DATA["kabupaten_magelang"]["kecamatan"]) + \
                len(KECAMATAN_DATA["kota_magelang"]["kecamatan"]) + \
                len(KECAMATAN_DATA["kabupaten_temanggung"]["kecamatan"])
                
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(KECAMATAN_DATA, f, indent=2, ensure_ascii=False)
        
    print("=" * 70)
    print("🌾 GENERATOR MATRIKS 44 KECAMATAN (MAGELANG & TEMANGGUNG)")
    print("=" * 70)
    print(f"✅ Total Wilayah Terdata: {total_kec} Kecamatan")
    print(f"   • Kabupaten Magelang: {len(KECAMATAN_DATA['kabupaten_magelang']['kecamatan'])} Kecamatan")
    print(f"   • Kota Magelang     : {len(KECAMATAN_DATA['kota_magelang']['kecamatan'])} Kecamatan")
    print(f"   • Kab. Temanggung   : {len(KECAMATAN_DATA['kabupaten_temanggung']['kecamatan'])} Kecamatan")
    print(f"📁 File JSON tersimpan di: {output_path}")
    print("=" * 70)

if __name__ == '__main__':
    main()
