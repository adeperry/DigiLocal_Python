import tkinter as tk
import requests
import random
import json
from io import BytesIO
from PIL import Image, ImageTk

bg_colour = '#0093d5'
fg_colour = '#4b4d4d'
small_font = ('Arial', 14)
medium_font = ('Arial', 18)
large_font = ('Arial', 30)
max_pokemon_number = 807 # TODO: use api to get max https://pokeapi.co/api/v2/pokemon/808

pokemon_data = dict()
pokemon_number = -1
pokemon_name = '???'

def get_pokemon_data(num):
    r = requests.get('http://pokeapi.co/api/v2/pokemon/'+str(num))
    pokemon_dictionary = r.json()
    if False:
        # DBG
        with open('pokemon_data_'+str(num)+'.json', 'w', encoding='utf8') as json_file: 
            json.dump(pokemon_dictionary, json_file, indent=2) 
    return pokemon_dictionary

def get_pokemon_image(num):
    image_bytes = requests.get(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+
            str(num)+".png")
    data_stream = BytesIO(image_bytes.content)
    pil_image = Image.open(data_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image

def show_pokemon_data(id=None):
    global pokemon_number, pokemon_data, pokemon_data

    if id == None:
        pokemon_number = txt_pokemon_number.get()
    else:
        pokemon_number = id

    try:
        pokemon_data = get_pokemon_data(pokemon_number)
        pokemon_name = pokemon_data['name']
        lbl_name_value.config(text=pokemon_name)
        lbl_number_value.config(text=pokemon_number)

        pokemon_image = get_pokemon_image(pokemon_number)
        lbl_image.config(image = pokemon_image)
        lbl_image.image = pokemon_image
        txt_pokemon_number.delete(0,99)

    except: 
        print('invalid pokemon number: '+str(pokemon_number))

def show_pokemon_data_rnd(): 
    show_pokemon_data(id=random.randint(1, max_pokemon_number+1))

window = tk.Tk()
window.title('PokeDex')

lbl_instructions = tk.Label(window, text='Enter a number between 1 and '+
    str(max_pokemon_number)+': ', font=small_font)
lbl_instructions.pack()

txt_pokemon_number = tk.Entry(window)
txt_pokemon_number.pack()

btn_get_info = tk.Button(window, text='Get Data!', command=show_pokemon_data)
btn_get_info.pack()

### Name

btn_rnd_info = tk.Button(window, text='Random Data!', command=show_pokemon_data_rnd)
btn_rnd_info.pack()

lbl_name_text = tk.Label(window, text='Name: ', font=medium_font, 
    fg=fg_colour, bg=bg_colour)
lbl_name_text.pack()

### Number

lbl_name_value = tk.Label(window, text=pokemon_name, font=large_font, 
    fg=fg_colour, bg=bg_colour)
lbl_name_value.pack()

lbl_number_text = tk.Label(window, text='Number: ', font=medium_font, 
    fg=fg_colour, bg=bg_colour)
lbl_number_text.pack()

lbl_number_value = tk.Label(window, text=str(pokemon_number), font=large_font, 
    fg=fg_colour, bg=bg_colour)
lbl_number_value.pack()

lbl_image = tk.Label(window, bg=bg_colour)
lbl_image.pack()

window.mainloop()


