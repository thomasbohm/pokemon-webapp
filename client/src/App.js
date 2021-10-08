import { useState } from 'react';
import axios from 'axios';
import logo from './resources/logo.svg';
import './resources/styles.css';

const SERVER_URL = 'https://6e7a-2001-a61-3462-cd01-45ca-9792-c7d2-cdad.ngrok.io'
const POKEMON_URL = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/'

export default function App() {
  const [pokemon, setPokemon] = useState();

  async function submit(event) {
    const img = event.target.files[0];
    if (!img) {
      return;
    }

    const formData = new FormData();
    formData.append(
      "file",
      img,
      img.name
    );

    try {
      const res = await axios.post(SERVER_URL, formData);
      setPokemon(res.data)
    } catch (e) {
      console.log('Error: ' + e);
    }
  }

  return (
    <div className="app">
        <img className="logo" src={logo} alt="Pokemon Logo" />
        <div className="info">
          {pokemon ?
            <div>
              <h2>That's {pokemon.en.toUpperCase()}</h2>
              <img className="pokemon-img" src={POKEMON_URL + `${pokemon.id}`.padStart(3, '0') + '.png'} alt={pokemon.en}/>
            </div> :
            <div>
              <h2>Pokemon Classifier</h2>
              <p>Select an Image of a Pokemon and see how it's called.</p>
            </div>
          }         
        </div>
        <input className="inputfile" type="file" id="file" onChange={submit} accept=".jpg,.jpeg,.png,.svg" />
        <label className="inputLabel" htmlFor="file">SELECT IMAGE</label>
    </div>
  );
}
