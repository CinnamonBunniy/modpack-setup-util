import webview
import os
import pathlib

def custom_logic(window):
    # window.toggle_fullscreen()
    window.evaluate_js('alert("Nice one brother")')

def main():
    # Define the path to the index.html file
    html_file = pathlib.Path(__file__).resolve().parent / "web_content/index.html"
    # check that the file exists
    if not html_file.is_file():
        raise FileNotFoundError(f"HTML file not found: {html_file}")
    #

    # Create a Pywebview window loading the HTML file
    window = webview.create_window("Hello World", url=f"file://{html_file}")
    webview.settings["OPEN_DEVTOOLS_IN_DEBUG"] = False
    webview.start(custom_logic, window, debug=True)

if __name__ == '__main__':
    main()