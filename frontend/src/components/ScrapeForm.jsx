export default function ScrapeForm({ setData, setLoading }) {
  const submit = async (e) => {
    e.preventDefault();
    const url = e.target.url.value;
    setLoading(true);

    const res = await fetch("/scrape", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const json = await res.json();
    setData(json.result);
    setLoading(false);
  };

  return (
    <form onSubmit={submit}>
      <input name="url" placeholder="https://example.com" size="50" />
      <button>Scrape</button>
    </form>
  );
}
