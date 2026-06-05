def analyze_gene(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        
        # تجميع الحروف وتجاهل أول سطر
        dna = "".join(line.strip() for line in lines if not line.startswith(">"))
        
        # حساب البيانات
        length = len(dna)
        a = dna.count("A")
        t = dna.count("T")
        c = dna.count("C")
        g = dna.count("G")
        
        # حساب نسبة الـ GC (مهمة جداً لثبات الجين)
        gc_content = ((g + c) / length) * 100
        
        print(f"\n--- نتائج تحليل بيانات جين القمح ---")
        print(f"🧬 إجمالي طول الجين: {length} حرف")
        print(f"📊 نسبة الـ GC Content: {gc_content:.2f}%")
        print(f"📌 عدد قواعد الـ Adenine (A): {a}")
        print(f"📌 عدد قواعد الـ Cytosine (C): {c}")
        
    except FileNotFoundError:
        print("❌ الملف غير موجود، تأكد من الاسم!")

analyze_gene("gene_3260186644.fasta")




