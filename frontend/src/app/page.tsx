'use client';

import React from 'react';
import PortfolioForm from './components/PortfolioForm';
import FrontierChart from './components/FrontierChart';

export default function HomePage() {
  return (
    <div className="space-y-8 max-w-5xl mx-auto">
      <PortfolioForm />
      <FrontierChart />
    </div>
  );
}
