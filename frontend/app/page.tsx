"use client";

import { useState } from "react";
import dynamic from "next/dynamic";

const PortfolioFrontier = dynamic(
  () => import("./components/PortfolioFrontier"),
  { ssr: false }
);

interface PortfolioPoint {
  return: number;
  volatility: number;
}

export default function Page() {
  const [etfs, setEtfs] = useState("");
  const [data, setData] = useState<PortfolioPoint[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch("/api/optimize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tickers: etfs.split(",").map((t) => t.trim()) }),
      });

      if (!response.ok) throw new Error("Failed to fetch optimization");

      const result = await response.json();
      setData(result); // assume backend returns array of { return, volatility }
    } catch (err) {
      console.error(err);
      alert("Error fetching portfolio optimization");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main style={{ padding: "2rem" }}>
      <h1>Portfolio Optimizer</h1>

      <form onSubmit={handleSubmit} style={{ marginBottom: "2rem" }}>
        <label>
          Enter ETFs (comma-separated):
          <input
            type="text"
            value={etfs}
            onChange={(e) => setEtfs(e.target.value)}
            placeholder="SPY, VTI, QQQ"
            style={{ marginLeft: "1rem", padding: "0.5rem", width: "300px" }}
          />
        </label>
        <button
          type="submit"
          style={{ marginLeft: "1rem", padding: "0.5rem 1rem" }}
          disabled={loading}
        >
          {loading ? "Optimizing..." : "Optimize"}
        </button>
      </form>

      {data.length >= 2 ? (
        <PortfolioFrontier data={data} />
      ) : (
        <p>Enter ETFs and submit to see optimized portfolio</p>
      )}
    </main>
  );
}
