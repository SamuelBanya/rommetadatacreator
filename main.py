import platform

def directoryWizard:
    # Values include 'Windows', 'Darwin', and 'Linux'
    os_name = platform.system()

    print("I see you are using ${os_name} for your operating system");
    console_decision = input("What specific console are you scanning ROM metadata for?\n\nChoices include: '1': NES, '2': SNES, '3': Gameboy");
    directory_location = input("Within the current directory where you are running this script, what is the name of the folder you want to scan for ROM's?");

    pass;

def obtainFileInfo:
    # Determine matching file names:
    # Determine hashes of matching files
    # Determine sizes of matching files
    pass;

def __main__():
    directoryWizard();
    obtainFileInfo();

if __name__ == '__main__':
    main();
