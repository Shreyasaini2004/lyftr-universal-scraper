import { useState } from "react";
import ScrapeForm from "./components/ScrapeForm";
import SectionsView from "./components/SectionsView";

export default function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div style={{ padding: 20 }}>
      <h2>Universal Website Scraper</h2>
      <ScrapeForm setData={setData} setLoading={setLoading} />
      {loading && <p>Scraping...</p>}
      {data && <SectionsView data={data} />}
    </div>
  );
}
