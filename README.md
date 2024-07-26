# Projenin Tanımı

Twitter,Facebook, Ekşi Sözlük ve Letterboxd gibi sosyal medya platformlarından veri çekmeyi ve bu verileri görselleştirmeyi içerir. Kullanıcı, belirli bir sosyal medya platformunda belirli bir kullanıcı adına göre veya herhangi bir anahtar kelimeye göre veri analizi yapabilir.
Projenin ana hedefi, farklı sosyal medya platformlarından veri çekme işlemlerini koordine etmek ve bu verileri kullanıcı dostu bir arayüzde görselleştirmektir. Bu amaçla, Flask kullanılarak bir web uygulaması oluşturuldu, Selenium kullanılarak web scraping işlemleri gerçekleştirildi ve elde edilen veriler Matplotlib kullanılarak görselleştirilmiştir.SMTP protokolü kullanılarak oluşturulan raporlar kullanıcıya e-mail olarak gönderilmesi de amaçlanmıştır

# Projenin Aşamaları

1. **Veri Toplama**: Bu aşamada, projenin amacına uygun olarak sosyal medya platformlarından (Twitter, Facebook, Ekşi Sözlük, Letterboxd vb.) veri toplanır. Bu veriler genellikle kullanıcılar veya belirli anahtar kelimeler üzerinden elde edilir.

2. **Veri Analizi ve Ayıklama**: Toplanan veriler analiz edilir ve gerektiğinde temizlenir. Analiz sürecinde, belirli algoritmalar ve yöntemler kullanılarak verilerin içeriği anlamlandırılır. Önemli bilgiler çıkarılır.

3. **Verileri Görselleştirme ve Raporlama**: Analiz edilen veriler görselleştirilir. Bu aşamada grafikler kullanılarak verilerin daha anlaşılır ve etkili bir şekilde sunulması sağlanır.

4. **Oluşturulan Raporu E-mail Yoluyla Gönderme**: Son aşamada, görselleştirme ve raporlama sürecinde oluşturulan raporlar, belirlenen alıcıya e-mail yoluyla gönderilir. Bu adım otomatikleştirilir ve raporların düzenli olarak paylaşılmasını sağlar.

# Projede Kullanılan Teknolojiler

- **Flask**: Web uygulamasının backend geliştirmesinde kullanılmıştır.
- **Selenium**: Sosyal medya platformlarından veri çekmek için web scraping işlemlerinde kullanılmıştır.
- **Matplotlib**: Veri görselleştirme işlemlerinde kullanılmıştır.
- **SMTP Protokolü**: Raporların e-posta ile gönderiminde kullanılmıştır.

# Anasayfa
![Anasayfa](https://github.com/emirhandev/Sosyal-Medya-Analiz-Araci/blob/main/images/1.png)<br/>
Kullanıcı Ana Menüden istediği Sosyal Medya Platformunu seçebilir:
- Twitter
- Facebook
- Ekşi Sözlük
- Letterboxd

# Arama Bölümü
![Arama Bölümü](https://github.com/emirhandev/Sosyal-Medya-Analiz-Araci/blob/main/images/2.png)<br/>
Sosyal medya platformunu seçtikten sonra, kullanıcı adına göre ya da spesifik bir kelimeye göre arama yapabilir.

# Grafik Görselleştirme Bölümü
![Grafik Görselleştirme Bölümü](https://github.com/emirhandev/Sosyal-Medya-Analiz-Araci/blob/main/images/3.png)<br/>
Kullanıcı bir süre içeriklerin taranmasını ve ayıklanmasını beklemektedir. Kirli veri ayrıştırıldıktan sonra kelimelerin kullanımına göre grafikleştirme işlemi yapılır.

# E-posta Gönderme Bölümü
![E-posta Gönderme Bölümü](https://github.com/emirhandev/Sosyal-Medya-Analiz-Araci/blob/main/images/4.png)<br/>
Oluşturulan rapor kullanıcının seçtiği mail adresine gönderilir.

![E-posta Gönderme Bölümü](https://github.com/emirhandev/Sosyal-Medya-Analiz-Araci/blob/main/images/5.png)<br/>

# Proje Akış Diyagramı
![Proje Akış Diyagramı](https://github.com/emirhandev/Sosyal-Medya-Analiz-Araci/blob/main/images/6.png)<br/>
