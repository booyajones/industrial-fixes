// @pagefind/default-ui ships no type declarations; declare it so astro check
// (tsc) does not error on the 404 page's search widget import.
declare module "@pagefind/default-ui";

interface Window {
  theme?: {
    themeValue: string;
    setPreference: () => void;
    reflectPreference: () => void;
    getTheme: () => string;
    setTheme: (val: string) => void;
  };
}
