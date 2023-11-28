import style from "./Header.module.css"
import { useLanguageStore } from '../../store/language.store'
import SelectLanguage from "./headerComponents/SelectLanguage"

export default function Header() {
    const { language, languageDictionary, changeLanguage } = useLanguageStore()
  return (
    <SelectLanguage changeLanguage={changeLanguage} language={language} languageDictionary={languageDictionary}/>
  )
}
