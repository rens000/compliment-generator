'use client';

import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  function onButtonClick(person: string) {
    router.push(`/compliments?person=${person}`);
  }

  const people = ["mom", "dad", "davis", "kai"];

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
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <div className="mb-2 tracking-[-.01em]">
          Hi there!  Please select your name below.
        </div>
        <div className="flex gap-4 items-center flex-col sm:flex-row">
          {people.map((person) => (
            <button
              key={person}
              type='button'
              onClick={() => onButtonClick(person)}
            >
              { person }
            </button>
          ))}
        </div>
      </main>
      <footer className="row-start-3 flex gap-[24px] flex-wrap items-center justify-center">
        <a
          className="underline hover:underline-offset-4"
          href="https://github.com/rens000/compliment-generator"
          target="_blank"
          rel="noopener noreferrer"
        >
          Source Code
        </a>
      </footer>
    </div>
  );
}
