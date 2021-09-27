import keyboard
import win32clipboard
import webbrowser


PATH_TO_CHROME = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
SHORTCUT_VAL = 'ctrl+alt+p'

keyboard.add_hotkey(SHORTCUT_VAL, lambda: print('ctrl + alt + p pressed - opening mailinator'))

def on_load():
    print("Does this happen")
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    print(str(data))
    # if this is a mailinator email saved
    if 'mailinator.com' in str(data):
        print("Found!")
        str(data).split('@')[0]
        url = 'https://www.mailinator.com/v4/public/inboxes.jsp?to='+ str(data).split('@')[0]
        webbrowser.register('chrome',
	    None,
	    webbrowser.BackgroundBrowser(PATH_TO_CHROME))
        webbrowser.get('chrome').open(url)
    else:
        print("Not Mailinator email!")


keyboard.add_hotkey(SHORTCUT_VAL, on_load)
keyboard.wait()