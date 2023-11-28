export default function SelectLanguage({ changeLanguage, language ,languageDictionary}) {
    return (
        <>
        <span>{languageDictionary.idioma}</span>
        <select name="language" id="language" onChange={e => changeLanguage(e.target.value)} value={language}>
            <option value="es">ES</option>
            <option value="en">EN</option>
            <option value="pt">PT</option>
        </select>
        </>
    )
}
