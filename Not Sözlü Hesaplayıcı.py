from typing import Tuple
import random

# Sabitler
MIN_NOT = 0
MAX_NOT = 100
BASARI_SINIRI = 75
GECME_SINIRI = 50

def not_al() -> int:
    """Kullanıcıdan not alır ve geçerli bir sayı olduğunu kontrol eder."""
    while True:
        try:
            not_ = int(input(f"Lütfen bir not giriniz ({MIN_NOT}-{MAX_NOT} arası): "))
            if MIN_NOT <= not_ <= MAX_NOT:
                return not_
            print(f"Lütfen {MIN_NOT} ile {MAX_NOT} arasında bir değer giriniz.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

def notu_degerlendir(not_: int) -> Tuple[str, str, int]:
    """Notu değerlendirir, uygun mesajı ve sözlü notunu döndürür."""
    if not_ >= BASARI_SINIRI:
        return "Başarıyla Geçtin", "😊", random.randint(75, 100)
    elif not_ >= GECME_SINIRI:
        return "Daha iyi olmalısın", "🤔", random.randint(50, 75)
    else:
        return "Kaldın", "😞", random.randint(0, 50)

def ortalama_hesapla(yazili: int, sozlu: int) -> float:
    """Yazılı ve sözlü notlarının ortalamasını hesaplar."""
    return (yazili + sozlu) / 2

def main():
    while True:
        yazili_not = not_al()
        mesaj, emoji, sozlu_not = notu_degerlendir(yazili_not)
        ortalama = ortalama_hesapla(yazili_not, sozlu_not)
        
        print(f"Yazılı Notun: {yazili_not}")
        print(f"Sözlü Notun: {sozlu_not}")
        print(f"Not Ortalaması: {ortalama:.2f}")
        print(f"Değerlendirme: {mesaj} {emoji}")
        
        if input("Başka bir not hesaplamak ister misiniz? (e/h): ").lower() != 'e':
            break

    print("Program sonlandı. İyi günler!")

if __name__ == "__main__":
    main()