import customtkinter
from googletrans import Translator
from ctk_scrollable_dropdown import *


def translate():
    translator = Translator()
    input_text = input_field.get('1.0', 'end-1c')
    translated_text = translator.translate(input_text, src=input_lang_combobox.get(), dest=output_lang_combobox.get())
    output_field.delete('0.0', 'end')
    output_field.insert('0.0', translated_text.text)


languages = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Aymara', 'Azerbaijani',
             'Bambara', 'Basque', 'Belarusian', 'Bengali', 'Bhojpuri', 'Bosnian', 'Bulgarian', 'Catalan',
             'Cebuano', 'Chichewa', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Corsican', 'Croatian',
             'Czech', 'Danish', 'Dhivehi', 'Dogri', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Ewe',
             'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Guarani',
             'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian',
             'Icelandic', 'Igbo', 'Ilocano', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese',
             'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Konkani', 'Korean', 'Krio', 'Kurdish (Kurmanji)',
             'Kurdish (Sorani)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lingala', 'Lithuanian', 'Luganda',
             'Luxembourgish', 'Macedonian', 'Maithili', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori',
             'Marathi', 'Meiteilon (Manipuri)', 'Mizo', 'Mongolian', 'Myanmar (Burmese)', 'Nepali', 'Norwegian',
             'Odia (Oriya)', 'Oromo', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua',
             'Romanian', 'Russian', 'Samoan', 'Sanskrit', 'Scots Gaelic', 'Sepedi', 'Serbian', 'Sesotho',
             'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese',
             'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tigrinya', 'Tsonga',
             'Turkish', 'Turkmen', 'Twi', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh',
             'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']

root = customtkinter.CTk()
root.title('Translator')
root.geometry('1000x680')
root.resizable(False, False)
root.config(background='#065042')

input_frame = customtkinter.CTkFrame(root,
                                     border_width=0,
                                     corner_radius=0,
                                     height=320,
                                     fg_color='#065042')
input_frame.pack(anchor='center', fill='both')

input_field = customtkinter.CTkTextbox(input_frame,
                                       border_width=0,
                                       corner_radius=0,
                                       height=300,
                                       fg_color='#00755e',
                                       font=('Calibri', 16))
input_field.pack(padx=10, pady=10, fill='both')

select_frame = customtkinter.CTkFrame(root,
                                      border_width=0,
                                      corner_radius=0,
                                      height=50,
                                      fg_color='#065042')
select_frame.pack(anchor='center', fill='y')

input_label = customtkinter.CTkLabel(select_frame, text='From:', fg_color='#065042')
input_label.pack(side='left', anchor='center', padx=10, pady=5)


input_lang_combobox = customtkinter.CTkComboBox(select_frame,
                                                border_width=0,
                                                corner_radius=0,
                                                width=150,
                                                height=30,
                                                fg_color='#00755e',
                                                button_color='#00755e',
                                                state='readonly')
input_lang_combobox.pack(side='left', anchor='center', padx=10)

CTkScrollableDropdown(input_lang_combobox,
                      frame_border_width=2,
                      fg_color='#00755e',
                      hover_color='#065042',
                      values=languages,
                      justify='left',
                      button_color='transparent')

output_label = customtkinter.CTkLabel(select_frame, text='To:', fg_color='#065042')
output_label.pack(side='left', anchor='center', padx=10)

output_lang_combobox = customtkinter.CTkComboBox(select_frame,
                                                 border_width=0,
                                                 corner_radius=0,
                                                 width=150,
                                                 height=30,
                                                 fg_color='#00755e',
                                                 button_color='#00755e',
                                                 state='readonly')
output_lang_combobox.pack(side='left', anchor='center', padx=10)

CTkScrollableDropdown(output_lang_combobox,
                      frame_border_width=2,
                      fg_color='#00755e',
                      hover_color='#065042',
                      values=languages,
                      justify='left',
                      button_color='transparent')

translate_button = customtkinter.CTkButton(select_frame,
                                           fg_color='#00755e',
                                           hover_color='#056955',
                                           text='Translate',
                                           command=translate)
translate_button.pack(side='left', anchor='center', padx=10)

output_frame = customtkinter.CTkFrame(root,
                                      border_width=0,
                                      corner_radius=0,
                                      height=320,
                                      fg_color='#065042')
output_frame.pack(anchor='center', fill='both')

output_field = customtkinter.CTkTextbox(output_frame,
                                        border_width=0,
                                        corner_radius=0,
                                        height=300,
                                        fg_color='#00755e',
                                        font=('Calibri', 16))
output_field.pack(padx=10, pady=10, fill='both')

root.mainloop()
