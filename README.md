# Study-Kasus-6-Muh.Agustyon

## file json
jadi, ini adalah file json nya, diawali dengan 2 data mahasiswa terlebih dahulu

<img width="597" height="335" alt="image" src="https://github.com/user-attachments/assets/aada4d68-ace3-4cdc-af86-bcb0c02ed6b9" />

## penjelasan kode

lanjut, setelah membuat file json nya, saya membuat program pythonnya
pertama, saya mengimport library yang saya perlukan, yaitu tentu saja json karena untuk menghubungkan program nya denga file json tersebut, dan prettytable agar outputnya rapi

<img width="350" height="77" alt="image" src="https://github.com/user-attachments/assets/213673bf-7632-439b-8800-d0525d28cc93" />

lanjut membuat kode untuk membaca file json nya

<img width="466" height="61" alt="image" src="https://github.com/user-attachments/assets/915f1c2d-997f-4a5b-b1e7-4cd4d55122b0" />

lanjut, saya membuat function untuk menampilkan nilai dari mahasiswa, saya menggunakan prettytable disini agar rapi

<img width="668" height="132" alt="image" src="https://github.com/user-attachments/assets/1cd03a7d-c232-4122-be33-5c719e283d6c" />

lalu saya membuat function untuk menambahkan data nya, dengan menggunakan append

<img width="398" height="162" alt="image" src="https://github.com/user-attachments/assets/4a30d7df-5012-4d70-83fd-e40bc25df37e" />

lanjut, saya membuat function untuk menyimpannya ke dalam file json nya

<img width="497" height="87" alt="image" src="https://github.com/user-attachments/assets/fbe9c89b-cc61-4b6a-ba6d-a887bc1ce173" />

lanjut, saya membuat function lagi, yang ini untuk menginput nilainya, saya menggunakan isdigit untuk melakukan pengecekan apakah nilai yang di input itu angka atau bukan dan karena ini isdigit, jadi hanya bisa bilangan bulat, dan juga saya membatasi nilai hanya pada 0-100, jika kurang dari 0 atau 100 maka akan muncvul output ""
"Nilai harus antara 0 sampai 100!"

<img width="442" height="208" alt="image" src="https://github.com/user-attachments/assets/c299fd30-cbe0-41de-ab4c-9fb9ef979f15" />

terakhir, saya membuat looping disini, untuk membuat menu, nah menu disini ada 3, 
1. yang pertama adalah memnu melihat nilainya, jadi memanggiol kembali function  tampilkan_data
2. yang kedua adalah menu untuk menginput nilainya, jafi memanggil 3 function disini, yaitu input_nilai untuk menginput nilainya, lalu tambah_data untuk menammbahkan datanya ke file json, terakhir simpan_file untuk menyimpan datanya ke file json agar tersimpan permanen
3. yang terakhir adalah menu untuk keluar dari program
<img width="580" height="403" alt="image" src="https://github.com/user-attachments/assets/5859a8e1-b9b2-418d-99ff-bd449d75e2e3" />

## penjelasan output

berikut output jika baru merunning program:

<img width="317" height="107" alt="image" src="https://github.com/user-attachments/assets/49fc7af4-4423-4919-aef4-57ab6cada848" />

ini output jika memilih 1:

<img width="557" height="172" alt="image" src="https://github.com/user-attachments/assets/8e333e65-435d-4573-8a80-6470fcf7ed59" />

ini output jika memilih 2:

<img width="367" height="262" alt="image" src="https://github.com/user-attachments/assets/bcc22c86-b6b2-4906-b2bc-541574ccb1a6" />

ini output jika memilih 3:

<img width="503" height="137" alt="image" src="https://github.com/user-attachments/assets/f62f0b6e-251e-42c3-a41e-f37d6edb3985" />

## data tersimpan
<img width="577" height="463" alt="image" src="https://github.com/user-attachments/assets/ba7ba9c3-7466-4b3b-b06e-e0951ef67215" />

