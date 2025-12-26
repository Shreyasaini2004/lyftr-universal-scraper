import JsonViewer from "./JsonViewer";

export default function SectionsView({ data }) {
  const download = () => {
    const blob = new Blob([JSON.stringify(data, null, 2)], {
      type: "application/json"
    });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "scrape.json";
    a.click();
  };

  return (
    <>
      <button onClick={download}>Download JSON</button>
      {data.sections.map((s) => (
        <details key={s.id}>
          <summary>{s.label}</summary>
          <JsonViewer data={s} />
        </details>
      ))}
    </>
  );
}
