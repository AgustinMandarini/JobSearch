import style from "./Card.module.css";
import { Link } from "react-router-dom";

export default function Card({ title, url, company, location, date }) {
  return (
    <div className={style.container}>
      <Link to={url}>
        <div className={style.breedName}>
          <h1>{title}</h1>
        </div>
      </Link>
      <div className={style.breedName}>
        <h2>{company}</h2>
      </div>
      <div className={style.descrContainer}>
        <div>Location: {location}</div>
        <div>{date}</div>
      </div>
    </div>
  );
}
