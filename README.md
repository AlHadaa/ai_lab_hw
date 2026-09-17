# 🚀 SmartText AI & Vibe Studio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1%2B-black.svg)](https://flask.palletsprojects.com/)
[![Code Style: Clean Code](https://img.shields.io/badge/Code%20Style-Clean%20Code%20%2F%20PEP8-emerald.svg)](https://peps.python.org/pep-0008/)
[![Tests: Pytest](https://img.shields.io/badge/Tests-Passing%20(9%2F9)-brightgreen.svg)](https://pytest.org/)
[![Vibe Coding](https://img.shields.io/badge/Vibe%20Coding-Active-purple.svg)]()

> **مشروع معمل الذكاء الاصطناعي (AI Lab) - إشراف: د. محمد الضبعي**  
> تطبيق ويب متكامل ومبني من الصفر يجسد التطبيق العملي لجميع مفاهيم الدورة: **أوامر لينكس (Linux)**، **إدارة الإصدارات (Git/GitHub)**، **البرمجة النظيفة (Clean Coding)**، و**البرمجة التفاعلية الحديثة (Vibe Coding)**.

---

## 📌 الفهرس / Table of Contents
1. [نظرة عامة على المشروع (Project Overview)](#-نظرة-عامة-على-المشروع-project-overview)
2. [الأركان الأربعة للمشروع (Core Pillars)](#-الأركان-الأربعة-للمشروع-core-pillars)
   - [1. أوامر لينكس (Linux Commands)](#1-أوامر-لينكس-linux-commands)
   - [2. إدارة المستودعات (Git & GitHub Workflow)](#2-إدارة-المستودعات-git--github-workflow)
   - [3. البرمجة النظيفة (Clean Coding)](#3-البرمجة-النظيفة-clean-coding)
   - [4. البرمجة التفاعلية (Vibe Coding)](#4-البرمجة-التفاعلية-vibe-coding)
3. [هيكلية المشروع (Project Architecture)](#-هيكلية-المشروع-project-architecture)
4. [دليل التشغيل السريع (Quickstart Guide)](#-دليل-التشغيل-السريع-quickstart-guide)
5. [أوامر الفحص والـ API (API Endpoints & Health Check)](#-أوامر-الفحص-والـ-api-api-endpoints--health-check)
6. [دليل لقطات الشاشة والتسليم (Screenshots & Submission)](#-دليل-لقطات-الشاشة-والتسليم-screenshots--submission)

---

## 🌟 نظرة عامة على المشروع (Project Overview)

**SmartText AI & Vibe Studio** هو تطبيق ويب تحليلي ذكي يوفّر:
- **تحليل النصوص والمشاعر (Sentiment & Text Analytics):** حساب دقيق لعدد الكلمات، الحروف، الجمل، وسرعة القراءة، مع كشف فوري لنبرة النص (إيجابي / سلبي / محايد) ودعم اللغتين العربية والإنجليزية.
- **التلخيص الاستخراجي (Extractive Summarizer):** استخراج أهم الجمل والمفاهيم الرئيسية تلقائياً.
- **استوديو Vibe Coding وهندسة الأوامر (Prompt Engineering Studio):** تحويل الأفكار الأولية البسيطة إلى أوامر احترافية مهيكلة للذكاء الاصطناعي وفق المعايير العالمية (Role, Task, Context, Constraints, Format).

---

## 🏛 الأركان الأربعة للمشروع (Core Pillars)

### 1. أوامر لينكس (Linux Commands)
تم تضمين سكربتات باش وأوامر طرفية فعلية داخل المشروع:
- **إدارة الصلاحيات (Permissions):**
  ```bash
  chmod +x scripts/*.sh
  ls -la scripts/
  ```
- **التنقل وإنشاء المجلدات واستعراض الملفات:**
  ```bash
  mkdir -p screenshots
  cat requirements.txt
  grep "Flask" requirements.txt
  ```
- **فحص صحة السيرفر عبر cURL ومراقبة العمليات:**
  ```bash
  # فحص حالة السيرفر
  curl -s http://127.0.0.1:5000/api/health | grep "status"

  # مراقبة عمليات بايثون النشطة في لينكس
  ps aux | grep python
  ```
- **أتمتة المهام عبر Makefile و Bash Scripts:**
  - `scripts/setup.sh` (إعداد البيئة الافتراضية وتثبيت المتطلبات)
  - `scripts/run.sh` (تشغيل السيرفر)
  - `scripts/health_check.sh` (اختبار الـ Endpoints برمجياً)

---

### 2. إدارة المستودعات (Git & GitHub Workflow)
تم الالتزام بأفضل ممارسات Git الاحترافية:
- **تهيئة المستودع واستثناء الملفات المؤقتة:**
  ملف `.gitignore` مهيأ بالكامل لاستثناء بيئات العمل الافتراضية وكاش بايثون.
- **استراتيجية الفروع (Branching Strategy):**
  العمل عبر فرع مخصص للميزات `feature/smart-text-analyzer` ثم دمجه مع `main`.
- **رسائل الالتزام القياسية (Conventional Commits):**
  - `feat: implement text analyzer service and sentiment scoring`
  - `feat: add vibe prompt engineering studio UI`
  - `test: add comprehensive pytest unit test suite`
  - `docs: add project documentation and screenshots guide`

---

### 3. البرمجة النظيفة (Clean Coding)
تم تطبيق قواعد الكود النظيف بمعايير عالية:
1. **نمط مصنع التطبيق (Application Factory Pattern):** فصل إعدادات التطبيق داخل `create_app()` في [`app/__init__.py`](file:///app/__init__.py).
2. **مبدأ المسؤولية الفردية (Single Responsibility Principle - SRP):**
   - **النماذج (`app/models/`):** تعريف تراكيب البيانات عبر `dataclasses` مع Type Hints كاملة.
   - **الخدمات (`app/services/`):** عزل منطق الأعمال الحسابي والتحليلي داخل كلاسات مستقلة سهلة الاختبار.
   - **المسارات (`app/routes/`):** استقبال طلبات HTTP والتحقق من صحة المدخلات.
3. **التوثيق ومعايير PEP 8:** جميع الدوال والكلاسات مزودة بـ Docstrings وتسميات ذات مغزى دلالي.
4. **الاختبارات الآلية (Unit Testing):** 9 اختبارات كاملة تغطي حالات الإدخال والحالات الحدية (Edge Cases) باستخدام مكتبة `pytest`.

---

### 4. البرمجة التفاعلية (Vibe Coding)
- دمج الذكاء الاصطناعي وتسريع التطوير عبر دورة تغذية راجعة فورية (Instant Feedback Loop).
- واجهة تفاعلية حديثة بأسلوب **Dark Mode + Glassmorphism** مبنية باستخدام **Tailwind CSS** وأيقونات **Lucide**.
- أداة متخصصة داخل التطبيق لمساعدة المطورين على ممارسة "Vibe Coding" من خلال تحسين وهندسة الـ Prompts لتوليد أفضل مخرجات برمجية من نماذج الذكاء الاصطناعي.

---

## 📁 هيكلية المشروع (Project Architecture)

```text
ai_lab_hw/
├── app/
│   ├── __init__.py              # Application Factory (create_app)
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py            # إعدادات وبيئة التشغيل (AppConfig)
│   ├── models/
│   │   ├── __init__.py
│   │   └── analysis.py          # نماذج البيانات المهيكلة (Dataclasses & Typing)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── text_analyzer.py     # منطق تحليل النصوص والمشاعر (Clean Code)
│   │   └── prompt_optimizer.py  # منطق هندسة الأوامر الذكية (Vibe Coding)
│   ├── routes/
│   │   ├── __init__.py
│   │   └── api.py               # نقاط اتصال الـ REST API وعرض الواجهة
│   ├── static/
│   │   ├── css/style.css        # التنسيقات المخصصة
│   │   └── js/main.js           # التفاعل البرمجي للواجهة
│   └── templates/
│       └── index.html           # واجهة المستخدم الحديثة (Tailwind CSS)
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py         # اختبارات الوحدة الآلية (Pytest)
├── scripts/
│   ├── setup.sh                 # سكربت لينكس لتهيئة المشروع وتثبيت المتطلبات
│   ├── run.sh                   # سكربت لينكس لتشغيل السيرفر
│   └── health_check.sh          # سكربت لينكس لفحص endpoints باستخدام curl
├── screenshots/
│   ├── .gitkeep
│   └── README.md                # دليل تنظيم وتسمية لقطات الشاشة للتسليم
├── .gitignore                   # استثناء الملفات المؤقتة والكاش
├── Makefile                     # أتمتة أوامر لينكس (make run, make test)
├── requirements.txt             # المكتبات والاعتماديات
├── run.py                       # نقطة انطلاق السيرفر
└── README.md                    # وثيقة المشروع التوضيحية
```

---

## ⚡ دليل التشغيل السريع (Quickstart Guide)

### 1. تثبيت المتطلبات (Requirements Installation)
```bash
pip install -r requirements.txt
```

### 2. تشغيل الاختبارات الآلية (Run Clean Code Tests)
```bash
pytest -v
```
ستظهر جميع الاختبارات التسعة باللون الأخضر ✅.

### 3. تشغيل تطبيق الويب (Start Server)
```bash
python run.py
```
افتح المتصفح وتوجه إلى:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📡 أوامر الفحص والـ API (API Endpoints & Health Check)

يمكنك فحص النظام من طرفية لينكس باستخدام `curl`:

1. **فحص صحة السيرفر (Health Check):**
   ```bash
   curl -i http://127.0.0.1:5000/api/health
   ```

2. **تحليل نص عبر POST API:**
   ```bash
   curl -X POST http://127.0.0.1:5000/api/analyze \
     -H "Content-Type: application/json" \
     -d '{"text": "Python clean coding is impressive and reliable."}'
   ```

3. **هندسة أمر ذكاء اصطناعي (Vibe Coding Prompt API):**
   ```bash
   curl -X POST http://127.0.0.1:5000/api/optimize-prompt \
     -H "Content-Type: application/json" \
     -d '{"prompt": "build a modern web app", "domain": "code"}'
   ```

---

## 📸 دليل لقطات الشاشة والتسليم (Screenshots & Submission)

قم بالتقاط الصور التالية وحفظها داخل مجلد `screenshots/` لإرسالها للدكتور:
1. `01_git_init_status.png` : أوامر Git الأولى (`git status`, `git add`)
2. `02_git_commit_branch.png` : إنشاء الفرع وتثبيت التعديلات (`git commit`)
3. `03_linux_commands.png` : تنفيذ أوامر لينكس (`ls -la`, `chmod +x`, `cat`, `grep`)
4. `04_pytest_passed.png` : نجاح الاختبارات الآلية عبر `pytest -v`
5. `05_app_running_terminal.png` : تشغيل السيرفر من الطرفية عبر `python run.py`
6. `06_web_analyzer_ui.png` : واجهة الموقع عند تحليل نص تجريبي وظهور النتيجة
7. `07_vibe_prompt_ui.png` : تبويب Vibe Coding عند توليد الـ Prompt
8. `08_health_check_curl.png` : استجابة أمر `curl` لفحص السيرفر
9. `09_github_repo_public.png` : المستودع وهو Public على GitHub

---
**جامعة المستقبل / الكلية - معمل الذكاء الاصطناعي**  
إشراف: **د. محمد الضبعي**
