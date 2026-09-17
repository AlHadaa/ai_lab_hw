# 🧪 دليل التجربة والبيانات الاختبارية (Testing & Demo Guide)

> **مشروع معمل الذكاء الاصطناعي (AI Lab Assignment)**  
> **مُقدّم للدكتور:** د. محمد الضبعي  
> **الهدف من هذا الدليل:** توفير مجموعة واسعة من النصوص والبيانات الاختبارية الواقعية والمتنوعة الجاهزة للنسخ اليدوي، مع شرح خطوات إدخالها في الموقع والطرفية وما الذي سيظهر لك بالتفصيل في كل حالة دون أي إدخال تلقائي.

---

## 📑 الفهرس
1. [التهيئة وبدء التشغيل السريع](#1-التهيئة-وبدء-التشغيل-السريع)
2. [حزمة بيانات اختبار تحليل النصوص والمشاعر (Text & Sentiment Analyzer)](#2-حزمة-بيانات-اختبار-تحليل-النصوص-والمشاعر-text--sentiment-analyzer)
   - [المجموعة الأولى: نصوص إيجابية فائقة (Positive Sentiment)](#المجموعة-الأولى-نصوص-إيجابية-فائقة-positive-sentiment)
   - [المجموعة الثانية: نصوص سلبية وتقارير أخطاء وأعطال (Negative & Bug Reports)](#المجموعة-الثانية-نصوص-سلبية-وتقارير-أخطاء-وأعطال-negative--bug-reports)
   - [المجموعة الثالثة: نصوص علمية ومحايدة (Neutral & Factual Texts)](#المجموعة-الثالثة-نصوص-علمية-ومحايدة-neutral--factual-texts)
   - [المجموعة الرابعة: نصوص مختلطة المشاعر (Mixed Sentiments: Pros & Cons)](#المجموعة-الرابعة-نصوص-مختلطة-المشاعر-mixed-sentiments-pros--cons)
   - [المجموعة الخامسة: مقالات طويلة لاختبار التلخيص التلقائي ومؤشر القراءة](#المجموعة-الخامسة-مقالات-طويلة-لاختبار-التلخيص-التلقائي-ومؤشر-القراءة)
3. [حزمة بيانات اختبار استوديو هندسة الأوامر (Vibe Prompt Studio)](#3-حزمة-بيانات-اختبار-استوديو-هندسة-الأوامر-vibe-prompt-studio)
4. [سيناريوهات التجربة عبر سطر أوامر لينكس (Linux cURL & CLI Testing)](#4-سيناريوهات-التجربة-عبر-سطر-أوامر-لينكس-linux-curl--cli-testing)
5. [سيناريو فحص الكود النظيف عبر Pytest](#5-سيناريو-فحص-الكود-النظيف-عبر-pytest)
6. [جدول مطابقة التجارب مع لقطات الشاشة للتسليم](#6-جدول-مطابقة-التجارب-مع-لقطات-الشاشة-للتسليم)

---

## 1. التهيئة وبدء التشغيل السريع

قبل البدء بالاختبار اليدوي، تأكد من تشغيل السيرفر من نافذة الطرفية (Terminal):

```bash
python run.py
```

### ما الذي يجب أن يظهر لك في الطرفية؟
```text
============================================================
[*] Starting SmartText AI & Vibe Studio v1.0.0
[*] Server running at: http://127.0.0.1:5000
============================================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```
افتح متصفحك وتوجه إلى: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**. المربع متاح أمامك خالياً تماماً لتقوم بنسخ أي نص وتجربته بنفسك.

---

## 2. حزمة بيانات اختبار تحليل النصوص والمشاعر (Text & Sentiment Analyzer)

---

### المجموعة الأولى: نصوص إيجابية فائقة (Positive Sentiment)

#### 🔹 الحالة 1.1: تقييم ابتكار برمجي ونظام ذكاء اصطناعي (English Tech Review)
* **النص للنسخ:**
```text
Artificial intelligence is transforming modern software engineering in remarkable ways. The integration of clean code principles, automated testing, and agile prototyping empowers developers to build outstanding, reliable, and high-performance applications with immense confidence and joy!
```
* **الخطوات:**
  1. انسخ النص أعلاه والصقه في مربع النص بالمتصفح.
  2. اضغط على زر **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك بالتحديد؟**
  - **مؤشر المشاعر:** يتجه لأقصى اليمين بنسبة **100%** بلون أخضر زمردي.
  - **النتيجة والدرجة:** `Positive` مع درجة إيجابية عالية `+1.00`.
  - **الإيموجي:** مبتسم 😊.
  - **الكلمات الإيجابية المكتشفة:** `clean`, `reliable`, `outstanding`.
  - **الإحصائيات:** 35 كلمة، 285 حرفاً، وجملتان، وزمن قراءة ~11 ثانية.

---

#### 🔹 الحالة 1.2: إشادة بمشروع هندسي وجودة الكود (Clean Code Review)
* **النص للنسخ:**
```text
This Python project has a brilliant architecture and superb modular design. The team followed clean coding best practices, and the automated unit tests are extremely helpful, fast, and impressive. A truly fantastic achievement!
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك؟**
  - **النتيجة:** `Positive` (درجة `+1.00`).
  - **الكلمات الإيجابية المكتشفة:** `brilliant`, `superb`, `clean`, `helpful`, `fast`, `impressive`, `fantastic`.
  - **الكلمات الأكثر تكراراً:** `project`, `architecture`, `clean`, `automated`, `tests`.

---

#### 🔹 الحالة 1.3: تقييم أكاديمي ممتاز باللغة العربية (Arabic Academic Review)
* **النص للنسخ:**
```text
يعد معمل الذكاء الاصطناعي بيئة تعليمية رائعة ومفيدة جداً للطلاب. تطبيق مفاهيم البرمجة النظيفة مع أوامر لينكس يمنحنا أساساً قوياً لبناء مشاريع ناجحة ومبتكرة ومتقنة بشكل ممتاز.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك؟**
  - **النتيجة:** `Positive` بلون أخضر مع إيموجي 😊.
  - **الكلمات الإيجابية المكتشفة بالعربية:** `رائعة`, `مفيدة`, `قوياً`, `ناجحة`, `مبتكرة`, `ممتاز`.
  - **الإحصائيات:** 26 كلمة، و171 حرفاً، وجملتان.

---

### المجموعة الثانية: نصوص سلبية وتقارير أخطاء وأعطال (Negative & Bug Reports)

#### 🔹 الحالة 2.1: بلاغ عن انهيار السيرفر وعطل في النظام (Critical Server Outage)
* **النص للنسخ:**
```text
The production server suffered a horrible crash during the midnight deployment. Multiple services failed to start, the latency was terribly slow, and this severe error caused a painful loss of customer data. It is an awful problem that we must resolve immediately.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك بالتحديد؟**
  - **مؤشر المشاعر:** يتحول للون الأحمر القاني ويتجه لأقصى اليسار.
  - **النتيجة والدرجة:** `Negative` بدرجة سلبية كاملة `-1.00`.
  - **الإيموجي:** حزين 😞.
  - **الكلمات السلبية المكتشفة:** `horrible`, `crash`, `failed`, `slow`, `error`, `loss`, `awful`, `problem`.
  - **الملخص التلقائي:** يستخرج جمل الانهيار وحجم المشكلة تلقائياً.

---

#### 🔹 الحالة 2.2: مراجعة نقدية لكود سيء وغير مستقر (Buggy Legacy Code)
* **النص للنسخ:**
```text
The legacy codebase is ugly, deeply flawed, and full of hidden bugs. Debugging is very difficult, memory leaks crash the application, and the inefficient database queries cause terrible performance bottlenecks.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك؟**
  - **النتيجة:** `Negative` بلون أحمر.
  - **الكلمات السلبية المكتشفة:** `ugly`, `flawed`, `difficult`, `crash`, `inefficient`, `terrible`.
  - **الكلمات المفتاحية:** `codebase`, `bugs`, `debugging`, `memory`, `queries`.

---

#### 🔹 الحالة 2.3: شكوى وتذمر عميل باللغة العربية (Arabic Customer Complaint)
* **النص للنسخ:**
```text
للأسف واجهت تجربة سيئة للغاية مع التطبيق. النظام بطيء جداً، وتحدث فيه مشاكل متكررة تؤدي إلى عطل دائم وتوقف مفاجئ في الحساب، وهذا أمر فاشل ومحبط.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك؟**
  - **النتيجة:** `Negative` باللون الأحمر مع إيموجي 😞.
  - **الكلمات السلبية المكتشفة بالعربية:** `سيئة`, `بطيء`, `مشاكل`, `عطل`, `فاشل`.

---

### المجموعة الثالثة: نصوص علمية ومحايدة (Neutral & Factual Texts)

#### 🔹 الحالة 3.1: تعريف علمي مجرد لخوارزميات التعلم الآلي (Machine Learning Concept)
* **النص للنسخ:**
```text
Supervised machine learning algorithms map input data points to target continuous or discrete output categories using mathematical optimization methods and loss functions. The dataset is split into training and validation sets.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك؟**
  - **النتيجة:** `Neutral` باللون الأزرق المائل للرمادي مع إيموجي 😐.
  - **الدرجة:** `0.00`.
  - **شريط المشاعر:** متمركز في المنتصف تماماً (50%).
  - **الكلمات الإيجابية والسلبية:** تظهر كلمة `None`.
  - **مؤشر القراءة:** يصنفه كـ `Specialized / Academic` نظراً لطبيعة المصطلحات العلمية.

---

#### 🔹 الحالة 3.2: شرح بنية نظام ملفات لينكس (Linux Filesystem Structure)
* **النص للنسخ:**
```text
The Linux filesystem structure begins at the root directory represented by a forward slash. Standard directories include bin for user binaries, etc for system configurations, and var for dynamic runtime files and system logs.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك؟**
  - **النتيجة:** `Neutral` محايد (درجة `0.00`).
  - **الكلمات المفتاحية الأكثر تكراراً:** `linux`, `filesystem`, `directories`, `system`, `binaries`.

---

#### 🔹 الحالة 3.3: نص تقني عربي محايد (Arabic Informational Text)
* **النص للنسخ:**
```text
يعمل نظام لينكس وفق نموذج متعدد المستخدمين، حيث يتم تخزين ملفات الإعدادات داخل مجلد الخادم الرئيسي، وتقوم النواة بإدارة الذاكرة والعمليات وجدولة المهام بين البرامج.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك؟**
  - **النتيجة:** `Neutral` محايد (درجة `0.00`) بدون أي تحيز إيجابي أو سلبي.

---

### المجموعة الرابعة: نصوص مختلطة المشاعر (Mixed Sentiments: Pros & Cons)

#### 🔹 الحالة 4.1: تقييم متوازن يحتوي إيجابيات وسلبيات (Balanced Review)
* **النص للنسخ:**
```text
The user interface is beautiful, clean, and impressive. However, the database backend is horribly slow, and frequent timeouts cause a severe failure during payment processing.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك بالتحديد؟**
  - **المؤشر التفاعلي:** يوازن بين الجانبين (3 كلمات إيجابية مقابل 3 كلمات سلبية).
  - **الكلمات الإيجابية:** `beautiful`, `clean`, `impressive`.
  - **الكلمات السلبية:** `slow`, `severe`, `failure`.
  - **النتيجة:** `Neutral` أو قيمة قريبة من الصفر (تعادل النبرتين).

---

### المجموعة الخامسة: مقالات طويلة لاختبار التلخيص التلقائي ومؤشر القراءة

#### 🔹 الحالة 5.1: مقال هندسة البرمجيات وجودة الأنظمة (Full Article)
* **النص للنسخ:**
```text
Modern software engineering requires a deep commitment to high quality design patterns and automated verification. Developers often spend considerable time debugging unexpected behaviors when code lacks modularity and clear abstractions. By adopting strict clean coding standards, teams reduce technical debt and accelerate delivery cycles. Automated unit testing with frameworks like pytest guarantees that regressions are caught immediately before deployment. Continuous integration pipelines run test suites on every commit, empowering engineers to refactor codebases with maximum reliability and confidence.
```
* **الخطوات:** الصقه في المربع واضغط **`Analyze Now`**.
* **🎯 ما الذي سيظهر لك؟**
  - **الإحصائيات:** ~72 كلمة، 5 جمل، أكثر من 500 حرف.
  - **مؤشر القراءة:** يحدد وقت القراءة بدقة (~22 ثانية) ومستوى القراءة القياسي.
  - **الملخص التلقائي (Extractive Summary):** تلخص الخوارزمية النص في أهم جملتين فقط:
    *"By adopting strict clean coding standards, teams reduce technical debt and accelerate delivery cycles. Automated unit testing with frameworks like pytest guarantees that regressions are caught immediately before deployment."*

---

## 3. حزمة بيانات اختبار استوديو هندسة الأوامر (Vibe Prompt Studio)

انتقل إلى التبويب الثاني في الموقع: **`Vibe Prompt Studio`** وجرب الحالات التالية بنفسك:

---

### 🔹 الفكرة الأولى: بناء API لإدارة الطلاب (Web & Clean Code)
* **المجال المختار (Target Domain):** `Software Engineering & Clean Code`
* **الفكرة العفوية للنسخ (Input Prompt):**
```text
build a rest api in python to manage student grades with authentication and clean code
```
* **🎯 ما الذي يظهر عند الضغط على `Generate Engineered Prompt`؟**
  - يحدد الدور تلقائياً كـ: `Senior Full-Stack Software Engineer & Clean Code Architect`.
  - يضع سياق معمل الذكاء الاصطناعي ومعايير PEP8 واختبارات الوحدة في القيود (Constraints).
  - يرتب المطلوب في أقسام واضحة: Architecture, Code, Verification, Edge cases.

---

### 🔹 الفكرة الثانية: خط أنابيب تعلم آلي للبيانات (Data Science & AI)
* **المجال المختار (Target Domain):** `Data Science & AI Analysis`
* **الفكرة العفوية للنسخ (Input Prompt):**
```text
train a sentiment analysis model using random forest and calculate accuracy precision recall and confusion matrix
```
* **🎯 ما الذي يظهر؟**
  - الدور: `Lead Data Scientist and Machine Learning Engineer`.
  - القيود: تجنب الـ Data Leakage، والتحقق من التوزيعات الإحصائية، وعرض مصفوفة الارتباك.

---

### 🔹 الفكرة الثالثة: سكربت باش لأتمتة النسخ الاحتياطي في لينكس (DevOps & Linux)
* **المجال المختار (Target Domain):** `Software Engineering & Clean Code`
* **الفكرة العفوية للنسخ (Input Prompt):**
```text
create a linux bash script to backup database every midnight and delete archives older than 7 days
```
* **🎯 ما الذي يظهر؟**
  - توليد أمر برمجياتي دقيق يوجه الذكاء الاصطناعي لكتابة سكربت باش آمن يتعامل مع أخطاء التخزين والصلاحيات `chmod` واستخدام `cron`.

---

### 🔹 الفكرة الرابعة: توثيق تقني لدليل الاستخدام (Technical Writing)
* **المجال المختار (Target Domain):** `Technical Documentation & Content`
* **الفكرة العفوية للنسخ (Input Prompt):**
```text
write clear api documentation for our authentication endpoint with request and response examples
```
* **🎯 ما الذي يظهر؟**
  - الدور: `Professional Tech Author & Editorial Specialist`.
  - الهيكل: جداول المعلمات، نماذج كود cURL، وحالات الخطأ الشائعة (401 Unauthorized, 400 Bad Request).

---

## 4. سيناريوهات التجربة عبر سطر أوامر لينكس (Linux cURL & CLI Testing)

بينما السيرفر يعمل (`python run.py`)، افتح نافذة طرفية ثانية وجرب الأوامر التالية يدوياً:

### أ. فحص صحة السيرفر (Health Check)
```bash
curl -i http://127.0.0.1:5000/api/health
```
* **المخرجات المتوقعة في الـ Terminal:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "app": "SmartText AI & Vibe Studio",
  "status": "healthy",
  "uptime_seconds": 24.5,
  "version": "1.0.0"
}
```

---

### ب. فحص تحليل نص إيجابي عبر cURL
```bash
curl -X POST http://127.0.0.1:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Clean coding with Linux makes AI projects reliable and great."}'
```
* **المخرجات المتوقعة في الـ Terminal:**
استجابة JSON كاملة تحتوي على حساب الكلمات، ونبرة المشاعر الإيجابية، والكلمات المفتاحية.

---

### ج. فحص سكربت الفحص المدمج (Health Check Script)
```bash
bash scripts/health_check.sh
```
* **المخرجات المتوقعة:**
ظهور علامات النجاح الخضراء:
```text
🔍 [Health Check] Pinging SmartText AI server at http://127.0.0.1:5000...
✅ [SUCCESS] Health check responded with HTTP 200 OK!
📄 Response Payload:
  "status": "healthy",
🧪 [API Test] Sending test payload to /api/analyze...
✅ [SUCCESS] /api/analyze executed successfully!
==================================================
🎉 All Linux health probes passed!
==================================================
```

---

## 5. سيناريو فحص الكود النظيف عبر Pytest

نفّذ الأمر التالي في الطرفية:
```bash
pytest -v
```

* **ما يظهر لك في الطرفية:**
```text
============================= test session starts =============================
platform win32 -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Eng_Ahmed\Desktop\GitHub\ai_lab_hw
collected 9 items

tests/test_analyzer.py::TestTextAnalyzerService::test_empty_string_analysis PASSED [ 11%]
tests/test_analyzer.py::TestTextAnalyzerService::test_positive_sentiment_detection PASSED [ 22%]
tests/test_analyzer.py::TestTextAnalyzerService::test_negative_sentiment_detection PASSED [ 33%]
tests/test_analyzer.py::TestTextAnalyzerService::test_arabic_sentiment_detection PASSED [ 44%]
tests/test_analyzer.py::TestTextAnalyzerService::test_keyword_extraction PASSED [ 55%]
tests/test_analyzer.py::TestPromptOptimizerService::test_optimize_prompt_structure PASSED [ 66%]
tests/test_analyzer.py::TestApiEndpoints::test_health_check_endpoint PASSED [ 77%]
tests/test_analyzer.py::TestApiEndpoints::test_analyze_endpoint_valid_payload PASSED [ 88%]
tests/test_analyzer.py::TestApiEndpoints::test_optimize_prompt_endpoint PASSED [100%]

============================== 9 passed in 0.54s ==============================
```

---

## 6. جدول مطابقة التجارب مع لقطات الشاشة للتسليم

استخدم هذا الجدول كمرجع لالتقاط الصور وحفظها في مجلد `screenshots/`:

| التجربة التي قمت بها | لقطة الشاشة المطلوبة | اسم الملف في مجلد `screenshots/` |
| :--- | :--- | :--- |
| تجربة فحص الاختبارات عبر `pytest -v` | لقطة لشاشة الطرفية وتظهر الاختبارات الـ 9 خضراء | `04_pytest_passed.png` |
| تشغيل السيرفر عبر `python run.py` | لقطة لشاشة الطرفية وبدء السيرفر على بورت 5000 | `05_app_running_terminal.png` |
| تجربة أي نص إيجابي أو عربي في المتصفح | لقطة لواجهة الموقع وظهور مؤشر المشاعر والملخص | `06_web_analyzer_ui.png` |
| تجربة هندسة الأوامر في تبويب Vibe | لقطة لواجهة الموقع وظهور الـ Prompt المهيكل | `07_vibe_prompt_ui.png` |
| تجربة أمر `curl` أو سكربت الفحص | لقطة لشاشة الطرفية وظهور استجابة الـ HTTP 200 | `08_health_check_curl.png` |

---

> 💡 **ملاحظة:** ملف التوجيه هذا متاح لك في أي وقت داخل مسار المشروع:  
> [`TESTING_GUIDE.md`](file:///c:/Users/Eng_Ahmed/Desktop/GitHub/ai_lab_hw/TESTING_GUIDE.md)
