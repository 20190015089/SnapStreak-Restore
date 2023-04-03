import os, time, sys, inflect, json, urllib.request
import undetected_chromedriver as uc
from datetime import date
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from captcha_bypass import mp32wav, transcribe_audio_to_text
from undetected_chromedriver import ChromeOptions

#wow
def writer(text, color=Fore.WHITE):
    os.system('cls')
    for char in text:
        sys.stdout.write(color + char + Fore.RESET)
        sys.stdout.flush()
        time.sleep(0.02)
    return " "

#date
today = date.today()
d = today.strftime("%d/%m/%Y")

#browser options
options = ChromeOptions()
options.add_argument('--headless')

PROXY_input = input(writer("Do you want to use proxy? Y/N", color=Fore.WHITE))
if (PROXY_input == 'Y') or (PROXY_input == 'y'):
    PROXY = input(writer('Write it in the correct format', color=Fore.RED))
    options.add_argument('--proxy-server=socks5://' + PROXY)
else:
    pass

#threading
while True:
    try:
        threading = int(input(writer("How fast you want it to be? 1-10/faster-slower", color=Fore.WHITE)))
        break
    except ValueError:
        print("")
if threading > 0:
    pass
else:
    thrading = 1

#json
if os.path.isfile('info.json'):
    saved_info = input(writer("Looks like it's not the first time using the tool. Do you want to continue with the previous info? Y/N", color=Fore.GREEN))
    if (saved_info == "Y") or (saved_info == "y"):
        with open("info.json", "r") as f:
            data = json.load(f)
        username = data["username"]
        email = data["email"]
        phone = data["phone"]
        device = data["device"]
        friend_usernames = data["friend_usernames"]
    else:
        username = input(writer("Enter your username:", color=Fore.CYAN))
        email = input(writer("Enter your email:", color=Fore.BLUE))
        phone = input(writer("Enter your phone number with +xxx:", color=Fore.CYAN))
        device = input(writer("Enter your device: ex. iPhone 11", color=Fore.BLUE))

        friend_usernames = []
        while True:
            try:
                how_many = int(input(writer("How many do you want to restore your streak with?", color=Fore.WHITE)))
                break
            except ValueError:
                print("")
        for i in range(1, how_many+1):
            p = inflect.engine()
            ordinal = p.ordinal(i)

            friend_username = input(writer(f"Enter the {ordinal} friend's username: ", color=Fore.BLUE))
            friend_usernames.append(friend_username)
        
        data = {
        "username": username,
        "email": email,
        "phone": phone,
        "device": device,
        "friend_usernames": friend_usernames
        }
        with open("info.json", "w") as f:
            json.dump(data, f, indent=4)
else:
    username = input(writer("Enter your username:", color=Fore.CYAN))
    email = input(writer("Enter your email:", color=Fore.BLUE))
    phone = input(writer("Enter your phone number with +xxx:", color=Fore.CYAN))
    device = input(writer("Enter your device: ex. iPhone 11", color=Fore.BLUE))

    friend_usernames = []
    while True:
        try:
            how_many = int(input(writer("How many do you want to restore your streak with?", color=Fore.WHITE)))
            break
        except ValueError:
            print("")
    for i in range(1, how_many+1):
        p = inflect.engine()
        ordinal = p.ordinal(i)

        friend_username = input(writer(f"Enter the {ordinal} friend's username: ", color=Fore.BLUE))
        friend_usernames.append(friend_username)
    
    data = {
    "username": username,
    "email": email,
    "phone": phone,
    "device": device,
    "friend_usernames": friend_usernames
    }
    with open("info.json", "w") as f:
        json.dump(data, f, indent=4)

#nothing
driver = uc.Chrome(options=options)
os.system('cls')
for i in range(5, 0, -1):
    print(Fore.RED + f"I will start in {i} seconds" + Fore.RESET)
    time.sleep(1)
    os.system('cls')

#ok
for friend_username in friend_usernames:

    driver.get("https://help.snapchat.com/hc/en-us/requests/new?ticket_form_id=149423&selectedAnswers=5695496404336640,5731111685324800")

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cookie-modal-container"]/div/section/div/section/div[2]/div/div/div/div[3]/button[1]'))
        ).click()
    except:
        pass

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "request_custom_fields_24281229"))
        ).send_keys(f"{username}")
        time.sleep(threading)
        driver.find_element(By.ID, "request_custom_fields_24335325").send_keys(f"{email}")
        time.sleep(threading)
        driver.find_element(By.ID, "request_custom_fields_24369716").send_keys(f"{phone}")
        time.sleep(threading)
        driver.find_element(By.ID, "request_custom_fields_24369726").send_keys(f"{device}")
        time.sleep(threading)
        driver.find_element(By.ID, "request_custom_fields_24369736").send_keys(f"{friend_username}")
        time.sleep(threading)
        driver.find_element(By.ID, "request_custom_fields_24326423").send_keys(f"{d}")
        time.sleep(threading)
        driver.find_element(By.ID, "request_description").send_keys("Return My Streak Back")
        time.sleep(threading)
        driver.find_element(By.NAME, "commit").click()

        frame_src = 'https://www.google.com/recaptcha/api2/bframe?hl=en&v=NZrMWHVy58-S9gVvad9HVGxk&k=6Ldt4CkUAAAAAJuBNvKkEcx7OcZFLfrn9cMkrXR8'
        captcha_frame = WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, f'//iframe[@src="{frame_src}"]'))
        )

        frame_src = 'https://www.google.com/recaptcha/api2/bframe?hl=en&v=NZrMWHVy58-S9gVvad9HVGxk&k=6Ldt4CkUAAAAAJuBNvKkEcx7OcZFLfrn9cMkrXR8'
        captcha_frame = WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, f'//iframe[@src="{frame_src}"]'))
        )

        error_flag = False
        while not error_flag:
            try:
                audio_button = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-audio-button"]'))
                )
                audio_button.click()

                downloadable = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="rc-audio"]/div[7]/a'))
                )
                source = downloadable.get_attribute('href')
                urllib.request.urlretrieve(source, "captcha.mp3")

                while True:
                    if os.path.isfile('captcha.mp3'):
                        mp32wav("captcha.mp3")
                        break

                while True:
                    if os.path.isfile('captcha.wav'):
                        solved_captcha = transcribe_audio_to_text("captcha.wav")
                        break

                #rc-audiochallenge-error-message

                response = driver.find_element("id", "audio-response").send_keys(solved_captcha)

                driver.find_element("id", "recaptcha-verify-button").click()

                error_message = driver.find_element(By.CLASS_NAME, "rc-audiochallenge-error-message")
                error_flag = True

            except NoSuchElementException:
                pass

        print(Fore.GREEN + friend_username + Fore.RESET)
        driver.close()

    except:
        print(Fore.RED + friend_username + Fore.RESET)
        driver.quit()