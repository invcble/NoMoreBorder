# NoMoreBorder

NoMoreBorder is a utility designed to enhance your multitasking experience by enabling any windowed application to run in a fullscreen borderless mode without changing the screen resolution. This software is perfect for certain scenarios where applications don't have a dedicated full-screen borderless mode and running it fullscreen would mess up with dual screen behaviours.

## Screenshots

### Application Interface

Here's how NoMoreBorder looks in action, demonstrating its straightforward and user-friendly interface.

![Screenshot 2024-07-25 234700](https://github.com/user-attachments/assets/33682870-2d65-4683-bc57-794c06a8746c)

### Before and After

These screenshots demonstrate the effect of NoMoreBorder on a sample application, showing both the original windowed mode and the seamless fullscreen experience after applying NoMoreBorder.

#### Before Applying NoMoreBorder

![2024-07-25_23-53-30](https://github.com/user-attachments/assets/832e5ca1-2fde-45ca-8432-e85a9298f140)

#### After Applying NoMoreBorder

![FTLGame_2024-07-25_23-53-36](https://github.com/user-attachments/assets/cff48b76-fae0-4de8-846c-f48ff7a5b430)

#### After Applying NoMoreBorder with custom resolution

![2024-07-25_23-53-57](https://github.com/user-attachments/assets/b6051378-cd1d-4d05-a332-5d8503e393a8)

## Features

- **Borderless Fullscreen**: Make any windowed application run in fullscreen mode without the traditional window borders, providing an immersive experience without altering the screen resolution.
- **Custom Resolution**: Have a big screen and an old game made for small screens and low resolutions where windowed mode is too small but fullscreen is so big you barely read the dialog? Now you can also set a custom resolution.
- **Multiple Monitor Support**: Ability to select which monitor you want the window to be on.
- **Reversible Action**: Easily revert any changes made to the window, restoring the original windowed mode with borders.
- **Session Memory**: NoMoreBorder remembers which applications were set to borderless mode, automatically reapplying these settings in future sessions. It's done through a configuration file, ensuring a seamless experience even after restarting the software or your computer.
- **Dark Mode**: Includes a built-in dark mode, allowing for an on-the-fly theme switch to reduce eye strain during late-night sessions.

## **Getting Started**

**Just download the `NoMoreBorder.exe` from [releases](https://github.com/invcble/NoMoreBorder/releases), and run it as it is.**

> **Note**: For the best experience, it's recommended to run NoMoreBorder with administrative privileges. This ensures that the application can properly interact with other software windows on your system.

### Compiling your own

You can run it as a python script or compile your own exe, I used pyinstaller. Ensure you have Python installed on your system along with the necessary packages: `customtkinter`, `pywin32`, and `pyinstaller`. These can be installed using pip:

```bash
pip install customtkinter pywin32 pyinstaller screeninfo
```

### Running NoMoreBorder

To run NoMoreBorder, simply execute the Python script from your terminal or command prompt:

```bash
python main.py
```
To compile, simply put this command in your terminal or command prompt:

```bash
pyinstaller --onefile --noconsole main.py
```

You will find the exe in dist folder in parent directory.

## How to Use

1. **Select an Application**: Use the dropdown menu to select an application currently running on your system.
2. **Make Borderless**: Click the "Make it Borderless" button to remove the window borders and expand the application to fill the screen.
3. **Revert Changes**: If you wish to revert the changes and restore the original windowed mode with borders, simply select the application again and click the "Undo Lmao!" button.
4. **Theme Switching**: Use the "Appearance Mode" options at the bottom of the application window to switch between System, Light, and Dark themes.

## Configuration

NoMoreBorder automatically saves your settings to a `settings.json` file located in the same directory as the application. This file includes the list of applications set to borderless mode and the selected theme, ensuring your preferences are maintained across sessions.

## Contributions

Contributions to NoMoreBorder are welcome! Whether it's feature enhancements, bug fixes, or documentation improvements, feel free to fork the repository and submit a pull request.

## License

NoMoreBorder is open-source software licensed under the MIT License. See the LICENSE file for more details.
