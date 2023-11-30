import style from "./Home.module.css"
import { useLanguageStore } from '../../store/language.store'
import { Link } from "react-router-dom"
import Pepe from "./homeComponents/ImgCarousel/ImgCarousel"

export default function Home() {
    const {languageDictionary} = useLanguageStore()
    return (
        <>
            <h1>{languageDictionary.saludo}</h1>
            <Link to="/login">Login</Link>
            <Pepe/>
        </>
    )
}
