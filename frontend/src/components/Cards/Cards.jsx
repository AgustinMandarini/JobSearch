import axios from "axios";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Table from "react-bootstrap/Table";

const URL = process.env.REACT_APP_API_SERVER_URL;

export default function Cards() {
  const [jobs, setJobs] = useState([]);

  const get_jobs = () => {
    axios(URL)
      .then((res) => {
        setJobs(res.data);
      })
      .catch((err) => {
        alert(err);
      });
  };

  useEffect(() => {
    get_jobs();
  }, []);
  return (
    <>
      <Table striped bordered hover variant="dark">
        <thead>
          <tr>
            <th></th>
            <th>Title</th>
            <th>Company</th>
            <th>Location</th>
            <th>Date</th>
            <th>Link</th>
          </tr>
        </thead>
        <tbody>
          {jobs.map((job, i) => (
            <tr key={job.id}>
              <td>{i + 1}.</td>
              <td>{job.title}</td>
              <td>{job.company}</td>
              <td>{job.location}</td>
              <td>{job.date}</td>
              <td>
                <Link to={job.job_url}>{job.job_url.slice(0, 80)}</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </>
  );
}
