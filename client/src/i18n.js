import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

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

export default i18n;