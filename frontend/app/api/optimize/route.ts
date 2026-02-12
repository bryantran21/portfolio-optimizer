import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { tickers } = await req.json();

  const response = await fetch(
    `http://127.0.0.1:8000/optimize/frontier?tickers=${tickers.join(",")}`
  );

  const data = await response.json();

  return NextResponse.json(data);
}