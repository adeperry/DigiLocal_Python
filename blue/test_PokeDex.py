import PokeDex

def test_btn_rnd():
    # simple test click "Random Data" changes name and number
    prev_number = PokeDex.pokemon_number
    prev_name = PokeDex.pokemon_name

    PokeDex.btn_rnd_info.invoke() #  click "Random Data"
    assert PokeDex.pokemon_name != prev_name, "name should have changed"
    assert PokeDex.pokemon_number != prev_number, "number should have changed"

def test_btn_info():
    pokemons={
        ('bulbasaur', 1),
        ('zeraora',  807)
    }

    for pokemon in pokemons:
        key=pokemon[0]
        val=pokemon[1]
        for i in pokemon:
            # seperate test insert name and then number
            PokeDex.txt_pokemon_number.insert(0, i)
            PokeDex.btn_get_info.invoke() # click "Get Data"
            assert PokeDex.pokemon_name == key, "expected name "+key+" but got "+PokeDex.pokemon_name
            assert PokeDex.pokemon_number == val, "expected number "+val+" but got "+PokeDex.pokemon_number