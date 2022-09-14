# pico-keyboard-automate

The code in this repository is for Automating Scripts/manual actions on computers using Raspberry Pi Picos, and serves as a boilerplate and collection of existing and scripts produced.

## Setting Up & Using the scripts

## To create/modify a script

1. Look for an existing script in `/scripts` that is close to what you need to do, or if not, use one of the boilerplate templates
2. Copy your chosen starting file into `/scripts`, and give it a descriptive filename related to its purpose, e.g. `setup_hp_bios.py` or `test_lectern.py`
3. Edit your file to perform the functions necessary. Please add comments in your file to describe what it does to help others and yourself in the future!
4. To copy it to the Pico, see the below sections

## To setup a new Pico from scratch

Before we can load Python code onto the Pico we must give the RP2040 a bootloader in .UF2 format, so that it knows how to run Python files.

1. Download the latest stable release of __CircuitPython 7.x__ from their Pico download page at this link, in .UF2 format: (https://circuitpython.org/board/raspberry_pi_pico/)
2. Plug the Pico into your PC over USB, and drag the .UF2 (extracting from zip if needed) to the attached mass storage device, which should have a drive label of `RP2` or similar.
3. Once the file has finished copying the Pico will automatically reboot with the new bootloader, and should reattach with the drive label `CIRCUITPY`.
4. Copy the `lib` folder in `/base` of this repository to the root directory of the Pico, this contains the USB input library.

## To copy a script to a CircuitPython Pico

1. Copy your desired script to the `/base` directory of this repository.
2. If a `code.py` already exists in `/base`, delete it.
3. Rename your copied script to `code.py`
4. Copy the `code.py` file from the `/base` directory to the root directory of the Pico
5. Your file structure on the Pico (ignoring the default files) should look like this:
    ```bash
    CIRCUITPY\                 # Pico root folder
        code.py                # default script     
        lib\                   # ┐
            adafruit_hid\      # ├ library files
                <.mpy files>   # ┘
    ```
6. Plug your Pico into a device and watch the magic happen!
    > Note: If testing on your own PC, can be a good idea to open Notepad and focus your input inside it before connecting the Pico!



## Resources

- [Adafruit CircuitPython HID Library Reference](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)
- [Adafruit CircuitPython HID Library Releases](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases) (use ~hid-7.x-mpy~.zip)
- [CircuitPython Pico Download page](https://circuitpython.org/board/raspberry_pi_pico/)