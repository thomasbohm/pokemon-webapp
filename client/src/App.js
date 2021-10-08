import { Suspense, useState } from 'react';
import axios from 'axios';
import i18n from 'i18next';
import { initReactI18next, useTranslation } from 'react-i18next';
import logo from './resources/logo.svg';
import germany from './resources/germany.png';
import uk from './resources/uk.png';
import './resources/styles.css';

const SERVER_URL = 'https://6e7a-2001-a61-3462-cd01-45ca-9792-c7d2-cdad.ngrok.io';
const POKEMON_URL = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/';

const translationsEn = {
  title: "Pokemon Classifier",
  info: "Select an Image of a Pokemon and see how it's called.",
  select: "SELECT IMAGE",
  thats: "That's ",
};
const translationsDe = {
  title: "Pokemon Klassifizierer",
  info: "Nimm ein Foto von einem Pokemon, und schau wie es heißt.",
  select: "FOTO WÄHLEN",
  thats: "Das ist ",
};

i18n
  .use(initReactI18next)
  .init({
    resources: {
      en: { translation: translationsEn },
      de: { translation: translationsDe },
    },
    lng: "en",
    fallbackLng: "en",
    interpolation: { escapeValue: false },
  });

export default function App() {
  const { t } = useTranslation();
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
            {pokemon ?
              <div>
                <h2>{t('thats') + i18n.language === 'en' ? pokemon.en.toUpperCase() : pokemon.de.toUpperCase()}</h2>
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
