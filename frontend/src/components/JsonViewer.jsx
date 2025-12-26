export default function JsonViewer({ data }) {
  return (
    <pre style={{ background: "#eee", padding: 10 }}>
      {JSON.stringify(data, null, 2)}
    </pre>
  );
}
