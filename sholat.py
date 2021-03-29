#!/usr/bin/python
# -*- coding: utf-8 -*-
# sholatkuy version 1.0 alpha spesial ramadhan
# Author by: @pemulabelajar
# My Github: https://github.com/pemulabelajar/sholatkuy

import sys, os, io, random
import subprocess as sp
import requests
from time import sleep
from time import strftime as tm
from requests import get
from bs4 import BeautifulSoup as bs
from threading import Thread

banner = """
\033[92;1m          dP                dP           dP     dP
\033[92;1m          88                88           88     88
\033[92;1m .d8888b. 88d888b. .d8888b. 88 .d8888b. d888b   88  .dP  d8   8P d8   88
\033[92;1m Y8ooooo. 88'  `88 88'  `88 88 88'  `88  88     88888"   88   88 88   88
\033[92;1m       88 88    88 88.  .88 88 88.  .88  88     88  `8b. 88   88 88   88
\033[92;1m `88888P' dP    dP `888888' 88 `88888P8  `8888b dP   `YP `88888' `88888b
\033[92;1m                                                                     88'
\033[92;1m [\033[97;1mv1.1\033[92;1m] \033[97;1mdiupgrade oleh @pemulabelajar ( spesial ramadhan )        \033[92;1md888'\n"""

def restart():
      python = sys.executable
      os.execl(python, python, * sys.argv)
      curdir = os.getcwd()

def play():
    animation = '|/-\\'
    for i in range(50):
        sleep(0.1)
        sys.stdout.write('\r ' + animation[(i % len(animation))]+' Mencari daftar kota (lokasi)')
        sys.stdout.flush()

def write(o):
      for i in o + '\n':
          sys.stdout.write(i)
          sys.stdout.flush()
          sleep(0.03)

def gettime():
      write('\n\033[0m[\033[95m●\033[0m] Memperbarui jadwal...\n')
      try:
            ts = open('.cookie/ts','r').read()
      except IOError:
            gettown()

      ts = open('.cookie/ts','r').read()
      if len(ts) == 0:
            ts = '83'
      try:
                        r = get('https://www.jadwalsholat.org/adzan/monthly.php?id='+ts)
      except requests.exceptions.ConnectionError:
                        print('\n\033[0m[\033[91;1mx\033[0m] Internet status ( tidak ada koneksi )\033[0m')
                        print('\033[0m[\033[91;1m!\033[0m] Gagal: Nyalakan data atau Wi-Fi\033[0m')
                        input('\n\033[0m[ \033[92mTekan Enter \033[0m]')
                        menu()
      b = bs(r.text,'html.parser')
      tr = b.find('tr',class_="table_highlight")
      with open('.cookie/sc','w') as sc:
            kota = b.find('option', attrs={'value':ts})
            i = tr.find_all('td')
            sc.write(i[0].text+','"03:00"','+i[1].text+','+i[2].text+','+i[5].text+','+i[6].text+','+i[7].text+','+i[8].text+','+kota.text)
      sc.close()

def gettown():
      os.system('clear')
      sleep(1)
      print(banner)
      print()
      play()
      sleep(1.5)
      print()
      print()
      print("\033[0m[\033[96;1;2m001\033[0m] Ambarawa            \033[0m[\033[96;1;2m155\033[0m] Mentok")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m002\033[0m] Ambon               \033[0m[\033[96;1;2m156\033[0m] Merauke")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m003\033[0m] Amlapura            \033[0m[\033[96;1;2m157\033[0m] Metro")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m004\033[0m] Amuntai             \033[0m[\033[96;1;2m158\033[0m] Meulaboh")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m005\033[0m] Argamakmur          \033[0m[\033[96;1;2m159\033[0m] Mojokerto")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m006\033[0m] Atambua             \033[0m[\033[96;1;2m160\033[0m] Muara Buli")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m007\033[0m] Babao               \033[0m[\033[96;1;2m161\033[0m] Muara Bunga")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m008\033[0m] Bagan Siap          \033[0m[\033[96;1;2m162\033[0m] Muara Enim")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m009\033[0m] Bajawa              \033[0m[\033[96;1;2m163\033[0m] Muara Tewe")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m010\033[0m] Balige              \033[0m[\033[96;1;2m164\033[0m] Muara Siju")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m011\033[0m] Balik Papan         \033[0m[\033[96;1;2m165\033[0m] Muntilan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m012\033[0m] Banda Aceh          \033[0m[\033[96;1;2m166\033[0m] Nabire")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m013\033[0m] Bandar Lampung      \033[0m[\033[96;1;2m167\033[0m] Negara")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m014\033[0m] Bandung             \033[0m[\033[96;1;2m168\033[0m] Nganjuk")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m015\033[0m] Bangkalan           \033[0m[\033[96;1;2m169\033[0m] Ngawi")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m016\033[0m] Bangkinang          \033[0m[\033[96;1;2m170\033[0m] Nunukan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m017\033[0m] Bangko              \033[0m[\033[96;1;2m171\033[0m] Pacitan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m018\033[0m] Bangli              \033[0m[\033[96;1;2m172\033[0m] Padang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m019\033[0m] Banjar              \033[0m[\033[96;1;2m173\033[0m] Padang Panjang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m020\033[0m] Banjar Baru         \033[0m[\033[96;1;2m174\033[0m] Padang Sidie")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m021\033[0m] Banjarmasin         \033[0m[\033[96;1;2m175\033[0m] Pagaralam")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m022\033[0m] Banjarnegara        \033[0m[\033[96;1;2m176\033[0m] Painan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m023\033[0m] Bantaeng            \033[0m[\033[96;1;2m177\033[0m] Palangkaraya")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m024\033[0m] Banten              \033[0m[\033[96;1;2m178\033[0m] Palembang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m025\033[0m] Bantul              \033[0m[\033[96;1;2m179\033[0m] Palopo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m026\033[0m] Banyuwangi          \033[0m[\033[96;1;2m180\033[0m] Palu")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m027\033[0m] Barabai             \033[0m[\033[96;1;2m181\033[0m] Pamekasan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m028\033[0m] Barito              \033[0m[\033[96;1;2m182\033[0m] Pandeglang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m029\033[0m] Barru               \033[0m[\033[96;1;2m183\033[0m] Pangkajane")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m030\033[0m] Batang              \033[0m[\033[96;1;2m184\033[0m] Pangkajene")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m031\033[0m] Batam               \033[0m[\033[96;1;2m185\033[0m] Pangkalanbaru")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m032\033[0m] Batu                \033[0m[\033[96;1;2m186\033[0m] Pangkal Pinang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m033\033[0m] Baturaja            \033[0m[\033[96;1;2m187\033[0m] Panyabunga")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m034\033[0m] Batusangka          \033[0m[\033[96;1;2m188\033[0m] Pare")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m035\033[0m] Baubau              \033[0m[\033[96;1;2m189\033[0m] Parepare")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m036\033[0m] Bekasi              \033[0m[\033[96;1;2m190\033[0m] Pariaman")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m037\033[0m] Bengkalis           \033[0m[\033[96;1;2m191\033[0m] Pasuruan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m038\033[0m] Bengkulu            \033[0m[\033[96;1;2m192\033[0m] Pati")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m039\033[0m] Benteng             \033[0m[\033[96;1;2m193\033[0m] Payakumbuh")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m040\033[0m] Biak                \033[0m[\033[96;1;2m194\033[0m] Pekalongan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m041\033[0m] Bima                \033[0m[\033[96;1;2m195\033[0m] Pekan Baru")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m042\033[0m] Binjai              \033[0m[\033[96;1;2m196\033[0m] Pemalang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m043\033[0m] Bireuen             \033[0m[\033[96;1;2m197\033[0m] Pematang Siantar")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m044\033[0m] Bitung              \033[0m[\033[96;1;2m198\033[0m] Pendopo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m045\033[0m] Blitar              \033[0m[\033[96;1;2m199\033[0m] Pinrang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m046\033[0m] Blora               \033[0m[\033[96;1;2m200\033[0m] Pelihari")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m047\033[0m] Bogor               \033[0m[\033[96;1;2m201\033[0m] Polewali")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m048\033[0m] Bojonegoro          \033[0m[\033[96;1;2m202\033[0m] Pondok Gede")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m049\033[0m] Bondowoso           \033[0m[\033[96;1;2m203\033[0m] Ponorogo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m050\033[0m] Bontang             \033[0m[\033[96;1;2m204\033[0m] Pontianak")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m051\033[0m] Boyolali            \033[0m[\033[96;1;2m205\033[0m] Poso")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m052\033[0m] Berbes              \033[0m[\033[96;1;2m206\033[0m] Parabumlih")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m053\033[0m] Bukit Tinggib       \033[0m[\033[96;1;2m207\033[0m] Praya")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m054\033[0m] Bulukambang         \033[0m[\033[96;1;2m208\033[0m] Probolingga")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m055\033[0m] Buntok              \033[0m[\033[96;1;2m209\033[0m] Purbalingga")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m056\033[0m] Cepu                \033[0m[\033[96;1;2m210\033[0m] Purukcahu")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m057\033[0m] Ciamis              \033[0m[\033[96;1;2m211\033[0m] Purwokarta")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m058\033[0m] Cianjur             \033[0m[\033[96;1;2m212\033[0m] Purwodadi")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m059\033[0m] Cibinong            \033[0m[\033[96;1;2m213\033[0m] Purwokerto")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m060\033[0m] Cilacap             \033[0m[\033[96;1;2m214\033[0m] Purworejo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m061\033[0m] Cilegon             \033[0m[\033[96;1;2m215\033[0m] Putussibau")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m062\033[0m] Cimahi              \033[0m[\033[96;1;2m216\033[0m] Raha")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m063\033[0m] Cirebon             \033[0m[\033[96;1;2m217\033[0m] Rangkasbitung")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m064\033[0m] Curup               \033[0m[\033[96;1;2m218\033[0m] Rantau")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m065\033[0m] Demak               \033[0m[\033[96;1;2m219\033[0m] Rantauprap")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m066\033[0m] Denpasar            \033[0m[\033[96;1;2m220\033[0m] Rantepao")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m067\033[0m] Depok               \033[0m[\033[96;1;2m221\033[0m] Rembang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m068\033[0m] Dili                \033[0m[\033[96;1;2m222\033[0m] Rengat")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m069\033[0m] Dompu               \033[0m[\033[96;1;2m223\033[0m] Ruteng")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m070\033[0m] Donggala            \033[0m[\033[96;1;2m224\033[0m] Sabang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m071\033[0m] Dumai               \033[0m[\033[96;1;2m225\033[0m] Salatiga")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m072\033[0m] Ende                \033[0m[\033[96;1;2m226\033[0m] Samarinda")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m073\033[0m] Engano              \033[0m[\033[96;1;2m227\033[0m] Sampang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m074\033[0m] Enerkang            \033[0m[\033[96;1;2m228\033[0m] Sampit")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m075\033[0m] Fakfak              \033[0m[\033[96;1;2m229\033[0m] Sanggau")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m076\033[0m] Garut               \033[0m[\033[96;1;2m230\033[0m] Sawahlunto")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m077\033[0m] Gianyar             \033[0m[\033[96;1;2m231\033[0m] Sekayu")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m078\033[0m] Gombong             \033[0m[\033[96;1;2m232\033[0m] Selong")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m079\033[0m] Gorontalo           \033[0m[\033[96;1;2m233\033[0m] Semarang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m080\033[0m] Gersik              \033[0m[\033[96;1;2m234\033[0m] Sengkang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m081\033[0m] Gunung Sitompu      \033[0m[\033[96;1;2m235\033[0m] Serang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m082\033[0m] Indramayu           \033[0m[\033[96;1;2m236\033[0m] Serui")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m083\033[0m] Jakarta             \033[0m[\033[96;1;2m237\033[0m] Sibolga")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m084\033[0m] Jambi               \033[0m[\033[96;1;2m238\033[0m] Sidikalang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m085\033[0m] Jayapura            \033[0m[\033[96;1;2m239\033[0m] Sidoarjo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m086\033[0m] Jember              \033[0m[\033[96;1;2m240\033[0m] Sigli")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m087\033[0m] Jeneponto           \033[0m[\033[96;1;2m241\033[0m] Singaparna")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m088\033[0m] Jepara              \033[0m[\033[96;1;2m242\033[0m] Singaraja")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m089\033[0m] Jombang             \033[0m[\033[96;1;2m243\033[0m] Singkawang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m090\033[0m] Kabanjahe           \033[0m[\033[96;1;2m244\033[0m] Sinjai")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m091\033[0m] Kalabahi            \033[0m[\033[96;1;2m245\033[0m] Sintang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m092\033[0m] Kalianda            \033[0m[\033[96;1;2m246\033[0m] Situbondo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m093\033[0m] Kandangan           \033[0m[\033[96;1;2m247\033[0m] Slawi")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m094\033[0m] Karanganya          \033[0m[\033[96;1;2m248\033[0m] Sleman")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m095\033[0m] Karawang            \033[0m[\033[96;1;2m249\033[0m] Soasiu")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m096\033[0m] Kasungan            \033[0m[\033[96;1;2m250\033[0m] Soe")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m097\033[0m] Kayuagung           \033[0m[\033[96;1;2m251\033[0m] Solo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m098\033[0m] Kebumen             \033[0m[\033[96;1;2m252\033[0m] Solok")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m099\033[0m] Kediri              \033[0m[\033[96;1;2m253\033[0m] Soreang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m100\033[0m] Kefamenanu          \033[0m[\033[96;1;2m254\033[0m] Sorong")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m101\033[0m] Kendal              \033[0m[\033[96;1;2m255\033[0m] Sragen")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m102\033[0m] Kendari             \033[0m[\033[96;1;2m256\033[0m] Stabat")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m103\033[0m] Kertosono           \033[0m[\033[96;1;2m257\033[0m] Subang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m104\033[0m] Ketapang            \033[0m[\033[96;1;2m258\033[0m] Sukabumi")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m105\033[0m] Kisaran             \033[0m[\033[96;1;2m259\033[0m] Sukoharjo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m106\033[0m] Klaten              \033[0m[\033[96;1;2m260\033[0m] Sumbawa Besar")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m107\033[0m] Kolaka              \033[0m[\033[96;1;2m261\033[0m] Sumedang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m108\033[0m] Kota Baru           \033[0m[\033[96;1;2m262\033[0m] Sumenep")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m109\033[0m] Kota Bumi           \033[0m[\033[96;1;2m263\033[0m] Sungai Liang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m110\033[0m] Kota Janth          \033[0m[\033[96;1;2m264\033[0m] Sungai Penang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m111\033[0m] Kota Mobag          \033[0m[\033[96;1;2m265\033[0m] Sunggumina")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m112\033[0m] Kuala Kapur         \033[0m[\033[96;1;2m266\033[0m] Surabaya")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m113\033[0m] Kuala Kurung        \033[0m[\033[96;1;2m267\033[0m] Surakarta")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m114\033[0m] Kuala Pembang       \033[0m[\033[96;1;2m268\033[0m] Tabanan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m115\033[0m] Kuala Tunggu        \033[0m[\033[96;1;2m269\033[0m] Tahuna")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m116\033[0m] Kudus               \033[0m[\033[96;1;2m270\033[0m] Takalar")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m117\033[0m] Kuningan            \033[0m[\033[96;1;2m271\033[0m] Takengon")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m118\033[0m] Kupang              \033[0m[\033[96;1;2m272\033[0m] Tamiang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m119\033[0m] Kutacane            \033[0m[\033[96;1;2m273\033[0m] Tanah Grogol")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m120\033[0m] Kutoarjo            \033[0m[\033[96;1;2m274\033[0m] Tangerang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m121\033[0m] Lbuhan              \033[0m[\033[96;1;2m275\033[0m] Tanjung Baru")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m122\033[0m] Lahat               \033[0m[\033[96;1;2m276\033[0m] Tanjung Enim")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m123\033[0m] Lamongan            \033[0m[\033[96;1;2m277\033[0m] Tanjung Padang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m124\033[0m] Langsa              \033[0m[\033[96;1;2m278\033[0m] Tanjung Pinang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m125\033[0m] Larantuka           \033[0m[\033[96;1;2m279\033[0m] Tanjung Rembang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m126\033[0m] Lawang              \033[0m[\033[96;1;2m280\033[0m] Tanjung Sebang")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m127\033[0m] Lhoseumawe          \033[0m[\033[96;1;2m281\033[0m] Tapak Tuan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m128\033[0m] Limboto             \033[0m[\033[96;1;2m282\033[0m] Tarakan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m129\033[0m] Lubuk Basu          \033[0m[\033[96;1;2m283\033[0m] Tarutung")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m130\033[0m] Lubuk Linggar       \033[0m[\033[96;1;2m284\033[0m] Tasikmalaya")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m131\033[0m] Lubuk Pakang        \033[0m[\033[96;1;2m285\033[0m] Tebing Tinggi")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m132\033[0m] Lubuk Sikasika      \033[0m[\033[96;1;2m286\033[0m] Teggal")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m133\033[0m] Lumajang            \033[0m[\033[96;1;2m287\033[0m] Temanggung")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m134\033[0m] Luwuk               \033[0m[\033[96;1;2m288\033[0m] Tembilahan")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m135\033[0m] Madiun              \033[0m[\033[96;1;2m289\033[0m] Tenggarong")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m136\033[0m] Magelang            \033[0m[\033[96;1;2m290\033[0m] Ternate")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m137\033[0m] Magetan             \033[0m[\033[96;1;2m291\033[0m] Tolitoli")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m138\033[0m] Majalengka          \033[0m[\033[96;1;2m292\033[0m] Tondano")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m139\033[0m] Majene              \033[0m[\033[96;1;2m293\033[0m] Trenggalek")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m140\033[0m] Makale              \033[0m[\033[96;1;2m294\033[0m] Tual")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m141\033[0m] Makassar            \033[0m[\033[96;1;2m295\033[0m] Tuban")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m142\033[0m] Malang              \033[0m[\033[96;1;2m296\033[0m] Tulung Agung")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m143\033[0m] Mamuju              \033[0m[\033[96;1;2m297\033[0m] Ujung Beru")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m144\033[0m] Manna               \033[0m[\033[96;1;2m298\033[0m] Ungaran")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m145\033[0m] Manokwari           \033[0m[\033[96;1;2m299\033[0m] Waikabubak")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m146\033[0m] Marabahan           \033[0m[\033[96;1;2m300\033[0m] Waingapu")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m147\033[0m] Maros               \033[0m[\033[96;1;2m301\033[0m] Wamena")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m148\033[0m] Martapura           \033[0m[\033[96;1;2m302\033[0m] Watampone")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m149\033[0m] Masohi              \033[0m[\033[96;1;2m303\033[0m] Watansoppe")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m150\033[0m] Mataram             \033[0m[\033[96;1;2m304\033[0m] Wates")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m151\033[0m] Maumere             \033[0m[\033[96;1;2m305\033[0m] Wonogiri")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m152\033[0m] Medan               \033[0m[\033[96;1;2m306\033[0m] Wonosari")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m153\033[0m] Mempawah            \033[0m[\033[96;1;2m307\033[0m] Wonosobo")
      sleep(0.03)
      print("\033[0m[\033[96;1;2m154\033[0m] Manado              \033[0m[\033[96;1;2m308\033[0m] Yogyakarta")
      sleep(0.1)
      print()
      inp = input('\033[0m(\033[93;1m?\033[0m) \033[97;1mPilih nomor kota anda: \033[0m')
      if int(inp) <= 82:
                  pass
      elif int(inp) > 83 and int(inp) <= 204:
                  inp = str(int(inp)-1)
      elif int(inp) >= 205:
                  inp = str(int(inp)-1)
      else:
                  inp = '308'
      ts = open('.cookie/ts','w')
      ts.write(inp)
      ts.close()
      gettime()

def start():
      global s, d, a, m, i, tt, o, im, saur
      try:
            sleep(1)
            try:
                  o = open('.cookie/sc','r').read()
            except IOError:
                  gettime()
            o = open('.cookie/sc','r').read()
            o = o.split(',')
            if o[0] != tm('%d'):
                  gettime()
            saur = int(o[1].replace(':',''))
            im = int(o[2].replace(':',''))
            s = int(o[3].replace(':',''))
            d = int(o[4].replace(':',''))
            a = int(o[5].replace(':',''))
            m = int(o[6].replace(':',''))
            i = int(o[7].replace(':',''))
            tt = int(tm('%H%M'))
            if tt > im and tt < s:
                  ss = 'sholat Subuh'
            elif tt > s and tt < d:
                  ss = 'sholat Dzuhur'
            elif tt > d and tt < a:
                  ss = 'sholat Ashar'
            elif tt > a and tt < m:
                  ss = 'sholat Maghrib'
            elif tt > m and tt < i:
                  ss = 'sholat Isya'
            elif tt > i and saur < im or tt < 2400 and saur < im and tt < saur:
                  ss = 'Sahur'
            else:
                  ss = 'Imsak'
            os.system('clear')
            sleep(1)
            print(banner)
            print(f'''
\033[0mJadwal sholat tanggal\033[96;1;2m {tm('%d %B, %Y')}
\033[0muntuk wilayah kota\033[96;1;2m {o[8]} \033[0mdan sekitarnya.

Sahur        :       {o[1]}

Imsak        :       {o[2]}
Subuh        :       {o[3]}
Dzuhur       :       {o[4]}
Ashar        :       {o[5]}
Maghrib      :       {o[6]}
Isya         :       {o[7]}

Sedang menantikan waktu\033[96;1;2m {ss}...\033[0m\n''')
            while True:
                  tt = int(tm('%H%M'))
                  time = tm('%H:%M:%S')
                  if tt == s:
                        print('\033[0m')
                        os.system('clear')
                        sleep(1)
                        print(banner)
                        print(f'\n\033[0m[\033[94m●\033[0m] \033[97;1mSAATNYA ADZAN SUBUH\033[0m\nuntuk wilayah kota\033[96;1;2m {o[8]} \033[0mdan sekitarnya\033[0m\n')
                        sholat()
                        start()
                        break
                  elif tt == d:
                        print('\033[0m')
                        os.system('clear')
                        sleep(1)
                        print(banner)
                        print(f'\n\033[0m[\033[94m●\033[0m] \033[97;1mSAATNYA ADZAN DZUHUR\033[0m\nuntuk wilayah kota\033[96;1;2m {o[8]} \033[0mdan sekitarnya\033[0m\n')
                        sholat()
                        start()
                        break
                  elif tt == a:
                        print('\033[0m')
                        os.system('clear')
                        sleep(1)
                        print(banner)
                        print(f'\n\033[0m[\033[94m●\033[0m] \033[97;1mSAATNYA ADZAN ASHAR\033[0m\nuntuk wilayah kota\033[96;1;2m {o[8]} \033[0mdan sekitarnya\033[0m\n')
                        sholat()
                        start()
                        break
                  elif tt == m:
                        print('\033[0m')
                        os.system('clear')
                        sleep(1)
                        print(banner)
                        print(f'\n\033[0m[\033[94m●\033[0m] \033[97;1mSAATNYA ADZAN MAGHRIB\033[0m\nuntuk wilayah kota\033[96;1;2m {o[8]} \033[0mdan sekitarnya\033[0m\n')
                        sholat()
                        start()
                        break
                  elif tt == i:
                        print('\033[0m')
                        os.system('clear')
                        sleep(1)
                        print(banner)
                        print(f'\n\033[0m[\033[94m●\033[0m] \033[97;1mSAATNYA ADZAN ISYA\033[0m\nuntuk wilayah kota\033[96;1;2m {o[8]} \033[0mdan sekitarnya\033[0m\n')
                        sholat()
                        start()
                        break
                  elif tt == saur:
                        print('\033[0m')
                        os.system('clear')
                        sleep(1)
                        print(banner)
                        print(f'\n\033[0m[\033[94;1m#\033[0m] \033[97;1mWAKTUNYA BANGUN SAHUR \033[96;1;2malarm waktu sahur sudah berbunyi\n\033[0;93mKredit Sumber: \033[95;3;4m(https://youtu.be/EXjt18hF6UY)\033[0m')
                        puasa()
                        start()
                        break
                  elif tt == im:
                        print('\033[0m')
                        os.system('clear')
                        sleep(1)
                        print(banner)
                        print(f'\n\033[0m[\033[94;1m#\033[0m] \033[97;1mWAKTUNYA IMSAK \033[0muntuk wilayah kota\033[96;1;2m {o[8]} \033[0mdan sekitarnya\n\033[0;93;1mKredit Sumber: \033[95;3;4m(https://youtu.be/OODQRq9BPSI)\033[0m')
                        puasa()
                        start()
                        break
                  else:
                        print('\r\033[97;1mTekan CTRL + C > Sekarang pukul\033[91;1m {} '.format(time),end=''),;sys.stdout.flush();sleep(1)
      except KeyboardInterrupt:
            print()
            print()
            print('\033[0m[\033[91;1m!\033[0m] \033[97;1mKembali ke menu\033[0m')
            print()
            sleep(1)
            menu()

def choic():
      print('\n')
      for i in random.choice(txt):
            print(str(i.replace('\n','')),end=''),;sys.stdout.flush();sleep(0.05)
      sleep(2)

def sound():
      if tm('%H:%M') == o[1]:
          nada = '.nada/saur'
      elif tm('%H:%M') == o[2]:
            nada = '.nada/imsak'
      elif tm('%H:%M') == o[3]:
            nada = '.nada/fajr'
      else:
            nada = '.nada/adzan'
      sp.call(['mpv '+nada],shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)

def sholat():
      global txt
      txt = open('.text/__','r').readlines()
      st = ['\033[97;4;1mALHAMDULILLAH SAATNYA ADZAN. DIAM DULU YA\033[0m']
      for i in st:
          print(i.center(85))
      ttt = Thread(name='adzan',target=sound)
      ttt.start()
      while ttt.is_alive():
             choic()

def puasa():
      global txt
      if int(tm('%H%M')) == saur:
            txt = open('.text/___','r').readlines()
      else:
            txt = open('.text/____','r').readlines()
      ttx = Thread(name='puasa',target=sound)
      ttx.start()
      while ttx.is_alive():
            choic()

def menu():
      print()
      print(banner)
      print()
      print(" \033[92;1m[\033[97;1m1\033[92;1m] \033[97;1mAktifkan Sekarang")
      print(" \033[92;1m[\033[97;1m2\033[92;1m] \033[97;1mCari Kota Lokasi")
      print(" \033[92;1m[\033[97;1m3\033[92;1m] \033[97;1mKeluar Dari Program")
      print()
      option = input(" \033[92;1mPilih salah satu opsi: \033[97;1m")
      if option.strip() in '1 aktifkan'.split():
            write('\n \033[0m[\033[94m●\033[0m] \033[97;1mMengaktifkan jadwal...\033[0m')
            start()
      elif option.strip() in '2 cari'.split():
            write('\n \033[0m[\033[94m●\033[0m] \033[97;1mSedang memproses...\033[0m')
            sleep(1)
            try:
                  sp.call('rm .cookie/ts')
            except:
                  pass
            gettown()
            start()
      elif option.strip() in '3 keluar'.split():
            print("\n \033[0m[\033[91;1m!\033[0m] \033[97;1mKeluar dari program!")
            print()
            sys.exit(1)
      else:
            print("\n \033[0m[=\033[102;90;1m Masukan Salah \033[0m=]")
            print()
            sleep(1)
            restart()

if (__name__=='__main__'):
      try:
            os.mkdir('.cookie')
      except OSError:
            pass
      menu()
