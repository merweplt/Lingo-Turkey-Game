# 🇹🇷 Lingo Turkey Game: Dağıtık Sistem Temelleri Uygulaması

Bu proje, popüler kelime tahmin oyunu Lingo'nun Türkçe versiyonudur ve **Temel Yazılım Mimarisi Bilgimi** göstermektedir.

---

## 🎯 Projenin Amacı ve Teknik Öğrenim Çıktıları

Bu uygulamanın temel amacı, bir yazılım projesini **Server-Client (Sunucu-İstemci) mimarisi** kullanarak tasarlama ve bu iki bileşen arasındaki güvenilir iletişimi yönetme yeteneğimi sergilemektir.

### 🛠️ Kritik Teknik Kazanımlar:

* **Dağıtık Mimari Tasarımı:** Uygulamayı iki ayrı, bağımsız bileşene (Sunucu ve İstemci) ayırarak, modern dağıtık sistemlerin temel mantığını uygulamalı olarak öğrendim.
* **Ağ İletişimi (Socket Programming):** Sunucu ile istemcinin, farklı makinelerde olabilme potansiyeliyle, **TCP/IP** üzerinden **socket'ler** aracılığıyla nasıl veri alışverişi yapacağını kodladım.
* **Durum Yönetimi (Server State Management):** Sunucunun, hangi kelimenin tahmin edildiği, kaç hak kaldığı gibi oyunun kritik durumunu yönetme ve bunu istemciye tutarlı bir şekilde yansıtma prensiplerini uyguladım.
* **Kod Okunabilirliği ve Modülerlik:** Python dilinin sağladığı temiz yapıyı kullanarak, hem sunucu hem de istemci tarafında anlaşılır ve bakımı kolay kod blokları oluşturdum.

---

## 💻 Kullanılan Teknolojiler

| Teknoloji | Rolü ve Uygulamadaki Kullanım Şekli |
| :--- | :--- |
| **Python** | Projenin tamamında kullanılan temel programlama dili. |
| **Sockets** | Sunucu ve istemci arasında anlık, iki yönlü (bidirectional) iletişimi sağlamak için kullanıldı. |
| **Server-Client Mimarisi** | Uygulamanın temel yapısı. İstemci sadece kullanıcı arayüzünü yönetirken, oyun mantığı (iş zekası) tamamen sunucuda tutulmuştur. |
| **Dosya İşleme (I/O)** | Sunucunun, oyunda kullanılacak kelime listesini bir dosyadan okuma yeteneği (gerektiğinde kelime dağarcığını dinamik olarak yönetme esnekliği). |

---

## 🚀 Sonuç

Bu proje, sadece bir oyun değil; aynı zamanda Python ile **temel network programlama ve modüler yazılım tasarımı** yeteneklerimi gösteren somut bir referanstır.

*(Bu, staj başvurusu amacıyla teknik yetkinlikleri öne çıkarmak için yapılan 11 Aralık 2025 tarihli düzenlemedir.)*
