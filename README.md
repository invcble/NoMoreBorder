# NoMoreBorder

NoMoreBorder is a utility designed to enhance your multitasking experience by enabling any windowed application to run in a fullscreen borderless mode without changing the screen resolution. This software is perfect for certain scenarios where applications don't have a dedicated full-screen borderless mode and running it fullscreen would mess up with dual screen behaviours.

> ⭐ If you like NoMoreBorder, leaving a star would mean a lot! It helps support the project and keeps it growing. Thank you! ⭐

## Screenshots

### Application Interface

Here's how NoMoreBorder user-friendly interface looks in action, courtesy of [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).

![UI](https://github.com/invcble/NoMoreBorder/blob/e769aa3f8fe05a1d76d47f29bc3367636d7eeb11/pictures/UI.png)

### Before and After

These screenshots demonstrate the effect of NoMoreBorder on a sample application, showing both the original windowed mode and the seamless fullscreen experience after applying NoMoreBorder.

#### Before Applying NoMoreBorder

![From](https://github.com/invcble/NoMoreBorder/blob/e769aa3f8fe05a1d76d47f29bc3367636d7eeb11/pictures/From.png)

#### After Applying NoMoreBorder

![To](https://github.com/invcble/NoMoreBorder/blob/e769aa3f8fe05a1d76d47f29bc3367636d7eeb11/pictures/To.png)

#### After Applying NoMoreBorder with custom resolution

![Custom](https://github.com/invcble/NoMoreBorder/blob/e769aa3f8fe05a1d76d47f29bc3367636d7eeb11/pictures/Custom.png)

## Features

1. **Borderless Fullscreen**: Make any windowed application run in fullscreen mode without the traditional window borders, providing an immersive experience without altering the screen resolution.
2. **Custom Resolution**: Have a big screen and an old game made for small screens and low resolutions where windowed mode is too small but fullscreen is so big you barely read the dialog? Now you can also set a custom resolution.
3. **Multiple Monitor Support**: Ability to select which monitor you want the window to be on.
4. **Reversible Action**: Easily revert any changes made to the window, restoring the original windowed mode with borders.
5. **Session Memory**: NoMoreBorder remembers which applications were set to borderless mode, automatically reapplying these settings in future sessions. It's done through a configuration file, ensuring a seamless experience even after restarting the software or your computer.
6. **Dark Mode**: Includes a built-in dark mode, allowing for an on-the-fly theme switch to reduce eye strain during late-night sessions.
7. **Start with Windows**: Now offers the option to auto start with your system, to save you a few clicks!

## **Getting Started**

### Option 1. Download stand-alone exe

Just download the `NoMoreBorder.exe` from [releases](https://github.com/invcble/NoMoreBorder/releases), and run it as it is. No need to setup dependencies, everything is included in this binary executable.

> **Note**: For the best experience, it's recommended to run NoMoreBorder with administrative privileges. This ensures that the application can properly interact with other software windows on your system.

### or, Option 2. Run as a script / Compile your own exe

You can run it as a python script or compile your own exe, I used pyinstaller. Ensure you have Python installed on your system along with the necessary packages: `customtkinter`, `pywin32`, `pyinstaller`, `screeninfo`, `pystray`, `win11toast`, and `pillow`. These can be installed using pip:

```bash
pip install -r requirements.txt
```

### Running NoMoreBorder

To run NoMoreBorder, simply execute the Python script from your terminal or command prompt:

```bash
python main.py
```
To compile, simply put this command in your terminal or command prompt:

```bash
pyinstaller NoMoreBorder.spec
```

You will find the exe in dist folder in parent directory.

## Configuration

NoMoreBorder automatically saves your settings to a `settings.json` file located in the `Documents/NoMoreBorder` directory. This file includes the list of applications set to borderless mode and the selected theme, ensuring your preferences are maintained across sessions.

## Contributions

Contributions to NoMoreBorder are welcome! Whether it's feature enhancements, bug fixes, or documentation improvements, feel free to fork the repository and submit a pull request.

## License

NoMoreBorder is open-source software licensed under the MIT License. See the LICENSE file for more details.
