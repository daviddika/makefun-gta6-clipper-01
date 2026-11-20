// gta6-clipper-01 entry (Node 22, standard library only).
//
// This program copies VIDEO.json from the repository root to /output/VIDEO.json,
// where the gate reads it. That is all it has to do: the entry itself is the
// YouTube video the file names. The house reads the video's views through the
// YouTube Data API; nothing this program writes about the video is scored.
//
// VIDEO.json holds a placeholder address until the clip is uploaded to YouTube
// as a public Short and its real address is written in. The gate refuses the
// placeholder, so replace it before submitting.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'VIDEO.json'), join(OUTPUT_DIR, 'VIDEO.json'));
} catch (err) {
  console.error(`VIDEO.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
