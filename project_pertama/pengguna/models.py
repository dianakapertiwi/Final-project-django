from django.db import models

# Create your models here.

class Pengguna(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class ProdukItem(models.Model):
    PILIHAN_LABEL = ["A", "B"]
    PILIHAN_KATEGORI = ["makanan", "minuman"]
    
    nama_produk = models.CharField(max_length=100)
    harga = models.FloatField()
    harga_diskon = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='product_pics')
    label = models.CharField(choices=PILIHAN_LABEL, max_length=4)
    kategori = models.CharField(choices=PILIHAN_KATEGORI, max_length=2)

class OrderProdukItem(models.Model):
    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    produk_item = models.ForeignKey(ProdukItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    produk_items = models.ManyToManyField(OrderProdukItem)
    tanggal_mulai = models.DateTimeField(auto_now_add=True)
    tanggal_order = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    alamat_pengiriman = models.ForeignKey('AlamatPengiriman', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)

class AlamatPengiriman(models.Model):
    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    alamat_1 = models.CharField(max_length=100)
    alamat_2 = models.CharField(max_length=100)
    negara = models.CharField(max_length=100)
    kode_pos = models.CharField(max_length=20)

class Payment(models.Model):
    user = models.ForeignKey(Pengguna, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    charge_id = models.CharField(max_length=50)
    

