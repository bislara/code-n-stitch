
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import clipboard_get, clipboard_set
from backend import summarize_text
def run_gui():
    large_font = ("Helvetica", 15)
    # define the layout
    layout = [ [sg.Text('Enter text to be summarized here:',font=large_font), sg.Text('', key='_OUTPUT_')],
                [sg.Multiline(do_not_clear=True, key='_IN_',size=(80, 20))],
                [sg.Button('Summarize'),sg.Button('Paste'),sg.Button('Exit'),
                sg.Text('Sentences in Summary: ', font=("Helvetica", 12)), 
                sg.Slider(range=(1,10),default_value=7, orientation='h',key='_SLIDER_')],
                [sg.Text('Summary',font = large_font)],
                [sg.Multiline(size=(80, 8), key='_OUT_',autoscroll = True,disabled=True)],
                [sg.Button('Copy')],
            ]
    # create the window
    window = sg.Window('Python Text Summarization').Layout(layout).Finalize()


    while True:  # Event Loop
        
        event, values = window.Read()
        print(event, values)

        if event is None or event == 'Exit':
            break

        if event == 'Summarize':
            # change the "output" element to be the value of "input" element
            window.Element('_OUT_').Update("Running NLP Algorithm...")
            # call the summarize_text function
            count = values['_SLIDER_']
            summary = summarize_text(values['_IN_'],int(count))
            window.find_element('_OUT_').Update(summary)

        if event == 'Paste':
            text = clipboard_get()
            window.Element('_IN_').Update(text)

        if event == 'Copy':
            text = window.Element('_OUT_').Get()
            clipboard_set(text)

    window.Close()