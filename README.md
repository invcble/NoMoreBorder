# NoMoreBorder

NoMoreBorder is a utility designed to enhance your multitasking experience by enabling any windowed application to run in a fullscreen borderless mode without changing the screen resolution. This software is perfect for users who desire a seamless and immersive experience across various applications, from gaming to productivity tools.

## Screenshots

### Application Interface

Here's how NoMoreBorder looks in action, demonstrating its straightforward and user-friendly interface.

![NoMoreBorder Interface](https://github.com/invcble/NoMoreBorder/blob/d990bf0b75254ed770062a5642e4c034e57d59d4/pic/NoMoreBorder.png)

### Before and After

These screenshots demonstrate the effect of NoMoreBorder on a sample application, showing both the original windowed mode and the seamless fullscreen experience after applying NoMoreBorder.

#### Before Applying NoMoreBorder

![Before NoMoreBorder](https://github.com/invcble/NoMoreBorder/blob/d990bf0b75254ed770062a5642e4c034e57d59d4/pic/From.png)

#### After Applying NoMoreBorder

![After NoMoreBorder](https://github.com/invcble/NoMoreBorder/blob/d990bf0b75254ed770062a5642e4c034e57d59d4/pic/To.png)

## Features

- **Borderless Fullscreen**: Make any windowed application run in fullscreen mode without the traditional window borders, providing an immersive experience without altering the screen resolution.
- **Reversible Action**: Easily revert any changes made to the window, restoring the original windowed mode with borders.
- **Session Memory**: NoMoreBorder remembers which applications were set to borderless mode, automatically reapplying these settings in future sessions. This persistence is achieved through a configuration file, ensuring a seamless experience even after restarting the software or your computer.
- **Dark Mode**: Includes a built-in dark mode, allowing for an on-the-fly theme switch to reduce eye strain during late-night sessions.

## Getting Started

Just download the NoMoreBorder.exe from releases, run it as it is.

### Compiling your own

You can compile your own exe, I used pyinstaller. Ensure you have Python installed on your system along with the necessary packages: `customtkinter`, `pywin32`, and `pyinstaller`. These can be installed using pip:

```bash
pip install customtkinter pywin32 pyinstaller
```

### Running NoMoreBorder

To run NoMoreBorder, simply execute the Python script from your terminal or command prompt:

```bash
python main.py
```

The application interface will appear, allowing you to select which windowed applications to make borderless or revert to their original state.

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
