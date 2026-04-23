

# 📦 مشروع CRUD باستخدام Python و MongoDB

## 🧑‍💻 نظرة عامة على المشروع
هذا المشروع عبارة عن تطبيق بسيط لإدارة المنتجات (CRUD) تم تطويره باستخدام **Python** وربطه مع قاعدة بيانات **MongoDB** باستخدام مكتبة PyMongo.

يعمل البرنامج عبر واجهة سطر الأوامر (Terminal) ويتيح للمستخدم إدارة المنتجات بسهولة.

---

## ⚙️ التقنيات المستخدمة
- Python 3.x
- MongoDB
- PyMongo
- VS Code;
      pip install pymongo; تثبيت المكتبة

---

## 🗄️ قاعدة البيانات

- اسم قاعدة البيانات: `info`
- اسم المجموعة (Collection): `produits`

### 📄 مثال على البيانات:
```json
{
  "nom": "Macbook Pro",
  "fabriquant": "Apple",
  "prix": 11435.99,
  "options": ["Intel Core i5", "Retina Display", "Long life battery"]
}
# 🚀 مميزات المشروع (CRUD)

## ➕ إضافة (Create)
إضافة منتج جديد مع:
- الاسم  
- الشركة المصنعة  
- السعر  

---

## 📄 عرض (Read)
عرض جميع المنتجات المخزنة في قاعدة البيانات.

---

## 🔍 بحث (Search)
البحث عن منتج باستخدام الاسم أو جزء منه.

---

## ✏️ تعديل (Update)
تعديل سعر منتج معين.

---

## 🗑️ حذف (Delete)
حذف منتج باستخدام الاسم.

---

## 🧾 واجهة البرنامج

```text
===== MENU =====
1 - Ajouter
2 - Afficher
3 - Chercher
4 - Modifier
5 - Supprimer
0 - Quitter
