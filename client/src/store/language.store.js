import { create } from 'zustand'
import { ESPAÑOL, INGLES, PORTUGUES } from '../language/language'



export const useLanguageStore = create((set) => ({
  language: localStorage.getItem("language") || (window.navigator.language).slice(0, 2),
  languageDictionary:
    (localStorage.getItem("language") || (window.navigator.language).slice(0, 2)) === "en" ?
      INGLES :
      (localStorage.getItem("language") || (window.navigator.language).slice(0, 2)) === "pt" ?
        PORTUGUES :
        ESPAÑOL,
  changeLanguage: (language) => {
    if (language === "en") {
      localStorage.setItem("language", "en");
      set({ languageDictionary: INGLES, language: language })
      return
    }
    if (language === "pt") {
      localStorage.setItem("language", "pt");
      set({ languageDictionary: PORTUGUES, language: language })
      return
    }
    else {
      localStorage.setItem("language", "es");
      set({ languageDictionary: ESPAÑOL, language: language })
      return
    }
  }
}))