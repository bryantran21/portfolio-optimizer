
import React, { useState } from "react";
import {
  ScatterChart,
  Scatter,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

interface PortfolioPoint {
  return: number;
  volatility: number;
}

interface PortfolioFrontierProps {
  data: PortfolioPoint[]; // efficient frontier points
}

const PortfolioFrontier: React.FC<PortfolioFrontierProps> = ({ data }) => {
  if (!data || data.length === 0) return <p>No data available</p>;

  const minVolPoint = data[0];
  const maxSharpePoint = data[data.length - 1];

  return (
    <ResponsiveContainer width="100%" height={400}>
      <ScatterChart margin={{ top: 20, right: 30, bottom: 20, left: 20 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis
          dataKey="volatility"
          type="number"
          name="Volatility"
          unit=""
          domain={["dataMin", "dataMax"]}
        />
        <YAxis
          dataKey="return"
          type="number"
          name="Return"
          unit=""
          domain={["dataMin", "dataMax"]}
        />
        <Tooltip
          cursor={{ strokeDasharray: "3 3" }}
          formatter={(value: number, name: string) => [
            value.toFixed(3),
            name,
          ]}
        />
        <Legend />

        {/* Efficient frontier line */}
        <Line
          type="monotone"
          data={data}
          dataKey="return"
          stroke="#8884d8"
          dot={false}
        />

        {/* Min volatility point */}
        <Scatter name="Min Volatility" data={[minVolPoint]} fill="#82ca9d" />

        {/* Max Sharpe point */}
        <Scatter name="Max Sharpe" data={[maxSharpePoint]} fill="#ff7300" />
      </ScatterChart>
    </ResponsiveContainer>
  );
};

export default PortfolioFrontier;
