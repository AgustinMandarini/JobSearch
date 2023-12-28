import "./App.css";
import { Route, Routes } from "react-router-dom";
import Nav from "./components/Nav/Nav";
import Cards from "./components/Cards/Cards";

function App() {
  return (
    <>
      <Nav />
      <Routes>
        <Route path={""} element={<Cards />}></Route>
      </Routes>
    </>
  );
}

export default App;
