'use client';

import { useRouter, useSearchParams } from "next/navigation";
import { useState, Suspense } from "react";

function ComplimentsContent() {
  const searchParams = useSearchParams();
  const person = searchParams.get("person");
  const router = useRouter();

  function onBackClick() {
    router.push("/");
  }

  const [data, setData] = useState();
  const [loading, setLoading] = useState(false);

  function fetchCompliment() {
    setLoading(true);
    fetch(`http://127.0.0.1:8080/api/compliment/?person=${person}`)
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(---primary-font)]">
      <div className="absolute top-0 w-full z-0">
        <svg viewBox="0 0 100 20" xmlns="http://www.w3.org/2000/svg" fill="none" className="w-full">
          <path
            d="M0 10 Q 25 0, 50 10 T 100 10"
            stroke="#b6a0d3"
            strokeWidth="1"
            fill="transparent"
          />
        </svg>
      </div>
      <main className="flex flex-col gap-[32px] row-start-2 items-center">
        <div className="mb-2 tracking-[-.01em] text-center">
          Yay it&apos;s {person}! Click on the button below to generate a custom built compliment!
        </div>
        <div className="flex gap-4 items-center flex-col sm:flex-row">
            <button
              type='button'
              onClick={() => fetchCompliment()}
              disabled={loading}
              className="relative"
            >
              {loading ? "Loading..." : "New Compliment"}
            </button>
        </div>
        <div className="flex text-center">
           {data ? data["compliment"] : ''}
        </div>
      </main>
      <footer className="row-start-3 flex gap-[24px] flex-wrap text-center">
        <div
          className="underline hover:underline-offset-4 cursor-pointer"
          onClick={() => onBackClick()}
        >
          Back 
        </div>
      </footer>
    </div>
  );
}

export default function Compliments() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <ComplimentsContent />
    </Suspense>
  );
}
