from fa_console import fa_input
import random

def play_game():
    
    secret_number = random.randint(1, 100)   
    max_attempts = 5                         
    attempts = 0                        
    won = False                             

    print("=" * 45)
    print(" بازی حدس عدد... ")
    print("=" * 45)
    print("من یک عدد بین ۱ تا ۱۰۰ انتخاب کردم.")
    print("تو ۵ فرصت داری تا آن را حدس بزنی. موفق باشی!")

    while attempts < max_attempts:
      
        print(f"تلاش {attempts + 1} از {max_attempts}")
        print(f"جان باقی‌مانده: {max_attempts - attempts}")

        user_input = fa_input("عدد حدس‌زده‌ات را وارد کن: ").strip()

       
        guess = int(user_input)

        
        if guess < 1 or guess > 100:
            print(" عدد باید بین ۱ تا ۱۰۰ باشد! دوباره تلاش کن.")
            continue  

        attempts += 1

        if guess == secret_number:
            won = True
            print(f" آفرین! عدد مخفی {secret_number} بود.")
            break

        diff = abs(guess - secret_number)   

        if diff <= 5:
            proximity = " خیلی نزدیکی!"
        elif diff <= 15:
            proximity = " نزدیکی، ولی هنوز فاصله داری!"
        else:
            proximity = " خیلی دوری!"

        if guess < secret_number:
            direction = " بزرگ‌تر وارد کن"
        else:
            direction = " کوچک‌تر وارد کن"

        print(f"{proximity} | {direction}\n")

    print("-" * 45)

    if won:
        
        if attempts == 1:
            rank = " نمونه‌ای!"
        elif attempts == 2:
            rank = " بسیار خوبی!"
        elif attempts == 3:
            rank = " خوب"
        elif attempts == 4:
            rank = " قبول"
        else: 
            rank = " با شانس بردی!"

        print(f"رتبه تو: {rank}")
        print(f"تعداد تلاش‌هایت: {attempts}")
    else:
        
        print(" متأسفانه باختی! فرصت‌هایت تمام شد.")
        print(f"عدد مخفی این دور: {secret_number}")

    print("-" * 45)


def main():
    
    while True:
        play_game()

        answer = fa_input("آیا می‌خواهی دوباره بازی کنی؟ (y/n): ").strip().lower()

        if answer in ("y", "yes", "بله", "آره", "ب"):
            print(" شروع یک بازی جدید...")
            continue  
        else:
            print("خداحافظ ")
            break
if __name__ == "__main__":
    main()