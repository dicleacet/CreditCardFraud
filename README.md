# CreditCardFraud
Bu proje dolandırıcıları engellemek için sahte kredi kartlarını bulan bir machine learn projesidir. Python dilinde yazılmış olup Sklearn, Pandas ve Matplotlib teknolojileri kullanılmıştır.

## Database Bilgileri 
Veri seti, Avrupalı kart sahipleri tarafından Eylül 2013'te kredi kartlarıyla yapılan işlemleri içermektedir.
Bu veri kümesi, 284,807 işlemden 492'sinin dolandırıcılık olduğu iki gün içinde gerçekleşen işlemleri sunar. Veri kümesi oldukça dengesizdir, pozitif sınıf (dolandırıcılık) tüm işlemlerin %0,172'sini oluşturur. 

Yalnızca bir PCA dönüşümünün sonucu olan sayısal girdi değişkenlerini içerir. Ne yazık ki, gizlilik sorunları nedeniyle, orijinal özellikleri ve verilerle ilgili daha fazla arka plan bilgisi sağlayamıyoruz. Özellikler V1, V2, … V28, PCA ile elde edilen temel bileşenlerdir, PCA ile dönüştürülmeyen tek özellikler 'Zaman' ve 'Miktar'dır. 'Zaman' özelliği, her işlem ile veri kümesindeki ilk işlem arasında geçen saniyeleri içerir.

Veri Seti: https://www.kaggle.com/mlg-ulb/creditcardfraud

# Kullandığımız Algoritmalar 

## Support Vector Machine

“Destek Vektör Makinesi” (SVM), sınıflandırma veya regresyon problemleri için kullanılabilen denetimli bir makine öğrenmesi algoritmasıdır. Bununla birlikte, çoğunlukla sınıflandırma problemlerinde kullanılır. Bu algoritmada, her bir veri maddesini belirli bir koordinatın değeri olan her özelliğin değeri ile birlikte n-boyutlu boşluğa (burada n sahip olduğunuz özelliklerin sayısı) bir nokta olarak çizilir. Ardından, iki sınıftan oldukça iyi ayrım yapan hiper-düzlemi bularak sınıflandırma gerçekleştirilir.
 
![image](https://user-images.githubusercontent.com/71029563/144699452-10fca995-6451-4a52-8eea-4567ce21398c.png)

## Random Forest

Random Forest algoritması denetimli bir sınıflandırma algoritmasıdır. (Supervised classification algorithm). İsminden de anlayacağımız üzere basit olarak algoritma rastgele olarak bir orman yaratıyor. Algoritmadaki ağaç sayısı ve elde edebileceği sonuç arasında doğrudan bir ilişki bulunmaktadır. Ağaç sayısı arttıkça kesin bir sonuç elde ederiz.

![image](https://user-images.githubusercontent.com/71029563/144699526-f0df5689-ca00-4fbb-8e48-b9b65d0d5a79.png)
![image](https://user-images.githubusercontent.com/71029563/144699532-0d2fff68-fd04-4e67-8d71-1bd0620e20c4.png)

## Oversampling

Sınıflandırma yaparken, sınıfların eşit dağılmadığı, yani her sınıf için yaklaşık olarak aynı sayıda verinin olmadığı veri kümesidir. Mesela, ikili sınıflandırma (binary classification) durumunda, 500 verinin olduğu bir veri kümesindeki 40 verinin azınlık sınıfa (Sınıf-1), 460 verinin ise diğer sınıfa (Sınıf-0) ait olması durumudur.

![image](https://user-images.githubusercontent.com/71029563/144699586-609850a1-dcac-4bac-b2c3-0b95be401ce2.png)
![image](https://user-images.githubusercontent.com/71029563/144699607-cc79ac8f-6dc5-4da3-92f5-5e1c90c2c5fa.png)

## Downsampling

Dijital sinyal işlemede, altörnekleme, sıkıştırma ve desimasyon, çok oranlı bir dijital sinyal işleme sisteminde yeniden örnekleme süreciyle ilişkili terimlerdir. Hem altörnekleme hem de karartma, sıkıştırma ile eşanlamlı olabilir veya bant genişliği azaltma (filtreleme) ve örnekleme hızı azaltma sürecinin tamamını tanımlayabilirler.

![image](https://user-images.githubusercontent.com/71029563/144699688-16bd0af7-3a58-4373-8ecd-3a8919d46dc3.png)
![image](https://user-images.githubusercontent.com/71029563/144699693-5d43a0ef-b2d8-495c-b3ac-ba00007ff65b.png)


