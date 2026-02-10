import './globals.css';
import React, { ReactNode } from 'react';

export const metadata = {
  title: 'Portfolio Optimizer',
  description: 'Interactive portfolio optimization dashboard',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-gray-900 font-sans">
        <header className="bg-white shadow-md p-4">
          <h1 className="text-xl font-bold">Portfolio Optimizer</h1>
        </header>
        <main className="p-4">{children}</main>
      </body>
    </html>
  );
}
