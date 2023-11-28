import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Header from "./components/header/Header";
import Home from "./pages/home/Home"
import Login from "./pages/login/Login.jsx";

function App() {
  return (
      <BrowserRouter>
      <Header/>
        <Routes>
          <Route path="*" element={<Navigate replace to='/' />} />
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </BrowserRouter>
  )
}

export default App
