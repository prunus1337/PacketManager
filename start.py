import time
import requests
import traceback
import os

def download_file(url, filename):
    print("Устанавливаем...")
    try:
        if not os.path.exists("downloaded"):
            os.makedirs("downloaded")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open("downloaded/" + filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except Exception as e:
        traceback.print_exc(e)
        print("Произошла ошибка при загрузке файла.. обратитесь к разработчику!")
        input("\nНажмите Enter для выхода...")
        main()
    finally:
        print("Установка завершена! Посмотрите папку downloaded!")
        input("\nНажмите Enter для выхода...")
        main()
    
clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def main():
    clear_console()
    print("""
  _____           _        _     __  __                                   
 |  __ \         | |      | |   |  \/  |                                  
 | |__) |_ _  ___| | _____| |_  | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 |  ___/ _` |/ __| |/ / _ \ __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |  | (_| | (__|   <  __/ |_  | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|   \__,_|\___|_|\_\___|\__| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                           __/ |          
                                                          |___/           

""")
    print("""
Выберите цифру для выбора категории:
1. Соц. сети
2. Драйвера
3. Прочее
4. Credits
          

Сделано с ❤️ by @prunus1337 / @weever
""")
    choice = input("> ")
    try:

        if choice == "4":
            print("\nCredits: @prunus1337, @Snaky1a\nВы можете найти их на гитхабе")
            input("\nНажмите Enter для выхода...")
            main()
        
        if choice == "1":
            print("\nВыберите соц. сети которые хотите установить:\n1. Viber\n2. Discord\n3. Telegram\n4. Whatsapp\n5. Выход")
            choice_soc = input("\n> ")
            if choice_soc == "1":
                download_file("https://download.cdn.viber.com/desktop/windows/ViberSetup.exe", "ViberSetup.exe")
            elif choice_soc == "2":
                download_file("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "DiscordInstaller.exe")
            elif choice_soc == "3":
                download_file("https://telegram.org/dl/desktop/win64", "TelegramSetup.exe")
            elif choice_soc == "4":
                print("Пока что нету.. (А зачем я этот бред сюда пишу? лан ты тупой бро...)")
                input("\nНажмите Enter для выхода...")
                main()
            elif choice_soc == "5":
                main()
            else:
                print("\nВыберите цифру и напишите сюда. Пример: 1")

        elif choice == "2":
            print("\nВыберите драйвера которые хотите установить:\n1. Microsoft Visual C++ Redist\n2. .NET framework\n3. Выход")
            choice_drivers = input("\n> ")
            if choice_drivers == "1":
                download_file("https://aka.ms/vs/16/release/vc_redist.x64.exe", "vc_redist.x64.exe")
            elif choice_drivers == "2":
                download_file("https://go.microsoft.com/fwlink/?linkid=2088632", "net_framework.exe")
            elif choice_drivers == "3":
                main()
            else:
                print("\nВыберите цифру и напишите сюда. Пример: 1")

        elif choice == "3":
            print("\nВыберите прочие приложения которые хотите установить:\n1. Spotify (SpotX)\n2. VMWare Workstation\n3. Epicgames\n4. 64Gram\n5. Steam\n6. Vencord\n7. Custom Windows Shutdown\n8. Выход")
            choice_other = input("\n> ")
            if choice_other == "1":
                download_file("https://github.com/SpotX-Official/SpotX/releases/download/1.8/Install_New_theme.bat", "SpotX-Spotify.bat")
            elif choice_other == "2":
                download_file("https://www.vmware.com/go/getworkstation-win", "vmware-workstation-setup.exe")
            elif choice_other == "3":
                download_file("https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi?trackingId=764168bb6408463089eb547a75658b8d", "EpicInstaller.exe")
            elif choice_other == "4":
                download_file("https://www.64gram.com/download", "64gram.exe")
            elif choice_other == "5":
                download_file("https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe", "SteamSetup.exe")
            elif choice_other == "6":
                download_file("https://github.com/Vencord/Installer/releases/latest/download/VencordInstaller.exe", "VencordInstaller.exe")
            elif choice_other == "7":
                download_file("https://github.com/prunus1337/CustomWindowsShutdown/releases/download/v0.2/CustomWindowsShutdown.exe", "CustomWindowsShutdown.exe")
            elif choice_other == "8":
                main()
            else:
                print("\nВыберите цифру и напишите сюда. Пример: 1")

    except Exception as e:
        traceback.print_exc(e)

# if choice == "1":
#     rich.print("Installing discord...")
#     download_file("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "DiscordInstaller.exe")
# elif choice == "2":
#     print("Installing Telegram Setup...")
#     download_file("https://telegram.org/dl/desktop/win64", "TelegramSetup.exe")
# elif choice == "3":
#     print("Installing 64Gram...")
#     download_file("https://github.com/TDesktop-x64/tdesktop/releases/download/v1.1.4/64Gram-setup-x64.1.1.4.exe", "64Gram-setup-x64.1.1.4.exe")
# elif choice == "4":
#     print("Installing Steam Setup")
#     download_file("https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe", "SteamSetup.exe")
# elif choice == "5":
#     print("Installing Spotify (with spotx)...")
#     download_file("https://github.com/SpotX-Official/SpotX/releases/download/1.8/Install_New_theme.bat", "Install_New_theme.bat")
# elif choice == "6":
#     print("Installing Spotify official...")
#     download_file("https://download.scdn.co/SpotifySetup.exe", "SpotifySetup.exe")
# elif choice == "7":
#     print("Installing Vencord (for discord)...")
#     download_file("https://github.com/Vencord/Installer/releases/latest/download/VencordInstaller.exe", "VencordInstaller.exe")
# elif choice == "8":
#     print("Installing Microsoft Visual C++ Redist...")
#     download_file("https://aka.ms/vs/16/release/vc_redist.x64.exe", "vc_redist.x64.exe")
# elif choice == "9":
#     print("Installing .NET framework...")
#     download_file("https://go.microsoft.com/fwlink/?linkid=2088632", "framework.exe")
# elif choice == "10":
#     print("Installing VMWare Workstation...")
#     download_file("https://www.vmware.com/go/getworkstation-win", "vmware-workstation-setup.exe")
# elif choice == "11":
#     print("Installing Epicgames...")
#     download_file("https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi?trackingId=764168bb6408463089eb547a75658b8d", "EpicInstaller.exe")


if __name__ == "__main__":
    main()
