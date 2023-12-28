import style from "./Nav.module.css";
// import SearchBar from "../SearchBar/SearchBar";
import { Link } from "react-router-dom";
// import { useLocation } from "react-router-dom";
// import { ROUTES } from "../../helpers/routesPath";

export default function Navbar(props) {
  // const location = useLocation();

  return (
    <>
      <nav className={style.navBar}>
        <div className={style.leftContainer}>
          Find Junior Jobs
          {/* <div className={style.links}>
            <Link to={ROUTES.HOME} className={style.navSpan}>
              <span>HOME</span>
            </Link>
            <Link to={ROUTES.NEW_BREED} className={style.navSpan}>
              <span>CREATE NEW BREED</span>
            </Link>
          </div> */}
        </div>

        {/* <div className={style.rightContainer}>
          {location.pathname === ROUTES.HOME ? <SearchBar /> : null}{" "}
        </div> */}
      </nav>
    </>
  );
}
