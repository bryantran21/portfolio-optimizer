'use client';

import React, { useState } from 'react';

export default function PortfolioForm() {
  const [tickers, setTickers] = useState('');
  const [period, setPeriod] = useState('1y');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Fetch data for:', tickers, period);
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md space-y-4">
      <div>
        <label className="block font-semibold mb-1">Tickers (comma-separated)</label>
        <input
          type="text"
          value={tickers}
          onChange={(e) => setTickers(e.target.value)}
          className="w-full border p-2 rounded"
        />
      </div>
      <div>
        <label className="block font-semibold mb-1">Period</label>
        <select
          value={period}
          onChange={(e) => setPeriod(e.target.value)}
          className="w-full border p-2 rounded"
        >
          <option value="1y">1 Year</option>
          <option value="6mo">6 Months</option>
          <option value="1mo">1 Month</option>
        </select>
      </div>
      <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
        Fetch Prices
      </button>
    </form>
  );
}
