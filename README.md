# Python File Organizer

A simple Python application to organize files in a selected folder by type, using a graphical interface built with Tkinter.

## Features

- Organizes files into subfolders by type (Images, Documents, Videos, Music, Archives)
- Easy-to-use GUI for selecting the target folder
- Cross-platform (Windows, macOS, Linux)

## Folder Structure

```
file_organizer/
├── app.py          # Main entry point (run this to start the GUI)
├── gui.py          # Tkinter GUI code
├── organizer.py    # File organization logic
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/file_organizer.git
   cd file_organizer
   ```

2. **Run the application:**

   ```bash
   python app.py
   ```

3. **Use the GUI:**
   - Click "Browse Folder" to select the folder you want to organize.
   - The app will sort files into subfolders by type.

## Customization

- To add more file types or change folder names, edit the `FILE_TYPES` dictionary in `organizer.py`.

## License

MIT License

---

_Created with ❤️ using Python and Tkinter._
