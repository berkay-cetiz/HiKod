import numpy as np

sayilar = np.array([1, 2, 3, 4, 5], dtype=int)

boyut = sayilar.ndim
eleman_sayisi = sayilar.size

print("Array Boyutu:", boyut)
print("Eleman Sayısı:", eleman_sayisi)



array_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)

boyut_2d = array_2d.ndim
eleman_sayisi_2d = array_2d.size

satir_sayisi_2d, sutun_sayisi_2d = array_2d.shape


print("2D Array Boyutu:", boyut_2d)
print("2D Eleman Sayısı:", eleman_sayisi_2d)
print("2D Satır Sayısı:", satir_sayisi_2d)
print("2D Sütun Sayısı:", sutun_sayisi_2d)




array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=int)

boyut_3d = array_3d.ndim
eleman_sayisi_3d = array_3d.size

boyutlar_3d = array_3d.shape

print("3D Array Boyutu:", boyut_3d)
print("3D Eleman Sayısı:", eleman_sayisi_3d)
print("3D Boyutlar:", boyutlar_3d)



print(array_2d[0, 1])
print(array_2d[:, 1])
print(array_2d[1, :])
print(array_2d[0:2, 1:3])


print(array_3d[0, 1, 1])
print(array_3d[:, 0, :])
print(array_3d[1, :, 0])




sifir_array = np.zeros((2, 3), dtype=int)
bir_array = np.ones((2, 3), dtype=int)

birlesik_satir = np.vstack((sifir_array, bir_array))
birlesik_sutun = np.hstack((sifir_array, bir_array))


print("Sıfır Array:")
print(sifir_array)

print("Bir Array:")
print(bir_array)

print("Satır Bazında Birleştirme:")
print(birlesik_satir)

print("Sütun Bazında Birleştirme:")
print(birlesik_sutun)
