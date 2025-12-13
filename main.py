import platform
from pathlib import Path

def directoryWizard():
    directory_wizard_dict = {'os_name': '', console_decision: '', 'directory_location': ''};
    # Values include 'Windows', 'Darwin', and 'Linux'
    os_name = platform.system()
    print(f"CHECK: os_name: {os_name}");
    print(f"I see you are using {os_name} for your operating system");
    console_decision = input("\n\nWhat specific console are you scanning ROM metadata for?\n\nChoices include: '1': NES, '2': SNES, '3': Gameboy\n");
    directory_location = input("\n\nWithin the current directory where you are running this script, what is the name of the folder you want to scan for ROM's?\n");
    print("\n\nTESTING: user's choice for directory_location: " + directory_location);

    directory_wizard_dict['os_name'] = os_name;
    if console_decision == 1:
        directory_wizard_dict['console_decision'] = 'NES';

    elif console_decision == 2:
        directory_wizard_dict['console_decision'] = 'SNES';

    elif console_decision == 3:
        directory_wizard_dict['console_decision'] = 'Gameboy';

    directory_wizard_dict['directory_location'] = directory_location;

    return directory_wizard_dict;

def obtainFileInfo(dir_dict):
    # Determine matching file names:
    # Determine hashes of matching files
    # Determine sizes of matching files
    # NES:
    # Check for '.nes' files
    if dir_dict['console_decision'] == 'NES':
        # Current file directory:
        current_directory = Path.cwd();
        nes_path = Path.joinpath(current_directory, dir_dict['directory_location']);
        for child in nes_path.iterdir():
            print('child: ', child);

    # SNES
    # Check for '.SMC' or '.SFC' files
    if dir_dict['console_decision'] == 'SNES':
        pass;

    # Gameboy
    # Check for '.gb' files:
    if dir_dict['console_decision'] == 'Gameboy':
        pass;
    pass;

def main():
    dir_dict = directoryWizard();
    obtainFileInfo(dir_dict);

if __name__ == '__main__':
    main();
