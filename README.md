# Classification of Music Genres from the Given Music

## 👨‍👧‍👧 สมาชิกภายในกลุ่ม
- 6310400941 จิรัชญา ผ่านพินิจ
- 6310401041 ธิติ ทวีสิน
- 6310403974 ณัฐดนัย ตันวาณิชกุล

## ⚙️ วิธีการใช้งาน
- สำหรับการฝึกโมเดลที่ใช้ข้อมูล MFCC ให้รันไฟล์ `/mfcc_model.ipynb`
- สำหรับการฝึกโมเดลที่ใช้ข้อมูล chroma feature ให้รันไฟล์ `/chroma_model.ipynb`

ก่อนการเริ่มรันไฟล์ `ipynb` ให้ดาวน์โหลดไฟล์ทั้งหมดจาก[ลิงก์นี้](https://drive.google.com/drive/folders/1_nA2P2ftalzBpe9k74xFVpytbTzaHcbv?usp=sharing)มาใส่ไว้ที่ไดเรกทอรี `/music_data/` ก่อน จากนั้นให้ทำการกำหนด root ของโปรเจกต์ภายในไฟล์ `ipynb` ภายใต้หัวข้อ **Defining Project Root**

## 📦 Resource ของโครงงาน
- [ลิงก์ไฟล์เพลง .wav และ ข้อมูลเพลงที่แปลงอยู่ในรูป chroma feature และ mfcc แล้วทำการจัดเก็บในรูป .npy (มีทั้งหมด 21 คลาส และขนาดของ matrix คือ (12,1000) และ (40,1000) ตามลำดับ)](https://drive.google.com/drive/folders/1ELZ49c3ArRA8uJ18U9WSkVPEltu5YN1q?usp=share_link)
- [ข้อมูลเพลงที่แปลงอยู่ในรูป chroma feature และ mfcc แล้วทำการจัดเก็บในรูป .npy (ในข้อมูลนี้ได้ทำการปรับแก้ไขคลาสจาก 21 เหลือ 18 และปรับขนาดของ matrix ให้เหลือ (12,640) และ (20,640) ตามลำดับ)](https://drive.google.com/drive/folders/1_nA2P2ftalzBpe9k74xFVpytbTzaHcbv?usp=sharing)
- [test กับข้อมูลจริง](https://drive.google.com/drive/folders/1BymvXXnngmKvUgmGh4MJzTJeVccp2W5g?usp=sharing)
- [ลิงก์ code สร้างข้อมูล](https://github.com/Natdadai/create-data-spotify.git)
