import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { resolve } from "node:path";

// Vendored IBM Plex Mono fonts (committed under src/assets/fonts) so OG-image
// generation never touches the network at build time. This module used to
// fetch the fonts from Google Fonts once per generated image, which timed out
// on hosts with slow or flaky outbound and failed the whole build.

const cache = new Map<string, Buffer>();

function loadLocalFont(file: string): Buffer {
  const cached = cache.get(file);
  if (cached) return cached;

  // Primary path resolves against the project source tree, which is always
  // present during `astro build`. The import.meta.url fallback covers builds
  // that run from a non-standard working directory.
  const candidates = [
    resolve(process.cwd(), "src/assets/fonts", file),
    fileURLToPath(new URL(`../assets/fonts/${file}`, import.meta.url)),
  ];

  for (const path of candidates) {
    try {
      const data = readFileSync(path);
      cache.set(file, data);
      return data;
    } catch {
      // try the next candidate
    }
  }

  throw new Error(`Vendored font not found: ${file}`);
}

// Signature kept compatible with the previous network version. The text
// argument is no longer needed (the full font is loaded) but callers still
// pass it, so it is accepted and ignored.
async function loadGoogleFonts(
  _text?: string
): Promise<
  Array<{ name: string; data: Buffer; weight: number; style: string }>
> {
  const fontsConfig = [
    {
      name: "IBM Plex Mono",
      file: "IBMPlexMono-Regular.ttf",
      weight: 400,
      style: "normal",
    },
    {
      name: "IBM Plex Mono",
      file: "IBMPlexMono-Bold.ttf",
      weight: 700,
      style: "bold",
    },
  ];

  return fontsConfig.map(({ name, file, weight, style }) => ({
    name,
    data: loadLocalFont(file),
    weight,
    style,
  }));
}

export default loadGoogleFonts;
