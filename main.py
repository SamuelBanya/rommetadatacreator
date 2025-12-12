import platform

def directoryWizard():
    directory_wizard_dict = {'os_name': '', 'directory_location': ''};
    # Values include 'Windows', 'Darwin', and 'Linux'
    os_name = platform.system()
    print(f"CHECK: os_name: {os_name}");
    print(f"I see you are using {os_name} for your operating system");
    console_decision = input("\n\nWhat specific console are you scanning ROM metadata for?\n\nChoices include: '1': NES, '2': SNES, '3': Gameboy\n");
    directory_location = input("\n\nWithin the current directory where you are running this script, what is the name of the folder you want to scan for ROM's?\n");
    print("\n\nTESTING: user's choice for directory_location: " + directory_location);

    directory_wizard_dict['os_name'] = os_name;
    directory_wizard_dict['directory_location'] = directory_location;

    return directory_wizard_dict;

def obtainFileInfo():
    # Determine matching file names:
    # Determine hashes of matching files
    # Determine sizes of matching files
    pass;

def main():
    directory_wizard_dic = directoryWizard();
    print("TEST WITHIN main(): ");
    print("directoryWizard: ", directoryWizard);
    print("directoryWizard['os_name']: ", directory_wizard_dic['os_name']);
    print("directoryWizard['directory_location']: ", directory_wizard_dic['directory_location']);
    obtainFileInfo();

if __name__ == '__main__':
    main();
