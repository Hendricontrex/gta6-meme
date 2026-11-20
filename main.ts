// Entry program for gta6-meme-x-01 ("Post a GTA 6 meme on X").
//
// The judged thing is the X post, not this program. All this file does is hand
// the grader the post's address: it copies POST.json from the repo root into
// the output directory. Nothing else is read, written, or fetched.
//
// The program keeps the competition's constraints: Node 22, standard library
// only, no network, deterministic (the same POST.json in gives the same
// POST.json out, byte for byte).
//
// Local check, mirroring the grader's container paths with scratch folders:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// afterwards out/POST.json holds the same bytes as POST.json.
//
// POST.json must name the real post before submitting: as shipped it holds a
// placeholder address, and the gate refuses a placeholder. Post the meme on X
// first, then put its address in POST.json and submit.

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

function main(): void {
  const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
  const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
  mkdirSync(outputDir, { recursive: true });
  const source = join(botDir, "POST.json");
  const target = join(outputDir, "POST.json");
  try {
    copyFileSync(source, target);
  } catch (error) {
    console.error(`POST.json could not be copied from ${source}: ${(error as Error).message}`);
    process.exit(1);
  }
}

main();
