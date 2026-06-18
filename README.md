<div align="center">

# 🔍 Noa — Number Finder | شماره یاب | مزاحم یاب

**ابزار ترمینالی برای پیدا کردن صاحب شماره یا پیدا کردن شماره با اسم**

[![Persian](https://img.shields.io/badge/Language-Persian-purple?style=for-the-badge)](README.md)

<img src="https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Termux-34a0a4?style=for-the-badge&logo=linux" />
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />

</div>

---

> [!WARNING]
> این ابزار فقط برای اهداف آموزشی و شخصیه. هر گونه سوءاستفاده به عهده خودته.

---

## ✨ چی داره؟

- جستجو با **شماره تلفن** — ببین این شماره مال کیه
- جستجو با **اسم** — شماره‌هاش رو پیدا کن
- پشتیبانی از پارسی (bidi + arabic_reshaper)

---

## 🐧 نصب روی Linux

**مرحله ۱ — Python رو نصب کن:**

Arch / Manjaro:
```bash
sudo pacman -S python python-pip
```

Ubuntu / Debian / Mint:
```bash
sudo apt install python3 python3-pip
```

Fedora:
```bash
sudo dnf install python3 python3-pip
```

**مرحله ۲ — کلون و نصب:**
```bash
git clone https://github.com/User-Noa/Number-Finder.git
cd noa-numberfinder
pip install -r requirements.txt
```

**مرحله ۳ — اجرا:**
```bash
python main.py
```

---

## 🪟 نصب روی Windows

**مرحله ۱ — Python رو نصب کن:**

برو [python.org](https://python.org) و Python 3.8+ رو دانلود کن. موقع نصب حتماً تیک `Add Python to PATH` رو بزن!

**مرحله ۲ — Git رو نصب کن:**

اگه git نداری از [git-scm.com](https://git-scm.com) نصبش کن.

**مرحله ۳ — کلون و نصب:**
```bash
git clone https://github.com/User-Noa/Number-Finder.git
cd noa-numberfinder
pip install -r requirements.txt
```

> [!NOTE]
> اگه خطای `pycryptodome` گرفتی، این رو بزن:
> ```bash
> pip install pycryptodome
> ```

**مرحله ۴ — اجرا:**
```bash
python main.py
```

---

## 📱 نصب روی Termux (اندروید)

> 💡 برای تجربه بهتر، گوشیت رو **افقی** بگیر — بنر و UI درست‌تر دیده میشه D:

**مرحله ۱ — آپدیت و پکیج‌های پایه:**
```bash
pkg update && pkg upgrade -y
pkg install python git rust -y
```

> [!IMPORTANT]
> **Rust** الزامیه! کتابخونه `python-bidi` موقع نصب باید کامپایل بشه و بدون Rust خطا میده. صبور باش، نصبش یکم طول میکشه.

**مرحله ۲ — کلون و نصب:**
```bash
git clone https://github.com/User-Noa/Number-Finder.git
cd noa-numberfinder
pip install -r requirements.txt
```

**مرحله ۳ — اجرا:**
```bash
python main.py
```

---

## 📦 requirements.txt

```
requests
pycryptodome
colorama
arabic-reshaper
python-bidi
urllib3
```

---

## 🎮 نحوه استفاده

وقتی برنامه باز شد یه منو می‌بینی:

```
  ┌─────────────────────────────────────────────────┐
  │                                                 │
  │  1  Phone lookup      find who's calling        │
  │  2  Name search       find numbers by name      │
  │                                                 │
  └─────────────────────────────────────────────────┘
```

- کلید `1` — شماره وارد کن، صاحبش رو پیدا کن
- کلید `2` — اسم وارد کن، شماره‌هاش رو پیدا کن
- کلید `q` — خروج
- کلید `b` — برگشت به منو

> [!TIP]
> شماره رو با فرمت `09XXXXXXXXX` وارد کن. اسم رو فارسی یا انگلیسی میتونی بدی.

---

## 🔧 مشکلات رایج

**خطای bidi یا arabic_reshaper روی Termux:**
```bash
pkg install rust -y
pip install python-bidi arabic-reshaper
```

**خطای pycryptodome:**
```bash
pip uninstall crypto pycrypto -y
pip install pycryptodome
```

**رنگ‌ها روی Windows درست نیستن:**

از **Windows Terminal** یا **PowerShell 7** استفاده کن. CMD قدیمی رنگ‌های ANSI رو درست نشون نمیده.

---

<div align="center">

ساخته شده با 💜 توسط **Noa**

[![Python](https://img.shields.io/badge/Made%20with-Python-3776ab?style=flat-square&logo=python)](https://python.org)

</div>
