import platform, hashlib;
from pathlib import Path;
import os;
from humanfriendly import format_size;
import json;
from pyfiglet import Figlet;
from tabulate import tabulate;

def directoryWizard():
    directory_wizard_dict = {'os_name': '', 'console_decision': '', 'directory_location': '', 'console_path': ''};
    # Values include 'Windows', 'Darwin', and 'Linux'
    os_name = platform.system()
    print(f"CHECK: os_name: {os_name}");
    print(f"I see you are using {os_name} for your operating system");
    console_decision = input("\n\nWhat specific console are you scanning ROM metadata for?\n\nChoices include: '1': NES, '2': SNES, '3': Gameboy\n");
    directory_location = input("\n\nWithin the current directory where you are running this script, what is the name of the folder you want to scan for ROM's?\n");

    directory_wizard_dict['os_name'] = os_name;

    if console_decision == '1':
        directory_wizard_dict['console_decision'] = 'NES';

    elif console_decision == '2':
        directory_wizard_dict['console_decision'] = 'SNES';

    elif console_decision == '3':
        directory_wizard_dict['console_decision'] = 'Gameboy';

    directory_wizard_dict['directory_location'] = directory_location;

    # Current file directory:
    current_directory = Path.cwd();
    console_path = Path.joinpath(current_directory, directory_wizard_dict['directory_location']);

    directory_wizard_dict['console_path'] = console_path;

    return directory_wizard_dict;

def obtainFileInfo(directory_wizard_dict):
    roms_list = [];
    # Determine matching file names:
    # Determine hashes of matching files
    # Determine sizes of matching files

    # Cycle through each of the files present:
    for child in directory_wizard_dict['console_path'].iterdir():
        if (child.suffix != '.json'):
            # Build out a dictionary for each game:
            # Grab file name:
            file_name = child.stem;
            file_extension = child.suffix;

            # Grab file hash:
            with open(child, "rb") as f:
                digest = hashlib.file_digest(f, "md5");

            file_hash = digest.hexdigest();
            stat_info = os.stat(child);
            file_size = format_size(stat_info.st_size);

            # Grab file size:
            # Place these properties into a single game dictionary:
            current_game_dict = { "name_of_game": "", "file_extension": "", "platform": "",
                                "file_hash": "", "file_size": "" };

            current_game_dict['name_of_game'] = file_name;
            current_game_dict['file_extension'] = file_extension;
            current_game_dict['platform'] = directory_wizard_dict['console_decision'];
            current_game_dict['file_hash'] = file_hash;
            current_game_dict['file_size'] = file_size;

            # Add it to the running JSON list:
            roms_list.append(current_game_dict);

    # Return the JSON file:
    return roms_list;

def writeJsonToFile(directory_wizard_dict, roms_list):
    output_file_path = directory_wizard_dict['console_path'] / f"{directory_wizard_dict['console_decision']}.json";

    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(roms_list, f, indent=2);

def successMessage():
    f = Figlet(font='slant');
    print(f.renderText("SUCCESS"));

def promptForTable(directory_wizard_dict, roms_list):
    user_decision = input("\n\nWould you like to see your ROM data results in tabular form before you go? ('y' or 'n'): \n");
    if user_decision.lower() == "y":
        f = Figlet(font='slant');
        print("\n\n");
        print(f.renderText(f"{directory_wizard_dict['console_decision']} ROM Datatable"));
        print(tabulate(roms_list, headers="keys", tablefmt="fancy_grid"));

    return user_decision;

def goodbyeMessage():
    f = Figlet(font='slant');
    print(f.renderText("GOODBYE"));

def main():
    directory_wizard_dict = directoryWizard();
    roms_list = obtainFileInfo(directory_wizard_dict);
    writeJsonToFile(directory_wizard_dict, roms_list);
    successMessage();
    user_decision = promptForTable(directory_wizard_dict, roms_list);
    if user_decision.lower() == "n":
        goodbyeMessage();

if __name__ == '__main__':
    main();
