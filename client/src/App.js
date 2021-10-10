import { Suspense, useState } from 'react';
import axios from 'axios';
import { useTranslation } from 'react-i18next';
import SyncLoader from "react-spinners/SyncLoader";

import logo from './resources/logo.svg';
import germany from './resources/germany.png';
import uk from './resources/uk.png';
import './resources/styles.css';
import './i18n'

const SERVER_URL = 'https://fd13-93-104-178-254.ngrok.io';
const POKEMON_URL = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/';

export default function App() {
  const { t, i18n } = useTranslation();
  const [pokemon, setPokemon] = useState();
  const [loading, setLoading] = useState(false);

  async function submit(event) {
    setLoading(true);
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
    } finally {
      setLoading(false);
    }
  }

  function changeLanguage() {
    if (i18n.language === 'en') {
      i18n.changeLanguage('de');
    } else {
      i18n.changeLanguage('en');
    }
  }

  return (
    <Suspense fallback="Loading...">
      <div className="app">
          <img className="logo" src={logo} alt="Pokemon Logo" />
            <div className="info">
              {loading ? <SyncLoader color='#FFDE00' size={20}/> :
                pokemon ?
                  <div>
                    <h2>{t('thats') + (i18n.language === 'en' ? pokemon.en.toUpperCase() : pokemon.de.toUpperCase())}</h2>
                    <img className="pokemon-img" src={POKEMON_URL + `${pokemon.id}`.padStart(3, '0') + '.png'} alt={pokemon.en}/>
                  </div> :
                  <div>
                    <h2>{t("title")}</h2>
                    <p>{t("info")}</p>
                  </div>
              }         
            </div>
          <input className="inputfile" type="file" id="file" onChange={submit} accept=".jpg,.jpeg,.png,.svg" />
          <label className="inputLabel" htmlFor="file">{t('select')}</label>
          {i18n.language === 'en' ?
            <img className="flag" onClick={changeLanguage} src={uk} alt="uk flag" width="32" height="32" /> :
            <img className="flag" onClick={changeLanguage} src={germany} alt="germany flag" width="32" height="32" />
          }
      </div>
    </Suspense>
  );
}
